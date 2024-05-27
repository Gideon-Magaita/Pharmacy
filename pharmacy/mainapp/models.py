from django.db import models
from django.core.validators import RegexValidator
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.



class Region(models.Model):
    name = models.CharField(max_length=200)
    district = models.CharField(max_length=200)
    ward = models.CharField(max_length=200)
    street = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    
GENDER = [
    ('male', 'Male'),
    ('female', 'Female'),
]


NATIONALITY = [
    ('Tanzanian', 'Tanzanian'),
    ('Other', 'Other'),
]

BEHAVIOUR = [
    ('Good', 'Good'),
    ('Bad', 'Bad'),
]

class Applicant(models.Model):
    user = models.ForeignKey(User,null=True,blank=True, on_delete=models.CASCADE)
    applicant_name = models.CharField(max_length=200)
    full_address = models.CharField(max_length=200)
    applicant_age = models.IntegerField()
    gender = models.CharField(max_length=200, choices=GENDER)
    phone_number = models.CharField(
        max_length=13,
        validators=[
            RegexValidator(
                regex=r'^\+255\d{9}$',
                message="Phone number must start with '+255' followed by 9 digits."
            )
        ]
    )
    pharmacy_name = models.CharField(max_length=200)
    location = models.ForeignKey('Region', max_length=200, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    phone = models.CharField(
        max_length=13,
        validators=[
            RegexValidator(
                regex=r'^\+255\d{9}$',
                message="Phone number must start with '+255' followed by 9 digits."
            )
        ]
    )
    registration_number = models.CharField(max_length=200)
    registration_date = models.DateField()
    certificate = models.FileField(blank=True, upload_to='images/')
    application_date = models.DateField()
    signature = models.BooleanField(default=False)
    status = models.CharField(max_length=200, default="pending")
    # veo fields
    applicant_nationality = models.CharField(max_length=200, choices=NATIONALITY, default='Tanzanian')
    applicant_behaviour = models.CharField(max_length=200, choices=BEHAVIOUR, default='Good')
    other_comment = models.TextField(default='No comment')
    received_date = models.DateField(default=timezone.now)
    processed_date = models.DateField(default=timezone.now)
    veo_signature = models.BooleanField(default=False)
    veo_name = models.CharField(max_length=200, default='No name')
    # weo fields
    received_date_from_veo = models.DateField(default=timezone.now)
    interview_date = models.DateField(default=timezone.now)
    interview_result = models.CharField(max_length=200, default='good')
    comments = models.TextField(default='No comment')
    weo_name = models.CharField(max_length=200, default='No name')
    weo_signature = models.BooleanField(default=False)
    submission_date = models.DateField(default=timezone.now)
    # cfdc fields
    cfdc_received_date = models.DateField(default=timezone.now)
    cfdc_comment = models.TextField(default='No comment')
    cfdc_name = models.CharField(max_length=200, default='No name')
    cfdc_signature = models.BooleanField(default=False)

    def __str__(self):
        return self.applicant_name

