# Generated by Django 3.1 on 2020-09-22 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0010_customer_enrol_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='new_tractor',
            field=models.CharField(choices=[('Immediate', 'Immediate'), ('Within_a_week', 'Within a week'), ('Within_a_month', 'Within a month'), ('Other', 'Other')], max_length=20, verbose_name='Planning for a new tractor in?'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='purpose_of_enrol',
            field=models.CharField(choices=[('Tractors', 'Tractors'), ('Implements', 'Implements'), ('Both', 'Both')], max_length=20, verbose_name='Purpose of Enrollment'),
        ),
    ]
