from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()

    def __str__(self):
        return f"{self.title} by {self.author} in {self.publication_year}"

    class Meta:
        permissions = [
            ("can_create", "can create books"),
            ("can_view", "can view books"),
            ("can_edit", "can edit books"),
            ("can_delete", "can delete books"),
        ]
        constraints = [
            models.UniqueConstraint(fields=['title', 'author'], name='unique_book_per_author'),
        ]

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, profile_picture=None, **other_fields):
        if not email or password is None:
            raise ValueError("Email and password should be provided")

        normal_email = self.normalize_email(email)
        user = self.model(email=normal_email, **other_fields)
        if profile_picture:
            user.profile_photo = profile_picture
        user.set_password(password)
        user.save(using=self._db)

    def create_superuser(self, email, password=None, profile_picture=None, **other_fields):
        other_fields.setdefault("is_staff", True)
        other_fields.setdefault("is_superuser", True)

        return self.create_user(email, password, profile_picture, **other_fields)

class CustomUser(AbstractUser):
    email = models.EmailField(max_length=255, unique=True)
    date_of_birth = models.DateField(null=True, blank=True)
    profile_photo = models.ImageField(upload_to="profile_pictures/", null=True, blank=True)

    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        return f"{self.username}"