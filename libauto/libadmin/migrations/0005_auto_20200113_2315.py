# Generated by Django 2.2.4 on 2020-01-13 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libadmin', '0004_auto_20200113_2242'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book_info',
            name='bk_student_id',
            field=models.IntegerField(default=-1),
        ),
    ]
