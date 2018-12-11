from django import forms
from django.forms import PasswordInput
from django.forms import widgets
from .models import Newuser , RegisterArtisan
from .validators import phone_validation

STATES=(
    ('AB','Abia'),
    ('AD','Adamawa'),
    ('AN','Anambra'),
    ('BU','Bauchi'),
    ('BE','Benue')
    )
ARTISAN_SKILLS=(
          ('A/C Maintenace','air-conditions'),
          ('Plumbing','plumbing'),
          ( 'Hygeine-Cleaning','hygiene-cleaning'),
          ('Car-Wash','car wash'),
          ('Carpenter','carpenter'),
          ('Chef','chef'),
          ('Driving-Trucks','driving-trucks'),
          ('Driving-HeavyDuty','driving-Heavy-Duty'),
          ('Driving-Automobile','driving-automobile'),
          ('Electrical-Wiring','electrical-wiring'),
          ('Electrical-Electronics','electrical-electronics'),
          ('Engineering-Auto','engineering-auto'),
          ('Engineering-Generators','engineering-generators'),
          ('Medicals-Nurse','medicals-nurse'),
          
          ) 


class RegisterForm(forms.ModelForm):
    firstname       =forms.CharField()
    phone           =forms.IntegerField()
    email           =forms.EmailField(
                                    widget=forms.TextInput(
                                     attrs={'placeholder':'enter your email','type':'Email'}) 
                                     )
    
    ##addling style to the form using widget
    phone.widget.attrs={'placeholder': '0XX-9XXX-6XXX'}
    firstname.widget.attrs={'placeholder': 'start typing your name'}
    #specifying the model used buy this form
    class Meta:
         model=Newuser
         fields=['firstname','phone','email']
        
class RegArtisans(forms.ModelForm):
    artisan_name               =forms.CharField(max_length=150)
    artisan_email              =forms.EmailField()
    artisan_password           =forms.PasswordInput()
    artisan_repeat_password    =forms.PasswordInput()
    artisan_phone              =forms.IntegerField()
    state_of_origin            = forms.Select(choices=STATES )
    artisan_skill              = forms.Select(choices=ARTISAN_SKILLS)
    class Meta:
            model=RegisterArtisan
            fields=['artisan_name','artisan_email','artisan_password','artisan_phone',
                   'artisan_repeat_password','state_of_origin','artisan_skill']
            widgets={
                'artisan_skill':forms.Select (attrs={'class':'mdb-select md-form','required':'true'}),   
                'state_of_origin':forms.Select (attrs={'class':'mdb-select md-form','required':'true'}),   
                'artisan_password':forms.PasswordInput(attrs={'type':'password'}),               
                'artisan_repeat_password': forms.PasswordInput(attrs={'type':'password'}),
                #'artisan_phone':forms.IntegerField(attrs={'placeholder':'0-XXXXXXXXXX'})
                }
    def phone_cleaned(self,*args,**kwargs):
        phone=self.cleaned_data.get("artisan_phone")
        str_conv_artisan_phone=str(phone) 
        if len(str_conv_artisan_phone) != 11:
            raise forms.ValidationError('please enter a valid phone number')
        return 
    def clean_password(self):
        #check is passwords match
       artisan_password=self.cleaned_data.get("artisan_password")
       artisan_repeat_password=self.cleaned_data.get("artisan_repeat_password")  
       if (artisan_password and artisan_repeat_password) and (artisan_repeat_password !=artisan_password):
           raise forms.ValidationError(self,'password does not match')
 
    
class TestForm(forms.Form):
    date=forms.DateField()
    state_of_origin= forms.CharField()
    phone=forms.IntegerField()
