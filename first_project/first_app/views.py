from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import WebPage
from . import forms

def index(request):
    webpages = WebPage.objects.order_by('id')
    data = {"Pages":webpages}
    return render(request, 'first_app/index.html', context=data)


def form_name(request):
    form = forms.BasicForm()
    if request.method == "POST":
        form = forms.BasicForm(request.POST)
        if(form.is_valid()):
            print("success")
    return render(request,'first_app/basicform.html',{'form':form})


def home(request):
    return render(request,'first_app/home.html')


def about(request):
    return render(request,'first_app/about.html')

def register(request):
    registered = False;
    userform = forms.UserForm()
    userInfoForm = forms.UserProfileInfoForm()
    if(request.method == "POST"):
        userForm = forms.UserForm(data=request.POST)
        userInfoForm = forms.UserProfileInfoForm(data=request.POST)
        if userForm.is_valid() and userInfoForm.is_valid():
            user = userForm.save()
            user.set_password(user.password)
            user.save()
            profile = userInfoForm.save(commit=False)
            profile.User = user;

            if 'ProfilePicture' in request.FILES:
                profile.ProfilePicture = request.FILES['ProfilePicture']

            profile.save()
            registered = True
        else:
            print(userForm.errors,userInfoForm.errors)
    else:
        userform = forms.UserForm()
        userInfoForm = forms.UserProfileInfoForm()
    return render(request,'first_app/register.html',{'user_form':userform,
                            'profile_form':userInfoForm,'registered':registered})
# Create your views here.
