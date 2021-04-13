from django.contrib import admin
from myapp.models import signup_user
# Register your models here.




class signup_userAdmin (admin.ModelAdmin):
    list_display = ["id","name","contact_no","roll_no","subject" , "added_on"]

admin.site.register (signup_user,signup_userAdmin)