from django.db import models

# Create your models here.

class mumbaiJobs(models.Model):
    companyName = models.CharField(max_length=100)
    jobTitle = models.CharField()
    salary = models.CharField()
    qualification = models.CharField()
    location = models.CharField()
    joiningDate = models.DateField()
    address = models.CharField()
    contactNumber = models.CharField()
    email = models.CharField()
    applyNow = models.CharField()

class puneJobs(models.Model):
    companyName = models.CharField(max_length=100)
    jobTitle = models.CharField()
    salary = models.CharField()
    qualification = models.CharField()
    location = models.CharField()
    joiningDate = models.DateField()
    address = models.CharField()
    contactNumber = models.CharField()
    email = models.CharField()
    applyNow = models.CharField()

class bangloreJobs(models.Model):
    companyName = models.CharField(max_length=100)
    jobTitle = models.CharField()
    salary = models.CharField()
    qualification = models.CharField()
    location = models.CharField()
    joiningDate = models.DateField()
    address = models.CharField()
    contactNumber = models.CharField()
    email = models.CharField()
    applyNow = models.CharField()

class delhiJobs(models.Model):
    companyName = models.CharField(max_length=100)
    jobTitle = models.CharField()
    salary = models.CharField()
    qualification = models.CharField()
    location = models.CharField()
    joiningDate = models.DateField()
    address = models.CharField()
    contactNumber = models.CharField()
    email = models.CharField()    
    applyNow = models.CharField()       