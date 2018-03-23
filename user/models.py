import typing
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from .address.models import Address


class UserManager(BaseUserManager):
    def create_user(self, wxopenid: str):
        return self.model.objects.get_or_create(wxopenid=wxopenid)[0]

    def create_superuser(self, wxopenid: str, password: str):
        user = self.create_user(wxopenid)
        user.set_password(password)
        user.is_staff = True
        user.is_admin = True
        user.save()
        return user


class User(AbstractBaseUser):
    invite_codes = models.ManyToManyField("invite_code.InviteCode", blank=True)
    default_address = models.ForeignKey(Address, null=True, blank=True, related_name="user", on_delete=models.CASCADE)
    address = models.ManyToManyField(Address, blank=True, related_name="users")
    mobile = models.CharField(max_length=11, unique=True, null=True, blank=True)
    nick = models.CharField(max_length=32, null=True, blank=True)
    wxopenid = models.CharField(max_length=64, unique=True, null=True, blank=True)
    is_staff = models.BooleanField(default=False)
    USERNAME_FIELD = 'wxopenid'
    objects = UserManager()

    def get_full_name(self) -> str:
        return self.nick or self.wxopenid

    def get_short_name(self) -> str:
        return self.get_full_name()

    def has_perm(self, perm, obj=None) -> bool:
        return True

    def has_module_perms(self, app_label) -> bool:
        return True

    def __str__(self):
        return self.get_full_name()
