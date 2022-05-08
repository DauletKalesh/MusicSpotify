
from django.db import models
from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import gettext_lazy as _
from utils.constants import GENDER_LIST
from utils.validators import validate_image_format, validate_image_size
from utils.upload import *
# Create your models here.


class AuthUserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class AuthUser(AbstractBaseUser, PermissionsMixin):

    username = models.CharField(_('Username'), unique=True, max_length=50)
    email = models.EmailField(_('Email address'), unique=True)
    first_name = models.CharField(_('First name'), max_length=30, blank=True)
    last_name = models.CharField(_('Last name'), max_length=30, blank=True)
    date_joined = models.DateTimeField(_('Date joined'), auto_now_add=True)
    is_active = models.BooleanField(_('active'), default=True, blank=True)
    is_staff = models.BooleanField(_('is_staff'), default=False, blank=True)

    objects = AuthUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('Users')


class Profile(models.Model):
    user = models.OneToOneField(AuthUser, on_delete=models.CASCADE, related_name='UserProfile')
    first_name = models.CharField(_('first name'), max_length=50, null=True, blank=True)
    last_name = models.CharField(_('last name'), max_length=50, null=True, blank=True)
    birthday = models.DateField(null=True, blank=True)
    gender = models.BooleanField(choices=GENDER_LIST, default=None, null=True, blank=True)
    avatar = models.ImageField(
        upload_to=profile_image_upload,
        validators=(validate_image_size, validate_image_format),
        blank=True, null=True
    )
    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'
        unique_together = (('user', 'first_name', 'last_name'),)

    def __str__(self) -> str:
        return self.user.username