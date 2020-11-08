from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import EmployeeProfile, Customer, ENESaleEntry, NonENESaleEntry, UsedTractorVerification 
from .forms import CustomerForm, ENESaleForm, NonENESaleForm, UsedTractorVerificationForm
from django.core.mail import send_mail
import uuid

def home(request):
	return render(request, 'Nandi/index.html',{})

def User_login(request):
	if request.method=='POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password= password)
		if user is not None:
			login(request, user)
			messages.success(request, 'You have successfully logged In!!!')
			return redirect('exec-log')
		else:
			messages.success(request, 'Invalid credentials, Try again...')
			return redirect('login')
	else:
		return render(request, 'Nandi/login.html', {})

def User_logout(request):
	logout(request)
	messages.success(request, ' You have been logged out...')
	return redirect('home')


def Tractors(request):
	return render(request,'Nandi/tractors.html',{})

def Implemns(request):
	return render(request,'Nandi/implements.html',{})

def UsedTracs(request):
	return render(request,'Nandi/used-tractors.html',{})

def Nandi_Farming(request):
	return render(request,'Nandi/nandi-farming.html',{})

def Dealer(request):
	return render(request,'Nandi/dealers-list.html',{})

def MasseyDealer(request):
	return render(request,'Nandi/massey-dealer.html',{})

def MahindraDealers(request):
	return render(request,'Nandi/mahindra-dealers.html',{})

def SwarajDealers(request):
	return render(request,'Nandi/swaraj-dealers.html',{})

def JDDealers(request):
	return render(request,'Nandi/JD-dealers.html',{})

def SonalikaDealers(request):
	return render(request,'Nandi/sonalika-dealers.html',{})

def ForceDealers(request):
	return render(request,'Nandi/force-dealers.html',{})

def About(request):
	return render(request,'Nandi/about.html',{})

def Contact(request):
	if request.method=="POST":
		contact_name = request.POST['contact_name']
		contact_mail = request.POST['contact_mail']
		message = request.POST['message']

		send_mail(
			'message from'+contact_name,
			message,
			contact_mail,
			['contact.nanditractors@gmail.com'],
			)

	else:
		return render(request,'Nandi/contact.html',{})





@login_required(login_url="/login")
def Exec_log(request):
	if request.user.is_authenticated:
		emp=EmployeeProfile.objects.get(user=request.user)
		return render(request, 'Nandi/exec-profile.html',{'emp':emp})
	else:
		return render(request, 'Nandi/login.html',{})

@login_required(login_url="/login")
def Custom(request):
	if request.method=='POST':
		form=CustomerForm(request.POST)
		if form.is_valid():
			nf=form.save(commit=False)
			unq_val=uuid.uuid4().hex[:9].upper()
			nf.enrol_id=unq_val
			nf.save()
			p=Customer.objects.get(enrol_id=unq_val)
			return render(request,'Nandi/customer-enrol.html',{'p':p})
	else:
		form=CustomerForm()

	return render(request, 'Nandi/customer-enrol.html',{'form':form})

@login_required(login_url="/login")
def SaleEntry(request):
	return render(request,'Nandi/sale-entry-option.html',{})


@login_required(login_url="/login")
def EneSaleCheck(request):
	if request.method=='POST':
		enrolled_id=request.POST['enrolled_id']
		match=Customer.objects.filter(enrol_id=enrolled_id).exists()
		if match:
			p=Customer.objects.get(enrol_id=enrolled_id)
			return render(request,'Nandi/ene-sale-check.html',{'p':p,'match':match})
		else:
			messages.success(request,'Invalid Enrollment ID or Not a enrolled customer')
			return render(request,'Nandi/ene-sale-check.html',{})
	else:
		return render(request,'Nandi/ene-sale-check.html',{})

@login_required(login_url="/login")
def EneSaleEntry(request):
	if request.method=='POST':
		p=EmployeeProfile.objects.get(user=request.user)
		form=ENESaleForm(request.POST)
		if form.is_valid():
			nf=form.save(commit=False)
			val=uuid.uuid4().hex[:9].upper()
			nf.sale_id=val
			nf.save()
			p.completed_sales+=1
			p.save()
			q=ENESaleEntry.objects.get(sale_id=val)
			return render(request,'Nandi/ene-sale-entry.html',{'q':q})
	else:
		form=ENESaleForm()

	return render(request,'Nandi/ene-sale-entry.html',{'form':form})

@login_required(login_url="/login")
def NonEneSaleEntry(request):
	if request.method=='POST':
		p=EmployeeProfile.objects.get(user=request.user)
		form=NonENESaleForm(request.POST)
		if form.is_valid():
			nf=form.save(commit=False)
			val=uuid.uuid4().hex[:9].upper()
			nf.sale_id=val
			nf.save()
			p.completed_sales+=1
			p.save()
			q=NonENESaleEntry.objects.get(sale_id=val)
			return render(request,'Nandi/non-ene-sale-entry.html',{'q':q})
	else:
		form=NonENESaleForm()

	return render(request,'Nandi/non-ene-sale-entry.html',{'form':form})

@login_required(login_url="/login")
def UsedTracVerificationEntry(request):
	if request.method=='POST':
		form=UsedTractorVerificationForm(request.POST,request.FILES)
		if form.is_valid():
			nf=form.save(commit=False)
			val=uuid.uuid4().hex[:9].upper()
			nf.verification_id=val
			nf.save()
			q=UsedTractorVerification.objects.get(verification_id=val)
			return render(request,'Nandi/used-trac-verify-entry.html',{'q':q})
	else:
		form=UsedTractorVerificationForm()

	return render(request,'Nandi/used-trac-verify-entry.html',{'form':form})

@login_required(login_url="/login")
def UsedTracStatusCheck(request):
	if request.method=='POST':
		verify_id=request.POST['verification_id']
		match=UsedTractorVerification.objects.filter(verification_id=verify_id)
		if match:
			p=UsedTractorVerification.objects.get(verification_id=verify_id)
			return render(request,'Nandi/used-trac-status-check.html',{'p':p,'match':match})
		else:
			messages.success(request,'Invalid Verification ID')
			return render(request,'Nandi/used-trac-status-check.html',{})
	else:
		return render(request,'Nandi/used-trac-status-check.html',{})
 

@login_required(login_url="/login")
def CustEneCheck(request):
	if request.method=='POST':
		enrolled_id=request.POST['enrolled_id']
		match=Customer.objects.filter(enrol_id=enrolled_id).exists()
		if match:
			p=Customer.objects.get(enrol_id=enrolled_id)
			return render(request,'Nandi/cust-ene-status-check.html',{'p':p,'match':match})
		else:
			messages.success(request,'Invalid Enrollment ID or Not a enrolled customer')
			return render(request,'Nandi/cust-ene-status-check.html',{})
	else:
		return render(request,'Nandi/cust-ene-status-check.html',{})


#Tractors

# Mahindra Tractors
def MD_245DI_ORC(request):
	return render(request,'Nandi/tractors/Mahindra/245-DI-Orchard.html',{})

def MD_255DI_PP(request):
	return render(request,'Nandi/tractors/Mahindra/255-DI-Power-Plus.html',{})

def MD_265DI_PP(request):
	return render(request,'Nandi/tractors/Mahindra/265-DI-Power-Plus.html',{})

def MD_265DI(request):
	return render(request,'Nandi/tractors/Mahindra/265-DI.html',{})

def MD_275DI_ECO(request):
	return render(request,'Nandi/tractors/Mahindra/275-DI-ECO.html',{})

def MD_275DI_TU(request):
	return render(request,'Nandi/tractors/Mahindra/275-DI-TU.html',{})

def MD_275DI_XP_Plus(request):
	return render(request,'Nandi/tractors/Mahindra/275-DI-XP-Plus.html',{})

def MD_415DI(request):
	return render(request,'Nandi/tractors/Mahindra/415-DI.html',{})

def MD_475DI_XP_Plus(request):
	return render(request,'Nandi/tractors/Mahindra/475-DI-XP-Plus.html',{})

def MD_475DI_SP(request):
	return render(request,'Nandi/tractors/Mahindra/475-di-sp-plus.html',{})

def MD_475DI(request):
	return render(request,'Nandi/tractors/Mahindra/475-DI.html',{})

def MD_555DI_PP(request):
	return render(request,'Nandi/tractors/Mahindra/555-DI-Power-Plus.html',{})

def MD_575DI_XP_Plus(request):
	return render(request,'Nandi/tractors/Mahindra/575-DI-XP-Plus.html',{})

def MD_575DI(request):
	return render(request,'Nandi/tractors/Mahindra/575-DI.html',{})

def MD_585DI_XP_Plus(request):
	return render(request,'Nandi/tractors/Mahindra/585-DI-XP-Plus.html',{})

def MD_585DI(request):
	return render(request,'Nandi/tractors/Mahindra/585-DI.html',{})

def MD_595DI(request):
	return render(request,'Nandi/tractors/Mahindra/595-DI.html',{})

def MD_Arj_555DI(request):
	return render(request,'Nandi/tractors/Mahindra/Arjun-555-DI.html',{})

def MD_Arj_605DI_Ultra(request):
	return render(request,'Nandi/tractors/Mahindra/Arjun-605-DI-Ultra-1.html',{})

def MD_Arj_605DI_i_4WD(request):
	return render(request,'Nandi/tractors/Mahindra/Arjun-Novo-605-DI-i-4WD.html',{})

def MD_Arj_605DI_i_AC(request):
	return render(request,'Nandi/tractors/Mahindra/Arjun-Novo-605-DI-i-with-AC-Cabin.html',{})

def MD_Arj_605DI_MS(request):
	return render(request,'Nandi/tractors/Mahindra/Arjun-Novo-605-DI-MS.html',{})

def MD_Arj_605DI_PS(request):
	return render(request,'Nandi/tractors/Mahindra/Arjun-Novo-605-DI-PS.html',{})

def MD_JIVO_225DI(request):
	return render(request,'Nandi/tractors/Mahindra/JIVO-225-DI.html',{})

def MD_JIVO_245DI(request):
	return render(request,'Nandi/tractors/Mahindra/JIVO-245-DI.html',{})

def MD_JIVO_365DI(request):
	return render(request,'Nandi/tractors/Mahindra/JIVO-365DI-4WD.html',{})

def MD_NOVO_655DI(request):
	return render(request,'Nandi/tractors/Mahindra/Novo-655DI.html',{})

def MD_NOVO_755DI(request):
	return render(request,'Nandi/tractors/Mahindra/Novo-755-DI.html',{})

def MD_YUVO_265DI(request):
	return render(request,'Nandi/tractors/Mahindra/Yuvo-265-DI.html',{})

def MD_YUVO_415DI(request):
	return render(request,'Nandi/tractors/Mahindra/YUVO-415-DI.html',{})

def MD_YUVO_475DI(request):
	return render(request,'Nandi/tractors/Mahindra/YUVO-475-DI.html',{})

def MD_YUVO_575DI(request):
	return render(request,'Nandi/tractors/Mahindra/Yuvo-575-DI.html',{})

def MD_YUVO_275DI(request):
	return render(request,'Nandi/tractors/Mahindra/yuvo-275DI.html',{})

def MD_YUVO_575DI_4WD(request):
	return render(request,'Nandi/tractors/Mahindra/yuvo-575DI-4WD.html',{})

def MD_YUVRAJ_215_NXT(request):
	return render(request,'Nandi/tractors/Mahindra/Yuvraj-215-NXT.html',{})


#Swaraj Tractors
def SJ_717(request):
	return render(request,'Nandi/tractors/Swaraj/Swaraj-717.html',{})

def SJ_724_XM_ORC_NT(request):
	return render(request,'Nandi/tractors/Swaraj/Swaraj-724-XM-Orchard-NT.html',{})

def SJ_724_XM(request):
	return render(request,'Nandi/tractors/Swaraj/Swaraj-724-XM.html',{})

def SJ_735_FE(request):
	return render(request,'Nandi/tractors/Swaraj/Swaraj-735-FE.html',{})

def SJ_735_XM(request):
	return render(request,'Nandi/tractors/Swaraj/Swaraj-735-XM.html',{})

def SJ_735_XT(request):
	return render(request,'Nandi/tractors/Swaraj/Swaraj-735-XT.html',{})

def SJ_742_FE(request):
	return render(request,'Nandi/tractors/Swaraj/Swaraj-742-FE.html',{})

def SJ_742_XT(request):
	return render(request,'Nandi/tractors/Swaraj/Swaraj-742-XT.html',{})

def SJ_744_FE_PE(request):
	return render(request,'Nandi/tractors/Swaraj/Swaraj-744-FE-Potato-Expert.html',{})

def SJ_744_FE(request):
	return render(request,'Nandi/tractors/Swaraj/Swaraj-744-FE.html',{})

def SJ_744_XT(request):
	return render(request,'Nandi/tractors/Swaraj/Swaraj-744-XT.html',{})

def SJ_825_XM(request):
	return render(request,'Nandi/tractors/Swaraj/Swaraj-825-XM.html',{})

def SJ_834_XM(request):
	return render(request,'Nandi/tractors/Swaraj/Swaraj-834-XM.html',{})

def SJ_841_XM(request):
	return render(request,'Nandi/tractors/Swaraj/Swaraj-841-XM.html',{})

def SJ_843_XM_OSM(request):
	return render(request,'Nandi/tractors/Swaraj/Swaraj-843-XM-OSM.html',{})

def SJ_843_XM(request):
	return render(request,'Nandi/tractors/Swaraj/Swaraj-843-XM.html',{})

def SJ_855_FE(request):
	return render(request,'Nandi/tractors/Swaraj/Swaraj-855-FE.html',{})

def SJ_855_XM(request):
	return render(request,'Nandi/tractors/Swaraj/Swaraj-855-XM.html',{})

def SJ_960_FE(request):
	return render(request,'Nandi/tractors/Swaraj/Swaraj-960-FE.html',{})

def SJ_963_FE(request):
	return render(request,'Nandi/tractors/Swaraj/Swaraj-963-FE.html',{})


#Massey Tractors
def MF_1030_DI_MS(request):
	return render(request,'Nandi/tractors/Massey/1030-DI-Mahashakti.html',{})

def MF_1035_DI_DOST(request):
	return render(request,'Nandi/tractors/Massey/1035-DI-Dost.html',{})

def MF_1035_DI_MS(request):
	return render(request,'Nandi/tractors/Massey/1035-DI-Mahashakti.html',{})

def MF_1035_DI_PP(request):
	return render(request,'Nandi/tractors/Massey/1035-DI-Planetary-Plus.html',{})

def MF_1035_DI_TONNER(request):
	return render(request,'Nandi/tractors/Massey/1035-DI-Tonner.html',{})

def MF_1035_DI(request):
	return render(request,'Nandi/tractors/Massey/1035-DI.html',{})

def MF_1134_DI(request):
	return render(request,'Nandi/tractors/Massey/1134-DI.html',{})

def MF_241_DI_DT(request):
	return render(request,'Nandi/tractors/Massey/241-DI-Dynatech.html',{})

def MF_241_DI_MAHAAN(request):
	return render(request,'Nandi/tractors/Massey/241-DI-Mahaan.html',{})

def MF_241_DI_PP(request):
	return render(request,'Nandi/tractors/Massey/241-DI-Planetary-plus.html',{})

def MF_241_DI_TONNER(request):
	return render(request,'Nandi/tractors/Massey/241-DI-Tonner.html',{})

def MF_241_DI(request):
	return render(request,'Nandi/tractors/Massey/241-DI.html',{})

def MF_245_DI(request):
	return render(request,'Nandi/tractors/Massey/245-DI.html',{})

def MF_245_SMART(request):
	return render(request,'Nandi/tractors/Massey/245-Smart.html',{})

def MF_2635_4WD(request):
	return render(request,'Nandi/tractors/Massey/2635-4WD.html',{})

def MF_5245_DI_4WD(request):
	return render(request,'Nandi/tractors/Massey/5245-DI-4WD.html',{})

def MF_5245_DI_MM(request):
	return render(request,'Nandi/tractors/Massey/5245-DI-Maha-Mahaan.html',{})

def MF_5245_DI_MM(request):
	return render(request,'Nandi/tractors/Massey/5245-DI-Maha-Mahaan.html',{})

def MF_5245_DI_PP(request):
	return render(request,'Nandi/tractors/Massey/5245-DI-Planetary-Plus.html',{})

def MF_6028(request):
	return render(request,'Nandi/tractors/Massey/6028.html',{})

def MF_7250_DI_PU(request):
	return render(request,'Nandi/tractors/Massey/7250-DI-Power-UP.html',{})

def MF_7250_DI(request):
	return render(request,'Nandi/tractors/Massey/7250-DI.html',{})

def MF_9000_PP(request):
	return render(request,'Nandi/tractors/Massey/9000-Planetary-Plus.html',{})

def MF_9500_SMART(request):
	return render(request,'Nandi/tractors/Massey/9500-Smart.html',{})

def MF_9500_SSS(request):
	return render(request,'Nandi/tractors/Massey/9500-Super-Shuttle-Series.html',{})

def MF_9500(request):
	return render(request,'Nandi/tractors/Massey/9500.html',{})


#Sonalika Tractors
def SN_BBN_DI_30(request):
	return render(request, 'Nandi/tractors/Sonalika/Sonalika-Baagban-DI-30.html',{})

def SN_BBN_SUPER_DI_30(request):
	return render(request, 'Nandi/tractors/Sonalika/Sonalika-Baagban-Super-DI-30.html',{})

def SN_DI_35_SKD(request):
	return render(request, 'Nandi/tractors/Sonalika/Sonalika-DI-35-Sikander.html',{})

def SN_DI_35(request):
	return render(request, 'Nandi/tractors/Sonalika/Sonalika-DI-35.html',{})

def SN_DI_42_CHTPI(request):
	return render(request, 'Nandi/tractors/Sonalika/Sonalika-DI-42-Chatrapathi.html',{})

def SN_DI_42_HDM(request):
	return render(request, 'Nandi/tractors/Sonalika/Sonalika-DI-42-HDM.html',{})

def SN_DI_42_Rx(request):
	return render(request, 'Nandi/tractors/Sonalika/Sonalika-DI-42-Rx.html',{})

def SN_DI_42_SKD(request):
	return render(request, 'Nandi/tractors/Sonalika/Sonalika-DI-42-Sikander.html',{})

def SN_DI_47_Rx(request):
	return render(request, 'Nandi/tractors/Sonalika/Sonalika-DI-47-Rx.html',{})

def SN_DI_50_SKD(request):
	return render(request, 'Nandi/tractors/Sonalika/Sonalika-DI-50-Sikander.html',{})

def SN_DI_52_Rx_TS(request):
	return render(request, 'Nandi/tractors/Sonalika/Sonalika-DI-52-RX-Tiger-Series.html',{})

def SN_DI_60_MM_SUPER(request):
	return render(request, 'Nandi/tractors/Sonalika/Sonalika-DI-60-MM-Super.html',{})

def SN_DI_60_Rx_MM_SUPER(request):
	return render(request, 'Nandi/tractors/Sonalika/Sonalika-DI-60-Rx-MM-Super.html',{})

def SN_DI_60_SKD(request):
	return render(request, 'Nandi/tractors/Sonalika/Sonalika-DI-60-Sikander.html',{})

def SN_DI_60(request):
	return render(request, 'Nandi/tractors/Sonalika/Sonalika-DI-60.html',{})

def SN_DI_730_II_HDM(request):
	return render(request, 'Nandi/tractors/Sonalika/Sonalika-DI-730-II-HDM.html',{})

def SN_DI_734(request):
	return render(request, 'Nandi/tractors/Sonalika/Sonalika-DI-734.html',{})

def SN_DI_740_III(request):
	return render(request, 'Nandi/tractors/Sonalika/Sonalika-DI-740-III.html',{})

def SN_DI_745_III_CHTPI(request):
	return render(request, 'Nandi/tractors/Sonalika/Sonalika-DI-745-III-Chhatrapati.html',{})

def SN_DI_745_III_SKD(request):
	return render(request, 'Nandi/tractors/Sonalika/Sonalika-DI-745-III-Sikander.html',{})

def SN_DI_750_III_SKD(request):
	return render(request, 'Nandi/tractors/Sonalika/Sonalika-DI-750-III-Sikander.html',{})

def SN_DI_750_III(request):
	return render(request, 'Nandi/tractors/Sonalika/Sonalika-DI-750-III.html',{})

def SN_GT_20(request):
	return render(request, 'Nandi/tractors/Sonalika/Sonalika-GT-20.html',{})

def SN_GT_22(request):
	return render(request, 'Nandi/tractors/Sonalika/Sonalika-GT-22.html',{})

def SN_GT_26(request):
	return render(request, 'Nandi/tractors/Sonalika/Sonalika-GT-26.html',{})

def SN_GT_28(request):
	return render(request, 'Nandi/tractors/Sonalika/Sonalika-GT-28.html',{})

def SN_MM_35_DI(request):
	return render(request, 'Nandi/tractors/Sonalika/Sonalika-MM-35-DI.html',{})

def SN_MM_39_DI(request):
	return render(request, 'Nandi/tractors/Sonalika/Sonalika-MM-39-DI.html',{})

def SN_MM_41_DI(request):
	return render(request, 'Nandi/tractors/Sonalika/Sonalika-MM-41-DI.html',{})

def SN_MM_45_DI(request):
	return render(request, 'Nandi/tractors/Sonalika/Sonalika-MM-45.html',{})

def SN_MM_50_DI(request):
	return render(request, 'Nandi/tractors/Sonalika/Sonalika-MM-50-DI.html',{})

def SN_Rx_35_SKD(request):
	return render(request, 'Nandi/tractors/Sonalika/Sonalika-Rx-35-Sikander.html',{})

def SN_Rx_35(request):
	return render(request, 'Nandi/tractors/Sonalika/Sonalika-Rx-35.html',{})

def SN_Rx_42_SKD(request):
	return render(request, 'Nandi/tractors/Sonalika/Sonalika-Rx-42-Sikander.html',{})

def SN_Rx_47_SKD(request):
	return render(request, 'Nandi/tractors/Sonalika/Sonalika-Rx-47-Sikander.html',{})

def SN_Rx_50_SKD(request):
	return render(request, 'Nandi/tractors/Sonalika/Sonalika-Rx-50-Sikander.html',{})

def SN_Rx_50(request):
	return render(request, 'Nandi/tractors/Sonalika/Sonalika-Rx-50.html',{})

def SN_Rx_55_SKD(request):
	return render(request, 'Nandi/tractors/Sonalika/Sonalika-Rx-55-Sikander.html',{})

def SN_Rx_60_SKD(request):
	return render(request, 'Nandi/tractors/Sonalika/Sonalika-Rx-60-Sikander.html',{})

def SN_Rx_60(request):
	return render(request, 'Nandi/tractors/Sonalika/Sonalika-Rx-60.html',{})

def SN_Rx_745_III_SKD(request):
	return render(request, 'Nandi/tractors/Sonalika/Sonalika-Rx-745-III-Sikander.html',{})

def SN_Rx_745_III(request):
	return render(request, 'Nandi/tractors/Sonalika/Sonalika-Rx-745-III.html',{})

def SN_Rx_750_III_SKD(request):
	return render(request, 'Nandi/tractors/Sonalika/Sonalika-Rx-750-III-Sikander.html',{})

def SN_WT_60_Rx_SKD(request):
	return render(request, 'Nandi/tractors/Sonalika/Sonalika-Worldtrac-60-Rx-Sikander.html',{})

def SN_WT_60(request):
	return render(request, 'Nandi/tractors/Sonalika/Sonalika-Worldtrac-60.html',{})

def SN_WT_75(request):
	return render(request, 'Nandi/tractors/Sonalika/Sonalika-Worldtrac-75.html',{})

def SN_WT_90(request):
	return render(request, 'Nandi/tractors/Sonalika/Sonalika-Worldtrac-90.html',{})






#John Deere Tractors
def JD_3028EN(request):
	return render(request,'Nandi/tractors/JD/3028EN.html',{})

def JD_3036E(request):
	return render(request,'Nandi/tractors/JD/3036E.html',{})

def JD_3036EN(request):
	return render(request,'Nandi/tractors/JD/3036EN.html',{})

def JD_5005(request):
	return render(request,'Nandi/tractors/JD/5005.html',{})

def JD_5036C(request):
	return render(request,'Nandi/tractors/JD/5036C.html',{})

def JD_5036D(request):
	return render(request,'Nandi/tractors/JD/5036D.html',{})

def JD_5038D(request):
	return render(request,'Nandi/tractors/JD/5038D.html',{})

def JD_5039C(request):
	return render(request,'Nandi/tractors/JD/5039C.html',{})

def JD_5039D_PP(request):
	return render(request,'Nandi/tractors/JD/5039D-PowerPro.html',{})

def JD_5039D(request):
	return render(request,'Nandi/tractors/JD/5039D.html',{})

def JD_5042C(request):
	return render(request,'Nandi/tractors/JD/5042C.html',{})

def JD_5042D_PP(request):
	return render(request,'Nandi/tractors/JD/5042D-PowerPro.html',{})

def JD_5042D(request):
	return render(request,'Nandi/tractors/JD/5042D.html',{})

def JD_5045D_PP(request):
	return render(request,'Nandi/tractors/JD/5045D-PowerPro.html',{})

def JD_5045D(request):
	return render(request,'Nandi/tractors/JD/5045D.html',{})

def JD_5045D(request):
	return render(request,'Nandi/tractors/JD/5045D.html',{})

def JD_5050D(request):
	return render(request,'Nandi/tractors/JD/5050D.html',{})

def JD_5050E(request):
	return render(request,'Nandi/tractors/JD/5050E.html',{})

def JD_5055E(request):
	return render(request,'Nandi/tractors/JD/5055E.html',{})

def JD_5060E(request):
	return render(request,'Nandi/tractors/JD/5060E.html',{})

def JD_5065E(request):
	return render(request,'Nandi/tractors/JD/5065E.html',{})

def JD_5075E(request):
	return render(request,'Nandi/tractors/JD/5075E.html',{})

def JD_5105(request):
	return render(request,'Nandi/tractors/JD/5105.html',{})

def JD_5205(request):
	return render(request,'Nandi/tractors/JD/5205.html',{})

def JD_5210_GP(request):
	return render(request,'Nandi/tractors/JD/5210-GearPro.html',{})

def JD_5210(request):
	return render(request,'Nandi/tractors/JD/5210.html',{})

def JD_5305D(request):
	return render(request,'Nandi/tractors/JD/5305D.html',{})

def JD_5310(request):
	return render(request,'Nandi/tractors/JD/5310.html',{})

def JD_5405_GP(request):
	return render(request,'Nandi/tractors/JD/5405-GearPro.html',{})

def JD_6110B(request):
	return render(request,'Nandi/tractors/JD/6110B.html',{})

def JD_6120B(request):
	return render(request,'Nandi/tractors/JD/6120B.html',{})



#Force Tractors
def F_ABHIMAN_MINI(request):
	return render(request,'Nandi/tractors/Force/Abhiman-Mini.html',{})

def F_ABHIMAN(request):
	return render(request,'Nandi/tractors/Force/Abhiman.html',{})

def F_BALWAN_400(request):
	return render(request,'Nandi/tractors/Force/Balwan-400.html',{})

def F_BALWAN_550(request):
	return render(request,'Nandi/tractors/Force/Balwan-550.html',{})

def F_ORC_DLX_LT(request):
	return render(request,'Nandi/tractors/Force/Orchard-DLX-LT.html',{})

def F_ORC_DLX(request):
	return render(request,'Nandi/tractors/Force/Orchard-DLX.html',{})

def F_ORC_MINI(request):
	return render(request,'Nandi/tractors/Force/Orchard-Mini.html',{})

def F_SANMAN_5000(request):
	return render(request,'Nandi/tractors/Force/Sanman-5000.html',{})

def F_SANMAN_6000(request):
	return render(request,'Nandi/tractors/Force/Sanman-6000.html',{})

#Implements

#Fert-Spreaders 
def FS_MG_500(request):
	return render(request,'Nandi/implements/fert-spreaders/mg-furbo-500.html',{})

def FS_MH(request):
	return render(request,'Nandi/implements/fert-spreaders/mahindra-fert-spreader.html',{})

def FS_LF(request):
	return render(request,'Nandi/implements/fert-spreaders/landforce-fert-spreader.html',{})

def FS_KD(request):
	return render(request,'Nandi/implements/fert-spreaders/khedut-fert-spreader.html',{})

def FS_FK(request):
	return render(request,'Nandi/implements/fert-spreaders/fieldking-fert-spreader.html',{})

#Trailers
def TLS_KD(request):
    return render(request,'Nandi/implements/trailers/khedut-trailer.html',{})

def TLS_FK(request):
    return render(request,'Nandi/implements/trailers/fieldking-trailer.html',{})

def TLS_LF(request):
    return render(request,'Nandi/implements/trailers/landforce-trailer.html',{})

def TLS_SM(request):
    return render(request,'Nandi/implements/trailers/soil-master-trailer.html',{})	

#Balers
def BLR_MG_165(request):
	return render(request,'Nandi/implements/balers/mg-round-165.html',{})	

def BLR_MG_180(request):
	return render(request,'Nandi/implements/balers/mg-round-180.html',{})	

def BLR_MG_SQB(request):
	return render(request,'Nandi/implements/balers/mg-square-baler.html',{})	

def BLR_MG_TT_125(request):
	return render(request,'Nandi/implements/balers/mg-trotter-125.html',{})	

def BLR_CLS(request):
	return render(request,'Nandi/implements/balers/claas-markant.html',{})	

def BLR_DSM_631(request):
	return render(request,'Nandi/implements/balers/dasmesh-631.html',{})

def BLR_FK_RB(request):
	return render(request,'Nandi/implements/balers/fieldking-round-baler.html',{})

def BLR_FK_SB(request):
	return render(request,'Nandi/implements/balers/fieldking-square.html',{})

def BLR_JD_CR(request):
	return render(request,'Nandi/implements/balers/jd-compact-round.html',{})

def BLR_MH_B(request):
	return render(request,'Nandi/implements/balers/mahindra-baler.html',{})	

def BLR_MH_SQ(request):
	return render(request,'Nandi/implements/balers/mahindra-square.html',{})	

def BLR_NH_SQ(request):
	return render(request,'Nandi/implements/balers/new-holland-square.html',{})	

def BLR_NH_SRB(request):
	return render(request,'Nandi/implements/balers/nh-small-round-baler.html',{})	

def BLR_SK_SQB(request):
	return render(request,'Nandi/implements/balers/shaktiman-square-baler.html',{})

def BLR_SK_SRB_60(request):
	return render(request,'Nandi/implements/balers/shaktiman-srb-60.html',{})


#Seeders
def SDR_DSM_610  (request):
	return render(request,'Nandi/implements/seeders/dasmesh-610-happy-seeder.html',{})

def SDR_FK_HS   (request):
	return render(request,'Nandi/implements/seeders/fk-happy-seeder.html',{})

def SDR_FK_SD  (request):
	return render(request,'Nandi/implements/seeders/fk-roto-seed-drill.html',{})	

def SDR_KD_DS  (request):
	return render(request,'Nandi/implements/seeders/khedut-drum-seeder.html',{})

def SDR_KD_SCF  (request):
	return render(request,'Nandi/implements/seeders/khedut-scf-drill.html',{})

def SDR_LF_HS  (request):
	return render(request,'Nandi/implements/seeders/lf-happy-seeder.html',{})

def SDR_LF_RSD_HD   (request):
	return render(request,'Nandi/implements/seeders/lf-roto-seed-drill-hduty.html',{})

def SDR_LF_RSD_SD  (request):
	return render(request,'Nandi/implements/seeders/lf-roto-seed-drill-std.html',{})

def SDR_LF_TS  (request):
	return render(request,'Nandi/implements/seeders/lf-turbo-seeder.html',{})

def SDR_MG_SS_205  (request):
	return render(request,'Nandi/implements/seeders/mg-superseeder-205.html',{})

def SDR_MG_SS_230  (request):
	return render(request,'Nandi/implements/seeders/mg-superseeder-230.html',{})

def SDR_NH_HS  (request):
	return render(request,'Nandi/implements/seeders/nh-happy-seeder.html',{})

def SDR_SON_RSD  (request):
	return render(request,'Nandi/implements/seeders/sonalika-roto-seed-drill.html',{})


#Harrows
def HRR_AG_615 (request):
	return render(request,'Nandi/implements/harrows/ag-power-615.html',{}) 

def HRR_FK_COM_MD (request):
	return render(request,'Nandi/implements/harrows/fk-compact-md.html',{})

def HRR_FK_DB (request):
	return render(request,'Nandi/implements/harrows/fk-dabangg.html',{})

def HRR_FK_EXTRA_HD (request):
	return render(request,'Nandi/implements/harrows/fk-extra-hd-hyra.html',{})

def HRR_FK_HD_HYDRA (request):
	return render(request,'Nandi/implements/harrows/fk-hd-hydra.html',{})

def HRR_FK_HS_DISC (request):
	return render(request,'Nandi/implements/harrows/fk-hs-disc.html',{})

def HRR_FK_MN_OD (request):
	return render(request,'Nandi/implements/harrows/fk-mounted-offset-disc.html',{})

def HRR_FK_MN_OD2 (request):
	return render(request,'Nandi/implements/harrows/fk-mounted-offset-disc2.html',{})

def HRR_FK_POWER (request):
	return render(request,'Nandi/implements/harrows/fk-power.html',{})

def HRR_FK_RPD (request):
	return render(request,'Nandi/implements/harrows/fk-robust-poly-disc.html',{})

def HRR_FK_TD_HD (request):
	return render(request,'Nandi/implements/harrows/fk-tandem-disc-hd.html',{})

def HRR_FK_TD_LS (request):
	return render(request,'Nandi/implements/harrows/fk-tandem-disc-ls.html',{})

def HRR_FK_TD_MD (request):
	return render(request,'Nandi/implements/harrows/fk-tandem-disc-med-duty.html',{})

def HRR_FK_TD_MS_USA (request):
	return render(request,'Nandi/implements/harrows/fk-tandem-disc-ms-usa.html',{})

def HRR_FK_TO (request):
	return render(request,'Nandi/implements/harrows/fk-trailed-offset.html',{})

def HRR_FK_UHH (request):
	return render(request,'Nandi/implements/harrows/fk-ultra-hd-hydra.html',{})

def HRR_FK_UD (request):
	return render(request,'Nandi/implements/harrows/fk-up-disc.html',{})

def HRR_KD_HH (request):
	return render(request,'Nandi/implements/harrows/kd-hydra-hdd.html',{})

def HRR_KD_MOD (request):
	return render(request,'Nandi/implements/harrows/kd-mounted-osct-disc.html',{})

def HRR_MD (request):
	return render(request,'Nandi/implements/harrows/mahindra-disc.html',{})

def HRR_SK_E120 (request):
	return render(request,'Nandi/implements/harrows/sk-power-e120.html',{})

def HRR_SK_M160 (request):
	return render(request,'Nandi/implements/harrows/sk-power-m160.html',{})

def HRR_SK_P (request):
	return render(request,'Nandi/implements/harrows/sk-power.html',{})

def HRR_SM_D (request):
	return render(request,'Nandi/implements/harrows/sm-disc.html',{})




#Ploughs
def PLG_AG_DISC (request):
	return render(request,'Nandi/implements/ploughs/agristar-disc-2-furrow.html',{})

def PLG_AG_MB (request):
	return render(request,'Nandi/implements/ploughs/agristar-mould-board.html',{})

def PLG_C_MB (request):
	return render(request,'Nandi/implements/ploughs/captain-mb.html',{})

def PLG_C_REV (request):
	return render(request,'Nandi/implements/ploughs/captain-rev.html',{})

def PLG_DSM_451_MB (request):
	return render(request,'Nandi/implements/ploughs/dasmesh-451mb.html',{})

def PLG_FK_MAXX (request):
	return render(request,'Nandi/implements/ploughs/fk-maxx-mb.html',{})

def PLG_FK_POLY (request):
	return render(request,'Nandi/implements/ploughs/fk-poly-disc.html',{})

def PLG_FK_REV_MAN (request):
	return render(request,'Nandi/implements/ploughs/fk-rev-manual.html',{})

def PLG_JD_CHISEL (request):
	return render(request,'Nandi/implements/ploughs/jd-chisel.html',{})

def PLG_JD_HYDRA (request):
	return render(request,'Nandi/implements/ploughs/jd-hydra-rev.html',{})

def PLG_KD_RMP (request):
	return render(request,'Nandi/implements/ploughs/kd-rmp.html',{})

def PLG_KD_MD (request):
	return render(request,'Nandi/implements/ploughs/khedut-mounted-disc.html',{})

def PLG_LMK_1MB (request):
	return render(request,'Nandi/implements/ploughs/lemken-opal-1mb.html',{})

def PLG_LMK_2MB (request):
	return render(request,'Nandi/implements/ploughs/lemken-opal-2mb.html',{})

def PLG_LF_MB_REV (request):
	return render(request,'Nandi/implements/ploughs/lf-mb-rev.html',{})

def PLG_MH_REV (request):
	return render(request,'Nandi/implements/ploughs/mahindra-rev.html',{})

def PLG_MG_SUMO_2MB (request):
	return render(request,'Nandi/implements/ploughs/mg-sumo-2mb.html',{})

def PLG_MG_SUMO_3MB (request):
	return render(request,'Nandi/implements/ploughs/mg-sumo-3mb.html',{})

def PLG_NH_REV (request):
	return render(request,'Nandi/implements/ploughs/nh-rev-hydra.html',{})

def PLG_SM_MB (request):
	return render(request,'Nandi/implements/ploughs/sm-mb-3row.html',{})

def PLG_SON_MB(request):
	return render(request,'Nandi/implements/ploughs/sonalika-mb.html',{})

def PLG_SON_REV (request):
	return render(request,'Nandi/implements/ploughs/sonalika-rev.html',{})



