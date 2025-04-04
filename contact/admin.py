from django.contrib import admin
from .models import ContactMessage

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'submission_date')
    list_filter = ('submission_date',)
    search_fields = ('name', 'email', 'subject')
    date_hierarchy = 'submission_date'