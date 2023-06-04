from django.db import models
import re

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
    date_of_birth = models.DateTimeField(auto_now_add=True)
    email = models.EmailField()
    title = models.CharField(max_length=4, choices=Title_Choices)
    class Meta:
        db_table = "CRUD_APP_client_info"

        def __str__(self) -> str:
            return self.id_number
        
    def change_date_format(self, dt):
        return self.re.sub(r'(\d{1,2})-(\d{1,2})-(\d{4})', '\\1-\\2-\\3', dt)