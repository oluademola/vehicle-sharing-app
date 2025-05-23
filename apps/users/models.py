"""
This module contains User model configurations.
"""

from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import PermissionsMixin, AbstractBaseUser
from apps.common import choices
from apps.common.base_model import BaseModel
from apps.users.managers import CustomUserManager


class CustomUser(BaseModel, PermissionsMixin, AbstractBaseUser):
    """
    User model class
    """
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True, max_length=100)
    gender = models.CharField(
        default="male", choices=choices.GENDER, max_length=10)
    phone_no = models.CharField(max_length=50, blank=True)
    document_type = models.CharField(
        max_length=100, choices=choices.DOCUMENT_TYPES)
    document = models.FileField(upload_to="documents/", help_text=_(
        "upload a legal document that truely identifies you for verification."),
        blank=True, null=True)
    profile_picture = models.ImageField(
        upload_to="profile picture/", default="images/dummy.png")

    personal_description = models.TextField(
        max_length=500, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = CustomUserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    class Meta:
        """
        metadata options
        """
        verbose_name = "User"
        verbose_name_plural = "Users"

    def get_full_name(self):
        """
        Captilization of full name.
        """
        return f"{self.first_name.capitalize()} {self.last_name.capitalize()}"

    def __str__(self):
        return f"{self.email}"

    def get_absolute_url(self):
        """
        returns user detail
        """
        return reverse("user_detail", kwargs={"id": self.id})
