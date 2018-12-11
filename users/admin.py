from django.contrib import admin
from .models import Newuser,RegisterArtisan
import two_factor
# Register your models here.
admin.site.register(Newuser)
admin.site.register(RegisterArtisan)
