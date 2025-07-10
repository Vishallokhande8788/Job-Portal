from django.shortcuts import render
from jobapp.models import mumbaiJobs

# Create your views here.
def home(request):
    return render(request, 'home.html')

def mumbaiJobsList(request):
    mumbaiJobsView = mumbaiJobs.objects.all()
    return render(request, 'mumbaiJobs.html', {'mumbaiJobsView': mumbaiJobsView})