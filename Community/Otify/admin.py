from django.contrib import admin
from .models import ComplainCategory, Complaint, User, Region

# Register your models here.
admin.site.register(ComplainCategory)

admin.site.register(Complaint)

admin.site.register(User)

admin.site.register(Region)

