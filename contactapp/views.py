from django.shortcuts import render
from .models import ContactData

def ContactForm(request):
    if request.method=='GET':
        return render(request,'contact.html')

    else:
        ContactData(
        first_name=request.POST.get('fname'),
        last_name=request.POST.get('lname'),
        course=request.POST.get('course'),
        age=request.POST.get('age'),
        gender=request.POST.get('gender'),
        email=request.POST.get('email'),
        mobile=request.POST.get('mobile'),
        location=request.POST.get('loc')
        ).save()

        return render(request,'contact.html')
