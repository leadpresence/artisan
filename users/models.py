from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.utils import timezone
from django.utils.encoding import smart_text
from .validators import phone_validation
STATES=(
    ('AB','Abia'),
    ('AD','Adamawa'),
    ('AN','Anambra'),
    ('BU','Bauchi'),
    ('BE','Benue')
    )
ARTISAN_SKILLS=(
          ('A/C Maintenace','A/C maintenance'),
          ('Plumbing','plumbing'),
          ( 'Hygeine-Cleaning','hygiene-cleaning'),
          ('Car-Wash','car wash'),
          ('Chef-All-Meals','All-Meals'),
          ('Chef-African','Chef-Afrcan'),
          ('Chef-Intercontinental','Chef-Intercontinental'),
          ('Electrical-Wiring','electrical-wiring'),
          ('Electrical-Electronics','electrical-electronics'),
          ('Engineering-Auto','engineering-auto'),
          ('Engineering-Generators','engineering-generators'),
          ('Driving-Trucks','driving-trucks'),
          ('Driving-HeavyDuty','driving-Heavy-Duty'),
          ('Driving-Automobile','driving-automobile'),
          ('Medicals-Nurse','medicals-nurse'),
         
          )
# Create your models here.
class Newuser(models.Model):
    firstname       =models.CharField(max_length=20)
    phone           = models.IntegerField()
    email           =models.EmailField(unique=True,
                                        error_messages={ 'unique': 'Email is incorrect or Already exists'})
    date_created    =models.DateField(auto_now_add=False,auto_now=False,default=timezone.now)
    #date_created.editable=True
    class Meta:
       #make email and phone numbers unique
        unique_together=[('email','phone')]
    def __str__(self):
            return (smart_text(self.email))

class RegisterArtisan(models.Model):
    artisan_name             =models.CharField(max_length=150)
    artisan_email             =models.EmailField()
    artisan_password          =models.CharField(max_length=150)
    artisan_repeat_password   =models.CharField(max_length=150)
    artisan_phone             =models.IntegerField(validators=[phone_validation])
    state_of_origin           = models.CharField(choices=STATES,max_length=150)
    artisan_skill             = models.CharField(choices=ARTISAN_SKILLS,max_length=150)
    date_created              =models.DateField(auto_now_add=False,auto_now=False,default=timezone.now)
        #widgets=models.Select(attrs='placeholder':'select state')
        
    class Meta:
        unique_together=[('artisan_email','artisan_phone')]
    def __str__(self):
            return (smart_text(self.artisan_email)) 




      