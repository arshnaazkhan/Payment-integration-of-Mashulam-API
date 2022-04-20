from django.contrib import admin
from .models import payment
# Register your models here.
class paymentAdmin(admin.ModelAdmin):
    list_display= ('userid', 'fullName', 'phone', 'email','sum','pageCode','processId','processToken')
    
admin.site.register(payment,paymentAdmin)