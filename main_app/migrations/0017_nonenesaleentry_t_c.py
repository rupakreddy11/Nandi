# Generated by Django 3.1 on 2020-09-23 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0016_auto_20200923_1559'),
    ]

    operations = [
        migrations.AddField(
            model_name='nonenesaleentry',
            name='t_c',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=20, null=True, verbose_name='Do you agree for all terms and conditions'),
        ),
    ]