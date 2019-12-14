from django.db import models
from django.core.validators import RegexValidator
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import AbstractUser
from datetime import datetime

# Create your models here.
GENDER = (
    ('male', 'Male'),
    ('female', 'Female'),
)
PAYMENTS = (
    ('cash', 'Cash'),
    ('cheque', 'Cheque'),
    ('card', 'Card'),
)
roles = (
    ('student', 'Student'),
    ('teacher', 'Teacher'),
    ('administrator', 'Administrator'),
    ('owner', 'Owner'),
    ('driver', 'Driver'),
    ('fee collector', 'Fee Collector'),

)
class PBSUser(AbstractUser):
   role = models.CharField(choices=roles, max_length=120)
   picture = models.ImageField(upload_to='profiles', blank=True, null=True,)

class Owner(models.Model):
    user = models.OneToOneField(PBSUser, on_delete=models.CASCADE, blank=True, null=True)
    first_name = models.CharField(max_length=55)
    last_name = models.CharField(max_length=55)
    address = models.CharField(max_length=120)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, )  # validators should be a list
    alternate_phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)
    document = models.CharField(max_length=30)
    document_no = models.CharField(max_length=12)
    document_upload = models.ImageField(upload_to="documents/", null=True, blank=True)
    blood_group = models.CharField(max_length=3, null=True)

    def __str__(self):
        return self.first_name

class Route(models.Model):
    route_no = models.CharField(max_length=3)
    origin = models.CharField(max_length=50)
    destination = models.CharField(max_length=50)

    def __str__(self):
        return f'Route No {self.route_no }: From {self.origin} to {self.destination}'

class School(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.name} "

class Student(models.Model):
    user = models.OneToOneField(PBSUser, on_delete=models.CASCADE, null=True, blank=True)
    first_name = models.CharField(max_length=55)
    last_name = models.CharField(max_length=55)
    id = models.AutoField(primary_key=True)
    school_name = models.ForeignKey(School, on_delete=models.CASCADE, default=1)
    class_name = models.CharField(max_length=100)
    section_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    fathers_name = models.CharField(max_length=100)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, )  # validators should be a list
    alternate_phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)
    address = models.CharField(max_length=120)
    image = models.ImageField(upload_to='documents', blank=True)
    route_no = models.ForeignKey(Route, on_delete=models.CASCADE, )
    blood_group = models.CharField(max_length=3, null=True)
    added = models.DateField(auto_now_add=True)
    fee_per_month = models.IntegerField(validators=[
            MinValueValidator(0)
        ])
    security_deposit = models.IntegerField(blank=True, validators=[
            MinValueValidator(0)
        ])

    def get_student_id(self):
        return str(self.id).zfill(4)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Driver(models.Model):
    user = models.OneToOneField(PBSUser, on_delete=models.CASCADE, blank=True, null=True)
    first_name = models.CharField(max_length=55)
    last_name = models.CharField(max_length=55)
    dl_no = models.CharField(max_length=20)
    dl_image = models.ImageField(upload_to='driving-licence/', blank=True)
    valid_upto = models.DateField()
    address = models.CharField(max_length=120)
    document = models.CharField(max_length=30)
    document_no = models.CharField(max_length=12)
    document_upload = models.ImageField(upload_to="documents", blank=True)
    blood_group = models.CharField(max_length=3, null=True)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17)  # validators should be a list
    alternate_phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)

    def __str__(self):
        return self.first_name

class Conductor(models.Model):
    user = models.OneToOneField(PBSUser, on_delete=models.CASCADE, null=True, blank=True)
    first_name = models.CharField(max_length=55)
    last_name = models.CharField(max_length=55)
    address = models.CharField(max_length=120)
    document = models.CharField(max_length=30)
    document_no = models.CharField(max_length=12)
    document_upload = models.ImageField(upload_to="documents", blank=True)
    blood_group = models.CharField(max_length=3, null=True)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17)  # validators should be a list
    alternate_phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)

    def __str__(self):
        return self.first_name

class Bus(models.Model):
    bus_no = models.CharField(max_length=10)
    driver_name = models.ForeignKey(Driver, on_delete=models.CASCADE, related_name='bus')
    conductor_name = models.ForeignKey(Conductor, on_delete=models.CASCADE)
    owner_name = models.ForeignKey(Owner, on_delete=models.CASCADE, related_name="buses")
    insurance = models.DateField()
    fitness = models.DateField()
    tax = models.DateField()
    permit = models.DateField()


    def __str__(self):
        return f"Bus No: {self.bus_no} Owner: {self.owner_name}"



class Teacher(models.Model):
    user = models.OneToOneField(PBSUser, on_delete=models.CASCADE, blank=True, null=True)
    school_name = models.ForeignKey(School, on_delete=models.CASCADE, default=1)
    first_name = models.CharField(max_length=55)
    last_name = models.CharField(max_length=55)
    added = models.DateField(auto_now_add=True)
    id = models.AutoField(primary_key=True)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17)  # validators should be a list
    alternate_phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)
    address = models.CharField(max_length=120)
    bus = models.ForeignKey(Route, on_delete=models.CASCADE)
    fee_per_month = models.IntegerField(validators=[
        MinValueValidator(0)
    ])
    security_deposit = models.IntegerField(blank=True, validators=[
        MinValueValidator(0)
    ])

    def get_teacher_id(self):
        return str(self.id).zfill(4)
    def __str__(self):
        return self.name

class FeeCollector(models.Model):
    user = models.OneToOneField(PBSUser, on_delete=models.CASCADE, blank=True, null=True)
    first_name = models.CharField(max_length=55)
    last_name = models.CharField(max_length=55)
    address = models.CharField(max_length=120)
    document = models.CharField(max_length=30)
    document_no = models.CharField(max_length=12)
    document_upload = models.ImageField(upload_to="documents", blank=True)
    blood_group = models.CharField(max_length=3, null=True)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17)  # validators should be a list
    alternate_phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)

    def __str__(self):
        return self.user.first_name

class Diesel(models.Model):
   bus = models.ForeignKey(Bus, on_delete=models.CASCADE, related_name='bus')
   diesel_consumed=models.IntegerField(validators=[MinValueValidator(0)])
   date=models.DateField(default=datetime.now, blank=True)
   diesel_rate=models.IntegerField(validators=[MinValueValidator(0)],default=74)
   total=models.IntegerField(validators=[MinValueValidator(0)],default=1000)
   def __str__(self):
      return str(self.bus.bus_no)+str(self.date)
                  
                        
