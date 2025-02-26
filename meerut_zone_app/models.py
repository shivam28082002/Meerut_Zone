from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.db import models

class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """

    def create_user(self, email, password=None, **extra_fields):
        """
        Create and save a user with the given email and password.
        """
        if not email:
            raise ValueError(_("The Email must be set"))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Superuser must have is_staff=True."))
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Superuser must have is_superuser=True."))
        return self.create_user(email, password, **extra_fields)


class User(AbstractUser):
    """
    User model with CustomUserManager object access
    """
    email = models.EmailField("email address", unique=True)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class UserProfile(models.Model):
    """
    User Profile model with more user details
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="user_profile")
    phone = models.CharField(max_length=255, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    GENDER_CHOICE = [
        ('', '----Select Gender----'),
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other')
    ]
    gender = models.CharField(choices=GENDER_CHOICE, blank=True, max_length=100)

    def __str__(self):
        return str(self.user.first_name + ' ' + self.user.last_name)


HOSPITAL_CHOICES = [
    ('Nursing homes', 'Nursing homes'),
    ('EYE hospitals', 'EYE hospitals'),
    ('Blood banks', 'Blood banks'),
    ('General Medical & Surgical Hospitals', 'General Medical & Surgical Hospitals'),
    ('Neurology', 'Neurology')
]

EDUCATION_CHOICES = [
    ('Govt-School', 'Govt-School'),
    ('CBSE Board School', 'CBSE Board School'),
    ('ICSE Board School', 'ICSE Board School'),
    ('College', 'College'),
    ('University', 'University'),

]

CAFES_CHOICES = [
    ('Chinese', 'Chinese'),
    ('North Indian', 'North Indian'),
    ('Food Franchise', 'Food Franchise'),
    ('Food Court', 'Food Court'),
    ('Family Restaurant', 'Family Restaurant')
]

BANKS_CHOICES = [
    ('ICIC', 'ICIC'),
    ('SBI', 'SBI'),
    ('HDFC', 'HDFC'),
    ('AXIS', 'AXIS'),
    ('BOB', 'BOB'),
    ('BOI', 'BOI'),
    ('ATM', 'ATM')
]

SHOPPING_CHOICES = [
    ('Malls', 'Malls'),
    ('Grocery', 'Grocery'),
    ('Outlets', 'Outlets'),
    ('PUMA', 'PUMA'),
    ('REDTAPE', 'REDTAPE')
]

PARK_CHOICES = [
    ('KIDS', 'KIDS'),
    ('CRICKET_GROUND', 'CRICKET GROUND'),
    ('Football_GROUND', 'Football GROUND')
]


class Hospital(models.Model):
    name = models.CharField(max_length=200)
    file = models.FileField(upload_to='files/')
    address = models.CharField(max_length=1000)
    category = models.CharField(choices=HOSPITAL_CHOICES, max_length=200)
    loction = models.URLField(max_length=200)

    def __str__(self):
        return self.name + ", " + self.category


class Education(models.Model):
    name = models.CharField(max_length=200)
    file = models.FileField(upload_to='files/')
    address = models.CharField(max_length=1000)
    category = models.CharField(choices=EDUCATION_CHOICES, max_length=200)
    loction = models.URLField(max_length=200)

    def __str__(self):
        return self.name + ", " + self.category




class Cafes(models.Model):
    name = models.CharField(max_length=200) 
    file = models.FileField(upload_to='files/')
    address = models.CharField(max_length=1000)
    category = models.CharField(choices=CAFES_CHOICES, max_length=200)
    loction = models.URLField(max_length=200)

    def __str__(self):
        return self.name + ", " + self.category




class Banks(models.Model):
    name = models.CharField(max_length=200)
    file = models.FileField(upload_to='files/')
    address = models.CharField(max_length=1000)
    category = models.CharField(choices=BANKS_CHOICES, max_length=200)
    loction = models.URLField(max_length=200)

    def __str__(self):
        return self.name + ", " + self.category



class Shopping(models.Model):
    name = models.CharField(max_length=200)
    file = models.FileField(upload_to='files/')
    address = models.CharField(max_length=1000)
    category = models.CharField(choices=SHOPPING_CHOICES, max_length=200)
    loction = models.URLField(max_length=200)

    def __str__(self):
        return self.name + ", " + self.category

class Park(models.Model):
    name = models.CharField(max_length=200)
    file = models.FileField(upload_to='files/')
    address = models.CharField(max_length=1000)
    category = models.CharField(choices=PARK_CHOICES, max_length=200)
    loction = models.URLField(max_length=200)

    def __str__(self):
        return self.name + ", " + self.category


class Messages(models.Model):
    name = models.CharField(max_length=200)
    subject = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField()


class Rating(models.Model):
    user = models.CharField(max_length=200)
    post = models.CharField(max_length=200)
    rating = models.IntegerField(default=0)
    comment = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.user}: {self.rating}"