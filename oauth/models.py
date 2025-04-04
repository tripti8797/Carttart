from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.core.validators import RegexValidator

class UserManager(BaseUserManager):
    def create_user(self, email, full_name, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, full_name=full_name, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, full_name, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('role', 'SUPERADMIN')

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        
        return self.create_user(email, full_name, password, **extra_fields)
class User(AbstractBaseUser, PermissionsMixin):
    ROLE_CHOICES = (
        ('SUPERADMIN', 'Super Admin'),
        ('EMPLOYEE', 'Employee'),
    )
    
    username = models.CharField(max_length=10, unique=True, blank=True)
    email = models.EmailField(unique=True)
    full_name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='EMPLOYEE')
    
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='oauth_user_groups',  # Add a unique related_name
        blank=True,
        help_text=_('The groups this user belongs to.'),
        verbose_name=_('groups'),
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='oauth_user_permissions',  # Add a unique related_name
        blank=True,
        help_text=_('Specific permissions for this user.'),
        verbose_name=_('user permissions'),
    )
    
    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['full_name']

    def save(self, *args, **kwargs):
        if not self.username:
            if self.role == 'SUPERADMIN':
                last_super = User.objects.filter(role='SUPERADMIN').order_by('-id').first()
                new_id = f"SAD{int(last_super.username[3:]) + 1:05d}" if last_super else "SAD00001"
                self.username = new_id
            elif self.role == 'EMPLOYEE':
                last_emp = User.objects.filter(role='EMPLOYEE').order_by('-id').first()
                new_id = f"EMP{int(last_emp.username[3:]) + 1:05d}" if last_emp else "EMP00001"
                self.username = new_id
        super().save(*args, **kwargs)

    def __str__(self):
        return self.username

    @property
    def is_superadmin(self):
        return self.role == 'SUPERADMIN'

    @property
    def is_employee(self):
        return self.role == 'EMPLOYEE'