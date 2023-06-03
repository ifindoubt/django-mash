from django.db import models
from django.core.validators import RegexValidator, EmailValidator
from django.forms import ModelForm
from django.core.exceptions import NON_FIELD_ERRORS, ValidationError
from django.utils.translation import gettext_lazy as a_

# Create your models here.

# The validation for entries from a user (client)

Title_Choices = [
    ("Mr.", "MR"),
    ("Mrs.", "MRS"),
    ("Ms.", "MS"),
    ("Ms", "Mr")
]


class Client(models.Model):
    """Model of a client form registering their details for the first time
    A client will be identified as new by their id number"""
    client_id = models.AutoField(primary_key=True)
    id_number = models.CharField(unique=1, max_length=13, help_text="Input 13 digit ID number")
    phone_number = models.CharField(max_length=11)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_of_birth = models.DateTimeField(help_text="Eg. YYYY-MM-DD")
    email = models.EmailField()
    title = models.CharField(max_length=4, choices=Title_Choices)
    class Meta:
        db_table = "CRUD_APP_client_info"

    

class ClientForm(ModelForm):
    class Meta:
        model = Client
        fields = [
            "id_number", "phone_number", "first_name", "last_name", "date_of_birth",
            "email", "title"
            ]