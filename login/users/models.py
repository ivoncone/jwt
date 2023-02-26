from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractUser


class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise TypeError("Enter a valid email address.")
        if not password:
            raise TypeError("Enter a valid password.")

        user = self.model(
            email=self.normalize_email(email),
        )
        user.set_password(password)
        user.is_active=True
        user.save()
        return user



class User(AbstractUser):
	username = None
	email = models.EmailField(max_length=50, unique=True)
	password = models.CharField(max_length=200)
	is_active = models.BooleanField(default=False)
	is_superuser = models.BooleanField(default=False)
	is_verified = models.BooleanField(default=False)


	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)


	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = []


	class Meta:
		db_table = 'usersapp'

		ordering = ["-updated_at"]
		
	def __str__(self):

		return self.email




