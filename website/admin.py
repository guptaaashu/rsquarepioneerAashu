from django.contrib import admin
from .models import PBSUser, Teacher, Student, Conductor, Driver, Owner, School, Bus, Diesel

admin.site.register(School)
admin.site.register(PBSUser)
admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(Conductor)
admin.site.register(Driver)
admin.site.register(Owner)
admin.site.register(Bus)
admin.site.register(Diesel)
