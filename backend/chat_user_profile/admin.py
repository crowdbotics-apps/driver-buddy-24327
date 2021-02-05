from django.contrib import admin
from .models import VerificationCode, Profile, Contact

admin.site.register(Contact)
admin.site.register(Profile)
admin.site.register(VerificationCode)

# Register your models here.
