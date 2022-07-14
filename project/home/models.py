from django.db import models
from compositefk.fields import CompositeForeignKey

# Create your models here.
class Revenue_District(models.Model):
    dist_code = models.IntegerField("District Code",unique=True)
    dist_name = models.CharField("District Name",max_length=30)

    def __str__(self):
       return self.dist_name

class Revenue_Mandal(models.Model):
    mandal_code = models.IntegerField("Mandal Code")
    dist_code = models.ForeignKey(Revenue_District,to_field = "dist_code",on_delete=models.CASCADE, db_column='dist_code',verbose_name="District")
    mandal_id = models.IntegerField("Mandal Id")
    mandal_name = models.CharField("Mandal Name", max_length=30)

    class Meta:
        unique_together = ('dist_code','mandal_code')
    
    def __str__(self):
       return self.mandal_name

class Revenue_Village(models.Model):
    village_code = models.IntegerField("Village Code")
    mandal_village_code = CompositeForeignKey(Revenue_Mandal,on_delete = models.CASCADE,to_fields={'mandal_code','dist_code'})
    village_id = models.IntegerField("Village Id")
    village_name = models.CharField("Village Name", max_length=30)

    class Meta:
        unique_together = ('dist_code','mandal_code', 'village_code')

    def __str__(self):
       return self.village_name




