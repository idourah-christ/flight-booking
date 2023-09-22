from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

# Create your models here.

class UserAccountManager(BaseUserManager):

    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("User must have a email")
 
        if not password:
            raise ValueError("User must have a password")

        email = self.normalize_email(email)
        user = self.model(email=email,**extra_fields)
        
        user.set_password(password)
        user.save()

        return user 

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_superuser',True)
        extra_fields.setdefault('is_active', True)
        
        email = self.normalize_email(email)
        user = self.model(email=email,**extra_fields)
        
        user.set_password(password)
        user.save()

        return user 
        
class UserAccount(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)
    phone = models.CharField(max_length=9, unique=True)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    first_name = models.CharField(max_length=255, null=True, blank=True)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_manager = models.BooleanField(default=False)
    code = models.CharField(unique=True, null=True, blank=True, max_length=6)

    # object manager
    objects = UserAccountManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ["phone"]

    def get_full_name(self):
        return self.last_name + " " + self.first_name

    def get_short_name(self):
        return self.email

    def __str__(self):
        return self.email 