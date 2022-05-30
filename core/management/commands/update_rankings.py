from django.core.management import BaseCommand
from django_redis import get_redis_connection
from common.services import UserService


class Command(BaseCommand):
    def handle(self, *args, **options):
        con = get_redis_connection("default")

        users = UserService.get('users')
        ambassadors = filter(lambda a: a['is_ambassador'] == 1, users)

        for ambassador in ambassadors:
            name = ambassador['first_name'] + ' ' + ambassador['last_name']
            con.zadd('rankings', {name: float(ambassador['revenue'])})
