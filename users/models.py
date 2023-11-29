import uuid
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model

class CustomUser(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(unique=True)


    # Use email as the unique identifier for authentication
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    groups = models.ManyToManyField(
        Group,
        verbose_name='groups',
        blank=True,
        help_text=
            'The groups this user belongs to. A user will get all permissions '
            'granted to each of their groups.',
        related_name='customuser_set',  # Add a related_name
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name='user permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name='customuser_set',  # Add a related_name
    )

    def __str__(self):
        return self.email
    
User = get_user_model()


class Gender(models.TextChoices):
    MALE = "Male", _("Male")
    FEMALE = "Female", _("Female")
    OTHER = "Other", _("Other")


class Profile(models.Model):
    user = models.OneToOneField(User, related_name="profile", on_delete=models.CASCADE)
    gender = models.CharField(
        verbose_name=_("Gender"),
        choices=Gender.choices,
        default=Gender.OTHER,
        max_length=20,
    )
    country = models.CharField(
        max_length=180,
        default="United States of America",
    )
    state = models.CharField(
        max_length=180,
        default="Texas",
    )
    account_number = models.BigIntegerField(
        default=9118872201,
    )
    account_type = models.CharField(
        max_length=180,
        default="E Checking",
    )
    opening_date = models.CharField(
        max_length=180,
        default="4/6/2000",
    )
    opening_amount = models.FloatField(
        default=4800000.00,
    )
    present_amount = models.FloatField(
        default=97000000.00,
    )
    next_of_kin = models.CharField(
        default="Monika A. Hinks",
        max_length=200
    )
    maiden_name = models.CharField(
        default="Sylvester",
        max_length=200
    )
    pet_name = models.CharField(
        default="Jack",
        max_length=200
    )
    favorite_color = models.CharField(
        default="white",
        max_length=200
    )
    account_status = models.BooleanField(
        default=False
    )


    def __str__(self):
        return f"{self.user.username}'s profile"
