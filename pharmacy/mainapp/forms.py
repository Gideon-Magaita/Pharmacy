from django import forms
from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, Group



class UserForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'Enter Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder': 'enter Password'}))
    group = forms.ModelChoiceField(queryset=Group.objects.all(), widget=forms.Select(attrs={'class':'form-control'}))



class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']



class ApplicationForm(ModelForm):
    class Meta:
        model = Applicant
        fields = [
            'applicant_name','full_address',
            'applicant_age',
            'gender',
            'phone_number',
            'pharmacy_name',
            'location',
            'full_name',
            'address',
            'phone',
            'registration_number',
            'registration_date',
            'certificate',
            'application_date',
            'signature',
        ]

        widgets = {
        'applicant_name':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter your name','required':'required'}),
        'full_address':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter your address','required':'required'}),
        'applicant_age': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter your age'}),        'phone_number':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter phone number(+255)','required':'required'}),
        'gender':forms.Select(attrs={'class':'form-control','required':'required'}),
        'phone_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your phone number'}),
        'pharmacy_name':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter pharmacy name','required':'required'}),
        'location':forms.Select(attrs={'class':'form-control','required':'required'}),
        'full_name':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter  drug outlets name','required':'required'}),
        'address':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter your address','required':'required'}),
        'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter drug outlets phone number'}),
        'registration_number':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter pharmacy registration number','required':'required'}),
        'registration_date':forms.DateInput(attrs={'class':'form-control','type':'date','required':'required'}),
        'certificate':forms.FileInput(attrs={'class':'form-control', 'required':'required'}),
        'application_date':forms.DateInput(attrs={'class':'form-control','type':'date','required':'required'}),
        'signature': forms.CheckboxInput(attrs={'class': 'form-control','rqeuired':'required'}),
    }



class VeoForm(ModelForm):
    class Meta:
        model = Applicant
        fields = [
            'applicant_nationality',
            'applicant_behaviour',
            'other_comment',
            'received_date',
            'processed_date',
            'veo_signature',
            'veo_name',
        ]


        widgets={
        'applicant_nationality':forms.Select(attrs={'class':'form-control','required':'required'}),
        'applicant_behaviour':forms.Select(attrs={'class':'form-control','required':'required'}),
        'other_comment':forms.Textarea(attrs={'class':'form-control'}),
        'received_date':forms.DateInput(attrs={'class':'form-control','type':'date','required':'required'}),
        'processed_date':forms.DateInput(attrs={'class':'form-control','type':'date','required':'required'}),
        'veo_signature': forms.CheckboxInput(attrs={'class': 'form-control','rqeuired':'required'}),
        'veo_name':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter your name','required':'required'}),

        }

#-------------------------------------------------------------------------------

class WeoForm(ModelForm):
    class Meta:
        model = Applicant
        fields = [
            'received_date_from_veo',
            'interview_date',
            'interview_result',
            'comments',
            'weo_name',
            'weo_signature',
            'submission_date',
        ]


        widgets={
        'received_date_from_veo':forms.DateInput(attrs={'class':'form-control','type':'date','required':'required'}),
        'interview_date':forms.DateInput(attrs={'class':'form-control','type':'date','required':'required'}),
        'interview_result': forms.TextInput(attrs={'class': 'form-control','rqeuired':'required','placeholder':'Enter inteview result'}),
        'comments':forms.Textarea(attrs={'class':'form-control'}),
        'weo_name':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter your name','required':'required'}),
        'weo_signature': forms.CheckboxInput(attrs={'class': 'form-control','rqeuired':'required'}),
        'submission_date':forms.DateInput(attrs={'class':'form-control','type':'date','required':'required'}),
        }


#-------------------------------------------------------------------------------

class CfdcForm(ModelForm):
    class Meta:
        model = Applicant
        fields = [
            'cfdc_received_date',
            'cfdc_comment',
            'cfdc_name',
            'cfdc_signature',
        ]

        widgets={
        'cfdc_received_date':forms.DateInput(attrs={'class':'form-control','type':'date','required':'required'}),
        'cfdc_comment':forms.Textarea(attrs={'class':'form-control'}),
        'cfdc_name':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter your name','required':'required'}),
        'cfdc_signature': forms.CheckboxInput(attrs={'class': 'form-control','rqeuired':'required'}),
        }

#-------------------------------------------------------------------------------

class TfdaForm(ModelForm):
    class Meta:
        model = Applicant
        fields = [
            'status',
        ]

        widgets={
        'status':forms.TextInput(attrs={'class':'form-control','required':'required'}),
        }