# Generated by Django 5.0 on 2023-12-20 17:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_remove_user_name_user_department_user_faculty_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='date_joined',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 21, 0, 53, 44, 277372, tzinfo=datetime.timezone.utc)),
        ),
    ]
