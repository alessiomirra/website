from django.contrib import admin
from .models import Car, CompanyInfo 
# Register your models here.

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ["make","model","created_at"]


admin.site.register(CompanyInfo)