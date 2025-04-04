from django.contrib import admin
from .models import AuditLog, SystemSetting, EmployeeProfile

@admin.register(AuditLog)
class AuditLogAdmin(admin.ModelAdmin):
    list_display = ('user', 'action', 'model', 'timestamp')
    list_filter = ('action', 'model')
    search_fields = ('user__username', 'details')

@admin.register(SystemSetting)
class SystemSettingAdmin(admin.ModelAdmin):
    list_display = ('key', 'last_updated')
    search_fields = ('key', 'description')

@admin.register(EmployeeProfile)
class EmployeeProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'department', 'position', 'hire_date')
    search_fields = ('user__username', 'department', 'position')