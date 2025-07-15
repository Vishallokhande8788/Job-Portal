from django.shortcuts import render
from jobapp.models import mumbaiJobs , puneJobs , bangloreJobs , delhiJobs

# Create your views here.
def home(request):
    return render(request, 'home.html')

def mumbaiJobsList(request):
    mumbaiJobsView = mumbaiJobs.objects.all()
    return render(request, 'mumbaiJobs.html', {'mumbaiJobsView': mumbaiJobsView})

def puneJobsList(request):
    puneJobsView = puneJobs.objects.all()
    return render(request, 'puneJobs.html', {'puneJobsView': puneJobsView})

def bangloreJobsList(request):
    bangloreJobsView = bangloreJobs.objects.all()
    return render(request, 'bangloreJobs.html', {'bangloreJobsView': bangloreJobsView})

def delhiJobsList(request):
    delhiJobsView = delhiJobs.objects.all()
    return render(request, 'delhiJobs.html', {'delhiJobsView': delhiJobsView})

def applybtn(request):
    return render(request, 'applybtn.html')