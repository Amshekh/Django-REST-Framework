from django.contrib import admin
from api.models import Company, Employee

class Company_Admin(admin.ModelAdmin):
    list_display = ('company_name', 'company_type', 'company_location') # only these fields will be visible on dashboard, when superuser goes to companies section
    search_fields = ('company_name', 'company_type', 'company_location') # using these fields you can search in dashboard for a company

class Employee_Admin(admin.ModelAdmin):
    list_display = ('emp_name', 'emp_post', 'emp_ctc')
    search_fields = ('emp_name', 'emp_post', 'emp_ctc')

admin.site.register(Company, Company_Admin)
admin.site.register(Employee, Employee_Admin)