from django.core.management.base import BaseCommand
import datetime
from workers.models import Worker, Shift

class Command(BaseCommand):
    def handle(self, *args, **options):
        #удаляем старые данные из таблиц бд
        Worker.objects.all().delete()
        Shift.objects.all().delete()


        #заполняем бд тестовыми данными работников
        workers = [{'name': 'worker', 'surname': '1'}, {'name': 'worker', 'surname': '2'}, {'name': 'worker', 'surname': '3'},
                   {'name': 'worker', 'surname': '4'}, {'name': 'worker', 'surname': '5'}, {'name': 'worker', 'surname': '6'},
                   {'name': 'worker', 'surname': '7'}, {'name': 'worker', 'surname': '8'}, {'name': 'worker', 'surname': '9'},
                   {'name': 'worker', 'surname': '10'}]
        for worker in workers:
            Worker.save(Worker(**worker))
        workers = []

        START_TIME = (8, 10)
        END_TIME = (20, 22)

        DEFAULT_SHIFT = 12

        WORKERS_LEN = 10
        MAX_HOURS = 144

        YEAR = 2023

        MOUNTHS = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        for i in range(WORKERS_LEN):
            workers.append([[] for i in range(12)])

        days_sum = 0
        last_worker = 0

        #создаем план работы
        for j, mounth in enumerate(MOUNTHS):
            worker_mean = int((MAX_HOURS / DEFAULT_SHIFT * WORKERS_LEN) / mounth)
            for i in range(1, mounth + 1):
                date = datetime.date(YEAR, j + 1, i)
                if date.weekday() == 0:
                    day_load = worker_mean + 1
                elif date.weekday() == 6:
                    day_load = worker_mean - 1
                else:
                    day_load = worker_mean

                if last_worker + day_load < WORKERS_LEN:
                    workers_with_shift = workers[last_worker:last_worker + day_load]
                    last_worker = last_worker + day_load
                else:
                    workers_with_shift = workers[last_worker:WORKERS_LEN] + workers[0:day_load - (WORKERS_LEN - last_worker)]
                    last_worker = day_load - WORKERS_LEN + last_worker
                for q, worker in enumerate(workers_with_shift):
                    shift_start = datetime.datetime(date.year, date.month, date.day, START_TIME[q % 2])
                    worker[j].append(str(shift_start))
                days_sum += 1

        #Записываем план в бд
        start_id = Worker.objects.first().id
        for i, worker in enumerate(workers):
            for j, mounth in enumerate(worker):
                for shift in mounth:
                    Shift.save(Shift(worker_id=start_id+i, date=shift))


