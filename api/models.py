from django.db import models
from django.core.validators import RegexValidator, EmailValidator

class User(models.Model):
    name = models.CharField(max_length=25)

    email = models.CharField(
        max_length=50,
        unique=True,
        validators=[EmailValidator(message="Enter a valid email address.")]
    )

    phone_number = models.CharField(
        max_length=10,
        unique=True,
        validators=[
            RegexValidator(
                regex=r'^\d{10}$',
                message='Phone number must be exactly 10 digits.',
                code='invalid_phone'
            )
        ]
    )

    date_created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
