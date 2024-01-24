from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator

# Create your models here.
class Band(models.Model):
  
  class Genre(models.TextChoices ):
    HIP_HOP ="HH"
    RYTHM_AND_BLUES="RB"
    ROCK ="RK"
    GOSPEL ="GP"
  name = models.CharField(max_length=200)
  
  genre = models.CharField(choices =Genre.choices, max_length=5)
  biography = models.CharField(max_length=200, default="")
  year_formed = models.IntegerField(
    validators=[MinValueValidator(1900), MaxValueValidator(2024)], default=""
                                    )
  active = models.BooleanField(default="")
  official_homepage = models.URLField(null=True,blank=True)
  
  def __str__(self):
    return f'{self.name}'
  
 
 

class Listing(models.Model):
  class Types(models.TextChoices):
    RECORDS = "RC"
    CLOTHINGS = "CL"
    POSTERS = "PS"
    MISCELLANEOUS = "MC"
  title = models.CharField(max_length=200)
  

  description = models.CharField(max_length=300)
  sold = models.BooleanField(default=True)
  year_originated = models.IntegerField(null=True)
  types = models.CharField(choices = Types.choices, max_length = 5)
  band = models.ForeignKey(Band,null=True,on_delete = models.SET_NULL)
  
  def __str__(self):
    return f'{self.title}'
  
  
   