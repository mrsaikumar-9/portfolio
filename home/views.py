from django.shortcuts import render,HttpResponse
from .models import email
def home(request):
    if request.method =='POST':
        mailv = request.POST['Mail']
        obj = email(mail=mailv)
        obj.save()
        return render(request,'thankyou.html')
    return render(request,'home.html')
