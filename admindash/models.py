from django.db import models
from oauth.models import User
from django.utils import timezone

class AuditLog(models.Model):
    ACTION_CHOICES = (
        ('CREATE', 'Create'),
        ('UPDATE', 'Update'),
        ('DELETE', 'Delete'),
        ('LOGIN', 'Login'),
        ('LOGOUT', 'Logout'),
    )

    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    action = models.CharField(max_length=10, choices=ACTION_CHOICES)
    model = models.CharField(max_length=50)
    object_id = models.CharField(max_length=50, null=True, blank=True)
    details = models.TextField()
    timestamp = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        return f"{self.user.username} - {self.action} - {self.model}"

class SystemSetting(models.Model):
    key = models.CharField(max_length=100, unique=True)
    value = models.TextField()
    description = models.TextField(blank=True)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.key

class EmployeeProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    department = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    hire_date = models.DateField()
    phone = models.CharField(max_length=20, blank=True)
    address = models.TextField(blank=True)
    emergency_contact = models.TextField(blank=True)

    def __str__(self):
        return f"{self.user.full_name} - {self.position}"

# from django.db import models
# from oauth.models import User
# from django.utils import timezone
# from django.core.exceptions import ValidationError

# class AuditLog(models.Model):
#     ACTION_CHOICES = (
#         ('CREATE', 'Create'),
#         ('UPDATE', 'Update'),
#         ('DELETE', 'Delete'),
#         ('LOGIN', 'Login'),
#         ('LOGOUT', 'Logout'),
#         ('ACCESS', 'Access'),
#     )

#     user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='audit_logs')
#     action = models.CharField(max_length=10, choices=ACTION_CHOICES)
#     model = models.CharField(max_length=50)
#     object_id = models.CharField(max_length=50, null=True, blank=True)
#     details = models.JSONField(default=dict)
#     ip_address = models.GenericIPAddressField(null=True, blank=True)
#     timestamp = models.DateTimeField(default=timezone.now)

#     class Meta:
#         ordering = ['-timestamp']
#         indexes = [
#             models.Index(fields=['-timestamp']),
#             models.Index(fields=['user']),
#             models.Index(fields=['action']),
#         ]

#     def __str__(self):
#         return f"{self.get_action_display()} on {self.model} by {self.user}"

#     def save(self, *args, **kwargs):
#         if not self.details:
#             self.details = {}
#         super().save(*args, **kwargs)

# class SystemSetting(models.Model):
#     key = models.CharField(max_length=100, unique=True)
#     value = models.JSONField()
#     description = models.TextField(blank=True)
#     is_public = models.BooleanField(default=False)
#     last_updated = models.DateTimeField(auto_now=True)
#     updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

#     class Meta:
#         verbose_name = "System Setting"
#         verbose_name_plural = "System Settings"

#     def __str__(self):
#         return self.key

#     def clean(self):
#         try:
#             # Validate JSON value
#             if not isinstance(self.value, (dict, list, str, int, float, bool)) and self.value is not None:
#                 raise ValidationError("Value must be valid JSON serializable data")
#         except ValueError:
#             raise ValidationError("Invalid JSON data")

# class EmployeeProfile(models.Model):
#     DEPARTMENT_CHOICES = (
#         ('CONTENT', 'Content'),
#         ('MARKETING', 'Marketing'),
#         ('DEVELOPMENT', 'Development'),
#         ('HR', 'Human Resources'),
#         ('ADMIN', 'Administration'),
#     )

#     user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='employee_profile')
#     department = models.CharField(max_length=20, choices=DEPARTMENT_CHOICES)
#     position = models.CharField(max_length=100)
#     hire_date = models.DateField()
#     phone = models.CharField(max_length=20, blank=True)
#     address = models.TextField(blank=True)
#     emergency_contact = models.JSONField(default=dict)
#     skills = models.JSONField(default=list)
#     is_remote = models.BooleanField(default=False)
#     last_evaluation = models.DateField(null=True, blank=True)
#     notes = models.TextField(blank=True)

#     class Meta:
#         verbose_name = "Employee Profile"
#         verbose_name_plural = "Employee Profiles"

#     def __str__(self):
#         return f"{self.user.get_full_name()} - {self.get_department_display()}"

#     @property
#     def employment_duration(self):
#         if self.hire_date:
#             delta = timezone.now().date() - self.hire_date
#             return f"{delta.days // 365} years, {(delta.days % 365) // 30} months"
#         return "N/A"
