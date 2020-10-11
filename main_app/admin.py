from django.contrib import admin
from .models import EmployeeProfile,Customer,NonENESaleEntry,ENESaleEntry,UsedTractorVerification

admin.site.register(EmployeeProfile)
admin.site.register(Customer)
admin.site.register(NonENESaleEntry)
admin.site.register(ENESaleEntry)
admin.site.register(UsedTractorVerification)