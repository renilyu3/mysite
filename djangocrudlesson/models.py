from django.db import models

# Create your models here.

class Gender(models.Model):
    gender_id = models.BigAutoField(primary_key=True, blank=False) # BIGINT NOT NULL AUTO_INCREMENT PRIMARY KEY
    gender = models.CharField(max_length=55, blank=False) # VARCHAR(55) NOT NULL
    date_created = models.DateTimeField(auto_now_add=True) # TIMESTAMP DEFAUL CURRENT_TIMESTAMP
    date_updated = models.DateTimeField(auto_now=True)  # TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE_TIMESTAMP

    class Meta:
       db_table = 'genders'

class User(models.Model):
    user_id = models.BigAutoField(primary_key=True, blank=False) # BIGINT NOT NULL AUTO_INCREMENT PRIMARY KEY 
    first_name = models.CharField(max_length=55, blank=False) # VARCHART(55) NOT NULL 
    middle_name = models.CharField(max_length=55, blank=True) # VARCHART(55) DEFAULT NULL  
    last_name = models.CharField(max_length=55, blank=False) # VARCHART(55) NOT NULL 
    age = models.CharField(blank=False) # INT NOT NULL 
    birth_date = models.DateField(blank=False) # DATE NOT NULL 
    Gender = models.ForeignKey(Gender, on_delete=models.CASCADE) 
    username = models.CharField(max_length=55, blank=False) 
    password = models.CharField(max_length=255, blank=False)
    date_created = models.DateTimeField(auto_now_add=True) # TIMESTAMP DEFAULT CURRENT_TIMESTAMP 
    date_updated = models.DateTimeField(auto_now=True) # TIMESTAMP DEFAULT CURREN_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP 

    class Meta:
        db_table = 'users'
