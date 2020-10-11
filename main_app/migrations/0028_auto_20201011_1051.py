# Generated by Django 3.1 on 2020-10-11 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0027_usedtractorverification_employee_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='usedtractorverification',
            name='used_trac_price',
            field=models.CharField(default=0, max_length=20, verbose_name='Used Tractor Price by Decider'),
        ),
        migrations.AlterField(
            model_name='usedtractorverification',
            name='alternate_phone_no',
            field=models.CharField(max_length=10, verbose_name='Owner Alternate Mobile No'),
        ),
        migrations.AlterField(
            model_name='usedtractorverification',
            name='ownership_no',
            field=models.CharField(max_length=20, verbose_name='Ownership Level'),
        ),
    ]
