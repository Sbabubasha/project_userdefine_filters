from django.shortcuts import render

# Create your views here.
def userdefine(request):
    d={'user':'hAI HelLoW hOw ArE YoU'}
    return render(request,'user.html',d)
