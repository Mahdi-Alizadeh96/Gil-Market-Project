from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


# second write this code (create model user manager)
class UserManager(BaseUserManager):
    def create_user(self, phone, first_name, last_name, email, address, password):
        if not phone:
            raise ValueError('please enter your Phone number')
        if not first_name:
            raise ValueError('please enter your first name')
        if not last_name:
            raise ValueError('please enter your last name')
        user = self.model(phone=phone, first_name=first_name, last_name=last_name, email=self.normalize_email(email),
                          address=address)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone, first_name, last_name, email, password):
        user = self.create_user(phone=phone, first_name=first_name, last_name=last_name, email=email, address=None,
                                password=password)
        user.is_admin = True
        user.save(using=self._db)
        return user

    
# first write this code (create model user)
class User(AbstractBaseUser):
    first_name = models.CharField(max_length=50, verbose_name='نام')
    last_name = models.CharField(max_length=50, verbose_name='نام خانوادگی')
    email = models.EmailField(null=True, blank=True, verbose_name='ایمیل')
    phone = models.CharField(max_length=15, unique=True, verbose_name='شماره تلفن')
    address = models.CharField(max_length=350, null=True, blank=True, verbose_name='آدرس')
    is_active = models.BooleanField(default=True, verbose_name='فعال / غیر فعال')
    is_admin = models.BooleanField(default=False, verbose_name='ادمین بودن / نبودن')
    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'email']  # another field ask you in createsuperuser
    objects = UserManager()

    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربران'

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"
