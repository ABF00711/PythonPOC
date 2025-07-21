from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.

class CustomUserManager(BaseUserManager):
    def create_user(self, username, password= None):
        user = self.model(username = username)
        user.set_password(password)
        user.save(using = self._db)
        return user
    
    def create_superuser(self, username, password):
        user = self.create_user(username = username, password = password)
        user.is_admin = True
        user.save(using = self._db)
        return user
    
class CustomUser(AbstractBaseUser):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=128)

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'username'

    def __str__(self):
        return self.username
    
    @property
    def is_staff(self):
        return self.is_admin