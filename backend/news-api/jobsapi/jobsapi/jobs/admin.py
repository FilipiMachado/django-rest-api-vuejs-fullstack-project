from django.contrib import admin

from .models import JobOffer

class JobOfferAdmin(admin.ModelAdmin):
    list_display = ["company_name", "job_title",]

admin.site.register(JobOffer, JobOfferAdmin)
