from django.core.management.base import BaseCommand
from workers.models import Mounth

class Command(BaseCommand):

    def handle(self, *args, **options):
        if Mounth.objects.all().count() == 0:
            MOUNTHS = ['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август',
                      'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь']
            for mounth in MOUNTHS:
                Mounth.save(Mounth(name=mounth))