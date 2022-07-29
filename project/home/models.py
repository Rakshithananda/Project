from statistics import mode
from django.db import models
from compositefk.fields import CompositeForeignKey

# Create your models here.

#Revenue Tables/Models
class Revenue_District(models.Model):
    district_code = models.CharField("District Code",max_length=30,primary_key=True)
    district_name = models.CharField("District Name", max_length=30)

class Revenue_Mandal(models.Model):
    district_code = models.CharField("District Code",max_length=30)
    mandal_code = models.CharField("Mandal Code", max_length=30)
    mandal_id = models.IntegerField("Mandal ID",primary_key=True)
    mandal_name = models.CharField("Mandal Name", max_length=30)

class Revenue_Village(models.Model):
    district_code = models.CharField("District Code",max_length=30)
    mandal_code = models.CharField("Mandal Code",max_length=30)
    village_code = models.CharField("Village Code",max_length=30)
    village_id = models.IntegerField("Village ID",primary_key=True)
    village_name = models.CharField("Village Name", max_length=30)

class Revenue_GSWS(models.Model):
    district_code = models.CharField("District Code",max_length=30)
    mandal_code = models.CharField("Mandal Code",max_length=30)
    village_code = models.CharField("Village Code",max_length=30)
    gsws_code = models.CharField("GSWS Code",max_length=30)
    gsws_id = models.IntegerField("GSWS ID",primary_key=True)
    gsws_name = models.CharField("GSWS Name", max_length=30)

class Revenue_VRO(models.Model):
    vro_entry = models.AutoField("VRO Entry",primary_key=True)
    district_code = models.CharField("District Code",max_length=30)
    mandal_code = models.CharField("Mandal Code",max_length=30)
    village_code = models.CharField("Village Code",max_length=30)
    gsws_code = models.CharField("GSWS Code",max_length=30)
    vro_code = models.CharField("VRO code",max_length=30)

class Revenue_VRO_Details(models.Model):
    district_code = models.CharField("District Code",max_length=30)
    mandal_code = models.CharField("Mandal Code",max_length=30)
    vro_code = models.CharField("VRO code",max_length=30)
    vro_id = models.IntegerField("VRO ID",primary_key=True)
    VRO_name = models.CharField("VRO Name", max_length=30)
    age = models.IntegerField("Age")
    gender = models.CharField("Gender",max_length=30)
    aadhar = models.CharField("Aadhar No.",max_length=16)
    relation_of = models.CharField("Relation To",max_length=30)
    relation_name = models.CharField("Relation Name",max_length=30)
    street = models.CharField("Street",max_length=30)
    village_name = models.CharField("Village Name", max_length=30)
    door_no = models.CharField("Door No.", max_length=30)
    pincode = models.CharField("Pincode", max_length=6)
    phone_no = models.CharField("Phone No.", max_length=15)
    entry_date = models.DateTimeField("Entry Date",auto_now_add=True)
class Revenue_Claiment(models.Model):
    claiment_id = models.IntegerField("Claiment ID",primary_key=True)
    gsws_id = models.IntegerField("GSWS ID")
    district_code = models.CharField("District Code",max_length=30)
    mandal_code = models.CharField("Mandal Code",max_length=30)
    village_code = models.CharField("Village Code",max_length=30)
    gsws_code = models.CharField("GSWS Code",max_length=30)
    title = models.CharField("Title",max_length=30)
    claiment_name = models.CharField("Claiment Name",max_length=30)
    age = models.IntegerField("Age")
    gender = models.CharField("Gender",max_length=30)
    aadhar = models.CharField("Aadhar No.",max_length=16)
    relation_of = models.CharField("Relation To",max_length=30)
    relation_name = models.CharField("Relation Name",max_length=30)
    village_id = models.IntegerField("Village ID")
    street = models.CharField("Street",max_length=30)
    door_no = models.CharField("Door No.", max_length=30)
    pincode = models.CharField("Pincode", max_length=6)
    phone_no = models.CharField("Phone No.", max_length=15)
    entry_date = models.DateTimeField(auto_now_add=True)
class Shedule_Entry(models.Model):
    claiment_id = models.IntegerField("Claiment ID",primary_key=True)
    gsws_id = models.IntegerField("GSWS ID")
    village_id = models.IntegerField("Village ID")
    district_code = models.CharField("District Code",max_length=30)
    mandal_code = models.CharField("Mandal Code",max_length=30)
    village_code = models.CharField("Village Code",max_length=30)
    gsws_code = models.CharField("GSWS Code",max_length=30)
    old_house_no = models.CharField("Phone No.", max_length=30) 
    nature_use = models.IntegerField("Nature Use")
    plot_no =  models.IntegerField("Plot No.")
    schedule_no = models.IntegerField("Schedule No.")
    jurisdicition = models.IntegerField("Jurisdicition")
    ward_no = models.IntegerField("Ward No.")
    block_no = models.IntegerField("Block No.")
    survey_no = models.CharField("Survey No", max_length=30)
    east_eng = models.CharField("East Eng", max_length=30)
    west_eng = models.CharField("West Eng", max_length=30)
    north_eng = models.CharField("North Eng", max_length=30)
    south_eng = models.CharField("South Eng", max_length=30)
    entry_date = models.DateTimeField("Entry Date",auto_now_add=True)

# Register Tables/Models
class Register_District(models.Model):
    district_code = models.CharField("District Code",max_length=30,primary_key=True)
    district_name = models.CharField("District Name", max_length=30)
class Register_SRO(models.Model):
    district_code = models.CharField("District Code",max_length=30)
    sro_code = models.CharField("SRO Code",max_length=30)
    sro_id = models.IntegerField("SRO ID",primary_key=True)
    sro_name = models.CharField("SRO Name", max_length=30)
class Register_Village(models.Model):
    district_code = models.CharField("District Code",max_length=30)
    sro_code = models.CharField("SRO Code",max_length=30)
    village_code = models.CharField("Village Code",max_length=30)
    village_id = models.IntegerField("Village ID",primary_key=True)
    village_name = models.CharField("Village Name", max_length=30)


