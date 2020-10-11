from .models import Customer,NonENESaleEntry, ENESaleEntry, UsedTractorVerification
from django import forms
from django.forms import ModelForm

class CustomerForm(forms.ModelForm):
	class Meta:
		model=Customer
		fields=['full_name','date_of_birth','father_name','mobile_no','alternate_mobile_no','aadhar_no','pan_no','present_address','permanent_address','purpose_of_enrol','tractor_exists','tractor_name_model','qualification','agriland_exists','land_acres','loans','new_tractor','t_c']
		field_order= ['full_name','date_of_birth','father_name','mobile_no','alternate_mobile_no','aadhar_no','pan_no','present_address','permanent_address','purpose_of_enrol','tractor_exists','tractor_name_model','qualification','agriland_exists','land_acres','loans','new_tractor','t_c']

		widgets={
		    'full_name':forms.TextInput(attrs={'class':'form-control'}),
		    'date_of_birth':forms.TextInput(attrs={'class':'form-control'}),
		    'father_name':forms.TextInput(attrs={'class':'form-control'}),
		    'mobile_no':forms.TextInput(attrs={'class':'form-control'}),
		    'alternate_mobile_no':forms.TextInput(attrs={'class':'form-control'}),
		    'aadhar_no':forms.TextInput(attrs={'class':'form-control'}),
		    'pan_no':forms.TextInput(attrs={'class':'form-control'}),
		    'present_address':forms.Textarea(attrs={'class':'form-control','rows':3, 'cols':10}),
		    'permanent_address':forms.Textarea(attrs={'class':'form-control','rows':3, 'cols':10}),
		    'purpose_of_enrol':forms.Select(attrs={'class':'form-control'}),
		    'tractor_exists':forms.Select(attrs={'class':'form-control'}),
		    'tractor_name_model':forms.TextInput(attrs={'class':'form-control'}),
		    'qualification':forms.TextInput(attrs={'class':'form-control'}),
		    'agriland_exists':forms.Select(attrs={'class':'form-control'}),
		    'land_acres':forms.TextInput(attrs={'class':'form-control'}),
		    'loans':forms.Textarea(attrs={'class':'form-control','rows':2, 'cols':10}),
		    'new_tractor':forms.Select(attrs={'class':'form-control'}),
		    't_c':forms.Select(attrs={'class':'form-control'}),
		}


class ENESaleForm(forms.ModelForm):
	class Meta:
		model=ENESaleEntry
		fields=['enrolled_id','product_category','model_name','mfg_date','sale_date','payment_type','financer','finance_hypothecation','sale_delivery_date','temporary_registration_number','rta_authority','docs_handovered','employee_id','workstation_code','t_c']
		field_order=['enrolled_id','product_category','model_name','mfg_date','sale_date','payment_type','financer','finance_hypothecation','sale_delivery_date','temporary_registration_number','rta_authority','docs_handovered','employee_id','workstation_code','t_c']

		widgets={
			'enrolled_id':forms.TextInput(attrs={'class':'form-control'}),
		    'product_category':forms.Select(attrs={'class':'form-control'}),
		    'model_name':forms.TextInput(attrs={'class':'form-control'}),
		    'mfg_date':forms.TextInput(attrs={'class':'form-control'}),
		    'sale_date':forms.TextInput(attrs={'class':'form-control'}),
		    'payment_type':forms.Select(attrs={'class':'form-control'}),
		    'financer':forms.TextInput(attrs={'class':'form-control'}),
		    'finance_hypothecation':forms.TextInput(attrs={'class':'form-control'}),
		    'sale_delivery_date':forms.TextInput(attrs={'class':'form-control'}),
		    'temporary_registration_number':forms.TextInput(attrs={'class':'form-control'}),
		    'rta_authority':forms.TextInput(attrs={'class':'form-control'}),
		    'docs_handovered':forms.Select(attrs={'class':'form-control'}),
		    'employee_id':forms.TextInput(attrs={'class':'form-control'}),
		    'workstation_code':forms.TextInput(attrs={'class':'form-control'}),
		    't_c':forms.Select(attrs={'class':'form-control'}),
		}
		

class NonENESaleForm(forms.ModelForm):
	class Meta:
		model=NonENESaleEntry
		fields=['full_name','date_of_birth','father_name','mobile_no','alternate_mobile_no','aadhar_no','pan_no','present_address','permanent_address','product_category','model_name','mfg_date','sale_date','payment_type','financer','finance_hypothecation','sale_delivery_date','temporary_registration_number','rta_authority','docs_handovered','employee_id','workstation_code','t_c']
		field_order=['full_name','date_of_birth','father_name','mobile_no','alternate_mobile_no','aadhar_no','pan_no','present_address','permanent_address','product_category','model_name','mfg_date','sale_date','payment_type','financer','finance_hypothecation','sale_delivery_date','temporary_registration_number','rta_authority','docs_handovered','employee_id','workstation_code','t_c']

		widgets={
		    'full_name':forms.TextInput(attrs={'class':'form-control'}),
		    'date_of_birth':forms.TextInput(attrs={'class':'form-control'}),
		    'father_name':forms.TextInput(attrs={'class':'form-control'}),
		    'mobile_no':forms.TextInput(attrs={'class':'form-control'}),
		    'alternate_mobile_no':forms.TextInput(attrs={'class':'form-control'}),
		    'aadhar_no':forms.TextInput(attrs={'class':'form-control'}),
		    'pan_no':forms.TextInput(attrs={'class':'form-control'}),
		    'present_address':forms.Textarea(attrs={'class':'form-control','rows':3, 'cols':10}),
		    'permanent_address':forms.Textarea(attrs={'class':'form-control','rows':3, 'cols':10}),
		    'product_category':forms.Select(attrs={'class':'form-control'}),
		    'model_name':forms.TextInput(attrs={'class':'form-control'}),
		    'mfg_date':forms.TextInput(attrs={'class':'form-control'}),
		    'sale_date':forms.TextInput(attrs={'class':'form-control'}),
		    'payment_type':forms.Select(attrs={'class':'form-control'}),
		    'financer':forms.TextInput(attrs={'class':'form-control'}),
		    'finance_hypothecation':forms.TextInput(attrs={'class':'form-control'}),
		    'sale_delivery_date':forms.TextInput(attrs={'class':'form-control'}),
		    'temporary_registration_number':forms.TextInput(attrs={'class':'form-control'}),
		    'rta_authority':forms.TextInput(attrs={'class':'form-control'}),
		    'docs_handovered':forms.Select(attrs={'class':'form-control'}),
		    'employee_id':forms.TextInput(attrs={'class':'form-control'}),
		    'workstation_code':forms.TextInput(attrs={'class':'form-control'}),
		    't_c':forms.Select(attrs={'class':'form-control'}),
		}

class UsedTractorVerificationForm(forms.ModelForm):
	class Meta:
		model=UsedTractorVerification
		fields=['registration_no','mfg_date','model_name','kms_driven','ownership_no','usage','phone_no','alternate_phone_no','customer_price_expectation','looking_for','employee_id','eng_no_pic','meter_reading_pic','front_side_pic','back_side_pic','right_side_pic','left_side_pic','tires_pic','t_c']
		field_order=['registration_no','mfg_date','model_name','kms_driven','ownership_no','usage','phone_no','alternate_phone_no','customer_price_expectation','looking_for','employee_id','eng_no_pic','meter_reading_pic','front_side_pic','back_side_pic','right_side_pic','left_side_pic','tires_pic','t_c']

		widgets={
			'registration_no':forms.TextInput(attrs={'class':'form-control'}),
			'mfg_date':forms.TextInput(attrs={'class':'form-control'}),
			'model_name':forms.TextInput(attrs={'class':'form-control'}),
			'kms_driven':forms.TextInput(attrs={'class':'form-control'}),
			'ownership_no':forms.TextInput(attrs={'class':'form-control'}),
			'usage':forms.Select(attrs={'class':'form-control'}),
			'phone_no':forms.TextInput(attrs={'class':'form-control'}),
			'alternate_phone_no':forms.TextInput(attrs={'class':'form-control'}),
			'customer_price_expectation':forms.TextInput(attrs={'class':'form-control'}),
			'looking_for':forms.Select(attrs={'class':'form-control'}),
			'employee_id':forms.TextInput(attrs={'class':'form-control'}),
			't_c':forms.Select(attrs={'class':'form-control'}),
		}