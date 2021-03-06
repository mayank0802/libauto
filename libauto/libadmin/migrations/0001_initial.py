# Generated by Django 2.2.4 on 2020-01-13 13:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='book_info',
            fields=[
                ('book_id', models.AutoField(primary_key=True, serialize=False)),
                ('book_name', models.CharField(max_length=50)),
                ('book_author', models.CharField(max_length=50)),
                ('book_student', models.CharField(max_length=50)),
                ('book_submission', models.DateField(default=datetime.date.today)),
                ('book_issue', models.DateField(default=datetime.date.today)),
            ],
        ),
    ]
