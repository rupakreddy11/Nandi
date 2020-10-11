# Generated by Django 3.1 on 2020-10-05 02:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0022_auto_20200925_0743'),
    ]

    operations = [
        migrations.CreateModel(
            name='UsedTractorVerification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('registration_no', models.CharField(max_length=20, verbose_name='Tractor Registration No')),
                ('mfg_date', models.DateField(help_text='Please mention the date of birth in YYYY/MM/DD format', verbose_name='Date of Manufacture')),
                ('model_name', models.CharField(max_length=100, verbose_name='Model Name')),
                ('kms_driven', models.CharField(max_length=20, verbose_name='No of Kilometers Driven')),
                ('ownership_no', models.CharField(max_length=20, verbose_name='Ownership No')),
                ('usage', models.CharField(choices=[('Agriculture', 'Agriculture'), ('Commercial', 'Commercial')], max_length=50, verbose_name='Usage Purpose')),
                ('phone_no', models.CharField(max_length=10, verbose_name='Owner Mobile No')),
                ('alternate_phone_no', models.CharField(max_length=10, verbose_name='Owner Mobile No')),
                ('customer_price_expectation', models.CharField(max_length=20, verbose_name='Price Expectation for Used Tractor')),
                ('looking_for', models.CharField(choices=[('Sale', 'Sale'), ('Commercial', 'Commercial')], max_length=20, verbose_name='Sale or Exchange?')),
                ('eng_no_pic', models.ImageField(upload_to='Images', verbose_name='Photo of Engine No')),
                ('meter_reading_pic', models.ImageField(upload_to='Images', verbose_name='Photo of Meter Reading')),
                ('front_side_pic', models.ImageField(upload_to='Images', verbose_name='Front Side Photo of Tractor')),
                ('back_side_pic', models.ImageField(upload_to='Images', verbose_name='Back Side Photo of Tractor')),
                ('right_side_pic', models.ImageField(upload_to='Images', verbose_name='Right Side Photo of Tractor')),
                ('left_side_pic', models.ImageField(upload_to='Images', verbose_name='Left Side Photo of Tractor')),
                ('tires_pic', models.ImageField(upload_to='Images', verbose_name='Photo of Tires')),
                ('t_c', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=20, verbose_name='Do you agree for all terms and conditions')),
            ],
            options={
                'verbose_name': 'Used Tractor Validation Entries',
                'verbose_name_plural': 'Used Tractor Validations Entries',
            },
        ),
    ]
