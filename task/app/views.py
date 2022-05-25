from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from .models import addevent
from .forms import addeventForm
from django.views.generic import TemplateView
# Create your views here.

class MytemplateView(TemplateView):
    template_name = 'app/index.html'
    def get_context_data(self,**kwargs):
        context = super(MytemplateView, self).get_context_data(**kwargs)
        context['all_events'] = addevent.objects.all()
        return context

def event(request):
    if request.method == "POST":
        form = addeventForm(request,data=request.POST)
        if forms.is_valid():
            form.save()
        else:
            messages.error(request,"Enter the correct event")
            return render(request,"app/addevent.html",context={"addeventForm":form})
    else:
        form=addeventForm()
        return render(request,"app/addevent.html",context={"addeventForm":form})

def user_login(request):
    if request.method == "POST":
        form = AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            user=authenticate(username=username,password=password)
            print(user)
            if user is not None:
                login(request,user)
                return redirect("event")
            else:
                messages.error(request,"Invalid login")
                return render(request,"app/login.html",context={"login_form":form})
        else:
                messages.error(request,"Invalid login")
                return render(request,"app/login.html",context={"login_form":form})
    else:
        form=AuthenticationForm()
        return render(request,"app/login.html",context={"login_form":form})