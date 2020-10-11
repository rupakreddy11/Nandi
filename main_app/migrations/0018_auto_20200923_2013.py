# Generated by Django 3.1 on 2020-09-23 14:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0017_nonenesaleentry_t_c'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeeprofile',
            name='completed_sales',
            field=models.IntegerField(default=0, verbose_name='No of Completed Sales'),
        ),
        migrations.AlterField(
            model_name='employeeprofile',
            name='isqualified',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=10, verbose_name='Eligibility for Incentives'),
        ),
        migrations.AlterField(
            model_name='employeeprofile',
            name='target',
            field=models.IntegerField(verbose_name='Sales Target'),
        ),
        migrations.CreateModel(
            name='ENESaleEntry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_category', models.CharField(choices=[('Tractor', 'Tractor'), ('Implement', 'Implement')], max_length=50, verbose_name='Product Category')),
                ('model_name', models.CharField(max_length=100, verbose_name='Model Name')),
                ('mfg_date', models.DateField(help_text='Please mention the manufactured date in YYYY/MM/DD format', verbose_name='Product Manufactured Date')),
                ('sale_date', models.DateField(help_text='Please mention the date of sale in YYYY/MM/DD format', verbose_name='Date of Sale')),
                ('payment_type', models.CharField(choices=[('Finance', 'Finance'), ('Cash', 'Cash')], max_length=50, verbose_name='Mode of Payment')),
                ('financer', models.CharField(max_length=100, verbose_name='Financer Name')),
                ('finance_hypothecation', models.CharField(max_length=100, verbose_name='Finance Hypothecation')),
                ('sale_delivery_date', models.DateField(help_text='Please mention the sale delivery date in YYYY/MM/DD format', verbose_name='Sale Delivery Date')),
                ('temporary_registration_number', models.CharField(max_length=50, verbose_name='Temporary Registration Number')),
                ('rta_authority', models.CharField(max_length=100, verbose_name='RTA Authority')),
                ('docs_handovered', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=20, verbose_name='Documents handovered to Customer?')),
                ('employee_id', models.CharField(max_length=10, verbose_name='Employee ID')),
                ('workstation_code', models.CharField(max_length=50, verbose_name='Workstation Code')),
                ('t_c', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=20, null=True, verbose_name='Do you agree for all terms and conditions')),
                ('enrolled_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.customer', verbose_name='Enrollment ID')),
            ],
        ),
    ]