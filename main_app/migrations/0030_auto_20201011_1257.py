# Generated by Django 3.1 on 2020-10-11 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0029_auto_20201011_1251'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usedtractorverification',
            name='used_trac_price',
            field=models.CharField(default=0, max_length=20, verbose_name='Used Tractor Price by Decider'),
        ),
    ]
