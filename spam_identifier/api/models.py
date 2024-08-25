from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Custom UserManager
class UserManager(BaseUserManager):
    def create_user(self, phone_number, name, password=None, email=None):
        if not phone_number:
            raise ValueError('Users must have a phone number')

        user = self.model(
            phone_number=phone_number,
            name=name,
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone_number, name, password=None, email=None):
        user = self.create_user(
            phone_number=phone_number,
            password=password,
            name=name,
            email=email
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

# Custom User Model
class User(AbstractBaseUser):
    phone_number = models.CharField(max_length=15, unique=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=255, null=True, blank=True)
    contacts = models.ManyToManyField('Contact', blank=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['name']

    def __str__(self):
        return self.name

class Contact(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    marked_as_spam = models.BooleanField(default=False)
    spam_reports = models.IntegerField(default=0)

    def mark_as_spam(self):
        self.marked_as_spam = True
        self.spam_reports += 1
        self.save()

    def __str__(self):
        return self.name
