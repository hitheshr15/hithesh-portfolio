from django.db import models

# Create your models here.

class Technology(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Project(models.Model):

    title = models.CharField(max_length=200)
    category = models.CharField(max_length=100)
    description = models.TextField()
    technologies = models.ManyToManyField(Technology,blank=True)
    github_url = models.URLField(blank=True)
    live_url = models.URLField(blank=True)
    image = models.ImageField(upload_to='projects/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title



class Certification(models.Model):

    title = models.CharField(max_length=200)
    issuer = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    issue_date = models.DateField( blank=True, null=True)
    credential_id = models.CharField( max_length=200, blank=True)
    certificate = models.FileField( upload_to='certificates/', blank=True, null=True)
    credential_url = models.URLField(blank=True)

    def __str__(self):
        return self.title


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(blank=True)
    subject = models.CharField(max_length=200,blank=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Experience(models.Model):
    job_title = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    location = models.CharField(max_length=200, blank=True)

    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)

    description = models.TextField()

    technologies = models.ManyToManyField(Technology,blank=True)

    def __str__(self):
        return f"{self.job_title} - {self.company}"




