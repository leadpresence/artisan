from django.shortcuts import render,redirect
from django.contrib import messages 
#from django.contrib.auth.forms import UserCreationForm
from .userforms import RegisterForm,TestForm ,RegArtisans
# Create your views here.


def register(request):
    if request.method=='POST':
        form=RegisterForm(request.POST)#we'll use and instance of this form in view file

        if (form.is_valid()): 
            try:
                form.save()
                messages.success(request,'Your acount has been Created Sucessfully, You can now Login')
                return redirect(request,'users/register.html')
            
            except:
                pass
        else:
                    messages.warning(request,"your username or password is incorrect")
    else:  
            form=RegisterForm      
    
        
    return render(request, 'users/register.html')
    
def home(request):
    
    return render(request, 'users/home.html')
def artisan(request): 
    if request.method=='POST':
        form=RegArtisans(request.POST)
        if form.is_valid():
          
                try:
                    form.save()
                    messages.success(request,'Your acount has been Created Sucessfully, You can now Login')
                    return redirect(request,'users/register.html')
                except:
                    pass
        
                        
    else:  
            form=RegArtisans  
  
    return render(request,'users/Register_Login_artisan.html',{'form':form})




#def login(request):
    #check if a user is a member then login her in
    #django-doc 226

#def logout(request):
