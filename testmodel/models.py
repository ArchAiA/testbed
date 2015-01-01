from django.db import models

# Test Case 1) Basic Model
class Person(models.Model):
    YEAR_IN_SCHOOL_CHOICES = (
        ('FR', 'Freshman'),
        ('SO', 'Sophmore'),
        ('JR', 'Junior'),
        ('SR', 'Senior'),
        ('GR', 'Graduate'),
    )

    first_name = models.CharField(max_length=20, help_text="Enter Your First Name, You Idiot")
    last_name = models.CharField(max_length=20, help_text="Enter Your Last Name, You Idiot")
    year_in_school = models.CharField(max_length=2, choices=YEAR_IN_SCHOOL_CHOICES)
    
    
# Test Case 2) Music Catalog
class Musician(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    band_name = models.CharField(max_length=30)
    
class Album(models.Model):
    artist = models.ForeignKey(Musician)
    title = models.CharField(max_length=30)
    release_date = models.DateField()
    num_starts = models.IntegerField()

    
    

