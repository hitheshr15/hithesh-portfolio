from django.shortcuts import render ,get_object_or_404,redirect
from django.contrib import messages
from .models import Project,Certification,Contact,Experience

from django.core.validators import validate_email
from django.core.exceptions import ValidationError

# Create your views here.
def home(request):

    if request.method == 'POST':

        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        Contact.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message
        )

        messages.success(
            request,
            'Your message has been sent successfully!'
        )

        return redirect('home')

    projects = Project.objects.all()
    certifications = Certification.objects.all()
    experiences = Experience.objects.all().order_by('-start_date')

    return render(
        request,
        'home/index.html',
        {
            'projects': projects,
            'certifications': certifications,
            'experiences': experiences,
        }
    )




def project_detail(request,id):

    project= get_object_or_404(Project,id=id)

    return render(request,'home/project_detail.html',{'project':project})




def certification_detail(request,id):

    certification= get_object_or_404(Certification,id=id)

    return render(request,'home/certification_detail.html',{'certification': certification})