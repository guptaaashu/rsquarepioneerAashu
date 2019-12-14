from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Student, Driver, Conductor, Bus, Route, Owner, School, Teacher, PBSUser, FeeCollector
from tempus_dominus.widgets import DatePicker
from django.core.validators import RegexValidator
from dal import autocomplete
from django.urls import reverse
from django.utils.safestring import mark_safe
from django.forms import widgets
from django.conf import settings


documents = (
    ('aadhar card', 'Aadhar Card'),
    ('pan card', 'Pan Card'),
    ('voter id card', 'Voter Id Card'),
)

blood_groups = (
    ('b+', 'B+'),
    ('a+', 'A+'),
    ('b-', 'B-'),
    ('a-', 'A-'),
    ('o+', 'O+'),
    ('o-', 'O-'),
    ('ab+', 'AB+'),
    ('ab-', 'AB-'),
    ('not known', 'Not Known'),
)
classes = (
            ('1', '1'),
            ('2', '2'),
            ('3', '3'),
            ('4', '4'),
            ('5', '5'),
            ('6', '6'),
            ('7', '7'),
            ('8', '8'),
            ('9', '9'),
            ('10', '10'),
            ('11', '11'),
            ('12', '12'),

        )
sections = (
            ('A', 'A'),
            ('B', 'B'),
            ('C', 'C'),
            ('D', 'D'),
        )
roles = (
    ('student', 'Student'),
    ('teacher', 'Teachher'),
    ('administrator', 'Administrator'),
    ('owner', 'Owner'),
    ('driver', 'Driver'),
    ('fee collector', 'Fee Collector'),

)



class RelatedFieldWidgetCanAdd(widgets.Select):

    def __init__(self, related_model, related_url=None, *args, **kw):

        super(RelatedFieldWidgetCanAdd, self).__init__(*args, **kw)

        if not related_url:
            rel_to = related_model
            info = (rel_to._meta.app_label, rel_to._meta.object_name.lower())
            related_url = 'admin:%s_%s_add' % info

        # Be careful that here "reverse" is not allowed
        self.related_url = related_url

    def render(self, name, value, *args, **kwargs):
        self.related_url = reverse(self.related_url)
        output = [super(RelatedFieldWidgetCanAdd, self).render(name, value, *args, **kwargs)]
        output.append('<a href="%s" class="add-another" id="add_id_%s" onclick="return showAddAnotherPopup(this);"> ' % \
            (self.related_url, name))
        output.append('<img src="%sadmin/img/icon_addlink.gif" width="10" height="10" alt="%s"/></a>' % (settings.STATIC_URL, 'Add Another'))
        return mark_safe(''.join(output))

class RegistrationForm(UserCreationForm):
    class Meta:
        model = PBSUser
        fields = ('username', 'first_name', 'last_name','email', 'password1', 'password2',)

class StudentAddForm(forms.ModelForm):

    class Meta:
        model = Student
        fields = '__all__'
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'class': 'datetime-input'}),
            'class_name': forms.Select(choices=classes, attrs={'class': 'form-control'}),
            'section_name': forms.Select(choices=sections, attrs={'class': 'form-control'}),
            'blood_group': forms.Select(choices=blood_groups, attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'size': 10, 'title': 'Your name'}),
            'last_name': forms.TextInput(attrs={'size': 20}),
        }

    def __init__(self, *args, **kwargs):
        super(StudentAddForm, self).__init__(*args, **kwargs)
        self.fields['route_no'].empty_label = "Select"
        self.fields['route_no'].queryset = Route.objects.all()
        self.fields['school_name'].empty_label = "Select"
        self.fields['school_name'].queryset = School.objects.all()


class DriverAddForm(forms.ModelForm):
    class Meta:
        model = Driver
        fields = '__all__'
        widgets = {
            'valid_upto': forms.DateInput(attrs={'class': 'datetime-input'}),
            'blood_group': forms.Select(choices=blood_groups, attrs={'class': 'form-control'}),
            'document': forms.Select(choices=documents, attrs={'class': 'form-control'}),
        }
    def __init__(self, *args, **kwargs):
        super(DriverAddForm, self).__init__(*args, **kwargs)
        self.fields['user'].empty_label = "Select"
        self.fields['user'].queryset = PBSUser.objects.all().filter(role='driver')

class ConductorAddForm(forms.ModelForm):
    class Meta:
        model = Conductor
        fields = '__all__'
        widgets = {
            'blood_group': forms.Select(choices=blood_groups, attrs={'class': 'form-control'}),
            'document': forms.Select(choices=documents, attrs={'class': 'form-control'}),
        }
    def __init__(self, *args, **kwargs):
        super(ConductorAddForm, self).__init__(*args, **kwargs)
        self.fields['user'].empty_label = "Select"
        self.fields['user'].queryset = PBSUser.objects.all().filter(role='conductor')

class BusAddForm(forms.ModelForm):
    class Meta:
        model = Bus
        fields = '__all__'
        widgets = {
            'insurance': forms.DateInput(attrs={'class': 'datetime-input'}),
            'fitness': forms.DateInput(attrs={'class': 'datetime-input'}),
            'tax': forms.DateInput(attrs={'class': 'datetime-input'}),
            'permit': forms.DateInput(attrs={'class': 'datetime-input'}),
        }
    def __init__(self, *args, **kwargs):
        super(BusAddForm, self).__init__(*args, **kwargs)
        self.fields['owner_name'].empty_label = "Select"
        self.fields['owner_name'].queryset = Owner.objects.all()
        self.fields['conductor_name'].empty_label = "Select"
        self.fields['conductor_name'].queryset = Conductor.objects.all()
        self.fields['driver_name'].empty_label = "Select"
        self.fields['driver_name'].queryset = Driver.objects.all()


class RouteAddForm(forms.ModelForm):
    class Meta:
        model = Route
        fields = '__all__'
        widgets = {
            'blood_group': forms.Select(choices=blood_groups, attrs={'class': 'form-control'}),
        }


class AddOwnerForm(forms.ModelForm):
    class Meta:
        model = Owner
        fields = '__all__'
        widgets = {
            'blood_group': forms.Select(choices=blood_groups, attrs={'class': 'form-control'}),
            'document': forms.Select(choices=documents, attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(AddOwnerForm, self).__init__(*args, **kwargs)
        self.fields['user'].empty_label = "Select"
        self.fields['user'].queryset = PBSUser.objects.all().filter(role='owner')


class StudentFormWithDate(forms.Form):
    school_name = forms.CharField(max_length=100)
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    class_name = forms.CharField(widget=forms.Select(choices=classes, attrs={'class': 'form-control'}))
    section_name = forms.CharField(widget=forms.Select(choices=sections, attrs={'class': 'form-control'}))
    date_of_birth = forms.DateField(widget=DatePicker(
            options={
                'minDate': '2009-01-20',
                'maxDate': '2017-01-20',
            },
        ),)
    fathers_name = forms.CharField(max_length=100)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = forms.CharField(validators=[phone_regex], max_length=17)  # validators should be a list
    address = forms.CharField(widget=forms.Textarea)
    email = forms.EmailField()
    route_no = forms.ModelChoiceField(queryset=Route.objects.all())
    blood_group = forms.CharField(widget=forms.Select(choices=blood_groups, attrs={'class': 'form-control'}))


class SchoolAddForm(forms.ModelForm):
    class Meta:
        model = School
        fields = '__all__'

class TeacherAddForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(TeacherAddForm, self).__init__(*args, **kwargs)
        self.fields['bus'].empty_label = "Select"
        self.fields['bus'].queryset = Route.objects.all()


class InUserAddForm(UserCreationForm):
    class Meta:
        model = PBSUser
        fields = ('username', 'password1', 'password2', 'role', 'email')
        widgets = {
            'password': forms.PasswordInput(),
            'role': forms.Select(choices=roles, attrs={'class': 'form-control'}),
        }

class FeeCollectorAddForm(forms.ModelForm):
    class Meta:
        model = FeeCollector
        fields = '__all__'
        widgets = {
            'blood_group': forms.Select(choices=blood_groups, attrs={'class': 'form-control'}),
            'document': forms.Select(choices=documents, attrs={'class': 'form-control'}),
        }
    def __init__(self, *args, **kwargs):
        super(FeeCollectorAddForm, self).__init__(*args, **kwargs)
        self.fields['user'].empty_label = "Select"
        self.fields['user'].queryset = PBSUser.objects.all().filter(role='feecollector')