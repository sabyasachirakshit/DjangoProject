# Generated by Django 3.1.3 on 2021-06-06 21:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cse', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='excelfile',
            name='Qn_No',
            field=models.IntegerField(),
        ),
    ]
