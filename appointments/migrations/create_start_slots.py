from django.db import migrations, models
from appointments.models import Slot, Saloon, Master

from datetime import datetime, date, timedelta, time

NUMBER_OF_AVAILABLE_DAYS = 14
SLOTS_PER_DAY = 18
WORK_STARTING_HOUR = 9


def create_starting_slots(apps, schema_editor):
    saloon = Saloon.objects.create(name='Дефолт-салон', address='Дефолт-сити, улица Дефолт, 25')
    today = date.today()
    for master_name in ['Ольга', 'Татьяна']:
        master = Master(name=master_name)
        master.save()
        for day in range(NUMBER_OF_AVAILABLE_DAYS):
            this_date = today + timedelta(days=day)
            base_datetime = datetime.combine(this_date, time.min) + timedelta(hours=WORK_STARTING_HOUR)
            for slot in range(SLOTS_PER_DAY):
                slot_datetime = base_datetime + timedelta(minutes=30)*slot
                Slot.objects.create(saloon=saloon, start_datetime=slot_datetime, master=master)


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('appointments', '0001_initial'),
        ('appointments', '0002_alter_slot_client_alter_slot_master_and_more')
    ]

    operations = [
        migrations.RunPython(create_starting_slots),
    ]