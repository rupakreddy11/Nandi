from django.db import models
from django.contrib.auth.models import User

class EmployeeProfile(models.Model):
	BOOLEAN_CHOICES=(
		('Yes','Yes'),
		('No','No'),
		)
	user=models.OneToOneField(User, on_delete=models.CASCADE)
	Empid=models.CharField(max_length=10,verbose_name='Employee ID')
	target=models.IntegerField(verbose_name='Sales Target')
	completed_sales=models.IntegerField(verbose_name='No of Completed Sales',default=0)
	isqualified=models.CharField(verbose_name='Eligibility for Incentives',max_length=10,choices=BOOLEAN_CHOICES)
	workstation=models.CharField(max_length=50, default='Hyderabad',verbose_name='Workstation Code')
	empimage=models.ImageField(verbose_name='Employee Profile Image',upload_to='Images',blank=True)

	def __str__(self):
		return self.user.username+' '+self.Empid

class Customer(models.Model):
	PURPOSE_CHOICES=(
		('Tractors','Tractors'),
		('Implements','Implements'),
		('Both','Both'),
		)
	BOOLEAN_CHOICES=(
		('Yes','Yes'),
		('No','No'),
		)
	NEWTRACTOR_CHOICES=(
		('Immediate','Immediate'),
		('Within_a_week','Within a week'),
		('Within_a_month','Within a month'),
		('Other','Other'))
	enrol_id=models.CharField(verbose_name='Customer Id',max_length=9,null=True)
	full_name=models.CharField(verbose_name='Full Name',max_length=100)
	date_of_birth=models.DateField(verbose_name='Date of Birth',help_text='Please mention the date of birth in YYYY-MM-DD format')
	father_name=models.CharField(verbose_name='Father Name',max_length=100)
	mobile_no=models.CharField(verbose_name='Mobile No',max_length=10)
	alternate_mobile_no=models.CharField(verbose_name='Alternate Mobile No',max_length=10)
	aadhar_no=models.CharField(verbose_name='Aadhar Card Number',max_length=12,help_text='Please enter the correct Aadhar number')
	pan_no=models.CharField(verbose_name='PAN Card Number',max_length=10,help_text='Please enter the correct PAN number')
	present_address=models.TextField(verbose_name='Present Address',null=True)
	permanent_address=models.TextField(verbose_name='Permanent Address',null=True)
	purpose_of_enrol=models.CharField(verbose_name='Purpose of Enrollment',max_length=20,choices=PURPOSE_CHOICES)
	tractor_exists=models.CharField(verbose_name='Do you have a tractor?',max_length=20,choices=BOOLEAN_CHOICES)
	tractor_name_model=models.CharField(verbose_name='Tractor Name & Model',max_length=300)
	qualification=models.CharField(max_length=200)
	agriland_exists=models.CharField(verbose_name='Do you have agriculture land?',max_length=20,choices=BOOLEAN_CHOICES)
	land_acres=models.DecimalField(verbose_name='Land in acres',max_digits=5,decimal_places=2)
	loans=models.TextField(verbose_name='Loan Details')
	new_tractor=models.CharField(max_length=20,choices=NEWTRACTOR_CHOICES,verbose_name='Planning for a new tractor in?')
	employee_id=models.CharField(max_length=20,verbose_name='Employee ID',blank=True)
	t_c=models.CharField(verbose_name='Do you agree?',max_length=20,choices=BOOLEAN_CHOICES)

	class Meta:
		verbose_name="Enrolled Customer"
		verbose_name_plural="Enrolled Customers"


	def __str__(self):
		return self.enrol_id+' '+self.employee_id



class ENESaleEntry(models.Model):
	PRODUCT_CHOICES=(
		('Tractor','Tractor'),
		('Implement','Implement'),
		)
	PAYMENT_CHOICES=(
		('Finance','Finance'),
		('Cash','Cash'),
		)
	DOCS_CHOICES=(
		('Yes','Yes'),
		('No','No'),
		)
	enrolled_id=models.CharField(verbose_name='Enrollment ID',max_length=9,blank=True)
	sale_id=models.CharField(verbose_name='Sale ID',max_length=9,blank=True)
	product_category=models.CharField(verbose_name='Product Category',max_length=50,choices=PRODUCT_CHOICES)
	model_name=models.CharField(verbose_name='Model Name',max_length=100)
	mfg_date=models.DateField(verbose_name='Product Manufactured Date',help_text='Please mention the manufactured date in YYYY-MM-DD format')
	sale_date=models.DateField(verbose_name='Date of Sale',help_text='Please mention the date of sale in YYYY/MM/DD format')
	payment_type=models.CharField(verbose_name='Mode of Payment',max_length=50,choices=PAYMENT_CHOICES)
	financer=models.CharField(verbose_name='Financer Name',max_length=100)
	finance_hypothecation=models.CharField(verbose_name='Finance Hypothecation',max_length=100)
	sale_delivery_date=models.DateField(verbose_name='Sale Delivery Date',help_text='Please mention the sale delivery date in YYYY-MM-DD format')
	temporary_registration_number=models.CharField(verbose_name='Temporary Registration Number',max_length=50)
	rta_authority=models.CharField(verbose_name='RTA Authority',max_length=100)
	docs_handovered=models.CharField(verbose_name='Documents handovered to Customer?',max_length=20,choices=DOCS_CHOICES)
	employee_id=models.CharField(verbose_name='Employee ID',max_length=10)
	workstation_code=models.CharField(verbose_name='Workstation Code',max_length=50)
	t_c=models.CharField(verbose_name='Do you agree for all terms and conditions',max_length=20,choices=DOCS_CHOICES,null=True)

	class Meta:
		verbose_name="Enrolled Customers Sale Entry"
		verbose_name_plural="Enrolled Customers Sale Entries"

	def __str__(self):
		return self.enrolled_id+' made by '+self.employee_id


class NonENESaleEntry(models.Model):
	PRODUCT_CHOICES=(
		('Tractor','Tractor'),
		('Implement','Implement'),
		)
	PAYMENT_CHOICES=(
		('Finance','Finance'),
		('Cash','Cash'),
		)
	DOCS_CHOICES=(
		('Yes','Yes'),
		('No','No'),
		)
	sale_id=models.CharField(verbose_name='Sale ID',max_length=9)
	full_name=models.CharField(verbose_name='Full Name',max_length=100)
	date_of_birth=models.DateField(verbose_name='Date of Birth',help_text='Please mention the date of birth in YYYY-MM-DD format')
	father_name=models.CharField(verbose_name='Father Name',max_length=100)
	mobile_no=models.CharField(verbose_name='Mobile No',max_length=10)
	alternate_mobile_no=models.CharField(verbose_name='Alternate Mobile No',max_length=10)
	aadhar_no=models.CharField(verbose_name='Aadhar Card Number',max_length=12,help_text='Please enter the correct Aadhar number')
	pan_no=models.CharField(verbose_name='PAN Card Number',max_length=10,help_text='Please enter the correct PAN number')
	present_address=models.TextField(verbose_name='Present Address',null=True)
	permanent_address=models.TextField(verbose_name='Permanent Address',null=True)
	product_category=models.CharField(verbose_name='Product Category',max_length=50,choices=PRODUCT_CHOICES)
	model_name=models.CharField(verbose_name='Model Name',max_length=100)
	mfg_date=models.DateField(verbose_name='Product Manufactured Date',help_text='Please mention the manufactured date in YYYY-MM-DD format')
	sale_date=models.DateField(verbose_name='Date of Sale',help_text='Please mention the date of sale in YYYY-MM-DD format')
	payment_type=models.CharField(verbose_name='Mode of Payment',max_length=50,choices=PAYMENT_CHOICES)
	financer=models.CharField(verbose_name='Financer Name',max_length=100)
	finance_hypothecation=models.CharField(verbose_name='Finance Hypothecation',max_length=100)
	sale_delivery_date=models.DateField(verbose_name='Sale Delivery Date',help_text='Please mention the sale delivery date in YYYY-MM-DD format')
	temporary_registration_number=models.CharField(verbose_name='Temporary Registration Number',max_length=50)
	rta_authority=models.CharField(verbose_name='RTA Authority',max_length=100)
	docs_handovered=models.CharField(verbose_name='Documents handovered to Customer?',max_length=20,choices=DOCS_CHOICES)
	employee_id=models.CharField(verbose_name='Employee ID',max_length=10)
	workstation_code=models.CharField(verbose_name='Workstation Code',max_length=50)
	t_c=models.CharField(verbose_name='Do you agree for all terms and conditions',max_length=20,choices=DOCS_CHOICES,null=True)

	class Meta:
		verbose_name="Non Enrolled Customers Sale Entry"
		verbose_name_plural="Non Enrolled Customers Sale Entries"

	def __str__(self):
		return self.sale_id+' made by '+self.employee_id


class UsedTractorVerification(models.Model):
	USAGE_CHOICES=(
		('Agriculture','Agriculture'),
		('Commercial','Commercial'),
		)
	TYPE_CHOICES=(
		('Sale','Sale'),
		('Exchange','Exchange'),
		)
	DOCS_CHOICES=(
		('Yes','Yes'),
		('No','No'),
		)
	verification_id=models.CharField(verbose_name='Verification Id',max_length=9,blank=True)
	used_trac_price=models.CharField(verbose_name='Used Tractor Price by Decider',max_length=20,default=0)
	registration_no=models.CharField(verbose_name='Tractor Registration No',max_length=20)
	mfg_date=models.DateField(verbose_name='Date of Manufacture',help_text='Please mention the date of birth in YYYY-MM-DD format')
	model_name=models.CharField(verbose_name='Model Name',max_length=100)
	kms_driven=models.CharField(verbose_name='No of Kilometers Driven',max_length=20)
	ownership_no=models.CharField(verbose_name='Ownership Level',max_length=20)
	usage=models.CharField(verbose_name='Usage Purpose',max_length=50,choices=USAGE_CHOICES)
	phone_no=models.CharField(max_length=10,verbose_name='Owner Mobile No')
	alternate_phone_no=models.CharField(max_length=10,verbose_name='Owner Alternate Mobile No')
	customer_price_expectation=models.CharField(max_length=20,verbose_name='Price Expectation for Used Tractor')
	looking_for=models.CharField(max_length=20,verbose_name='Sale or Exchange?',choices=TYPE_CHOICES)
	eng_no_pic=models.ImageField(upload_to='Images',verbose_name='Photo of Engine No')
	meter_reading_pic=models.ImageField(upload_to='Images',verbose_name='Photo of Meter Reading')
	front_side_pic=models.ImageField(upload_to='Images',verbose_name='Front Side Photo of Tractor')
	back_side_pic=models.ImageField(upload_to='Images',verbose_name='Back Side Photo of Tractor')
	right_side_pic=models.ImageField(upload_to='Images',verbose_name='Right Side Photo of Tractor')
	left_side_pic=models.ImageField(upload_to='Images',verbose_name='Left Side Photo of Tractor')
	tires_pic=models.ImageField(upload_to='Images',verbose_name='Photo of Tires')
	employee_id=models.CharField(max_length=20,verbose_name='Employee ID',blank=True)
	t_c=models.CharField(verbose_name='Do you agree for all terms and conditions',max_length=20,choices=DOCS_CHOICES)

	class Meta:
		verbose_name='Used Tractor Verification Entry'
		verbose_name_plural='Used Tractor Verification Entries'

	def __str__(self):
		return self.registration_no+' entry made by '+self.employee_id