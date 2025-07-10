from django.contrib import admin
from jobapp.models import mumbaiJobs , puneJobs , bangloreJobs , delhiJobs
# Register your models here.
admin .site .register(mumbaiJobs)
admin .site .register(puneJobs)
admin .site .register(bangloreJobs)
admin .site .register(delhiJobs)    
