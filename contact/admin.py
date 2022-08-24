from django.contrib import admin

from .models import Contact

@admin.register(Contact)
class ContactAmin(admin.ModelAdmin):
    list_display = ["email", "date"]
    