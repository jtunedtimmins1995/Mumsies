from django.shortcuts import render
from django.contrib.auth.models import User
from django.db.models import F
from clubs.models import Club, Deals
from clubs.forms import RegistrationForm, ClubsForm, DealsForm
from django.contrib.auth import logout, authenticate, login
from django.shortcuts import redirect, render_to_response
from django.contrib.auth.views import (
    LoginView,
    PasswordResetView

    )
import datetime
from django.utils import timezone
from rest_framework import viewsets
from clubs.serializers import ClubSerializer, DealSerializer

class ClubViewSet(viewsets.ModelViewSet):
    queryset = Club.objects.all().order_by('id')
    serializer_class = ClubSerializer

class DealViewSet(viewsets.ModelViewSet):
    queryset = Deals.objects.all().order_by('id')
    serializer_class = DealSerializer


def home(request):

    return render(request, 'clubs/Home.html')

def login_view(request):
    if request.user.is_authenticated:
        return redirect('/clubs/')

    return LoginView.as_view(template_name='clubs/Login.html')(request)  

def CreateDeal_view(request):
    if request.method == 'POST':
        DealForm = DealsForm(request.POST)
        deal = DealForm.save(False)
        deal.club = Club.objects.get(user = request.user)
        print(request.POST['Duration'])
        hr, min = map(float, request.POST['Duration'].split(':'))
        deal.endTime = deal.startTime + datetime.timedelta(hours=hr, minutes=min)
        deal.save()
    form = DealsForm()
    args = {'form': form, 'use': 'create'}
    return render(request, 'clubs/createDeals.html', args)

def EditDeal_view(request, id):
    deal = Deals.objects.get(id = id)
    if request.method == 'POST':
        form = DealsForm(request.POST, instance = deal)
        newDeal = form.save(False)
        hr, min = map(float, request.POST['Duration'].split(':'))
        newDeal.endTime=timezone.now() + datetime.timedelta(hours=hr, minutes=min)
        newDeal.save()
        return redirect('/clubs/currentDeal/')
        
    else:    
        form = DealsForm(instance = deal)
        TimeLeft = deal.endTime - timezone.now()
        hour = str(TimeLeft).split(':')[0]
        minu = str(TimeLeft).split(':')[1]
        if len(hour)==1:
            hour = '0'+hour
        if len(minu)==1:
            minu = '0'+minu
        TimeLeft = hour + ':' + minu
        if timezone.now()>deal.endTime:
            use = 'Cannot Edit'
        else:
            use = 'Edit'
        args = {'form': form, 'use': use, 'timeLeft': str(TimeLeft), 'id': id}
        return render(request, 'clubs/createDeals.html', args)   

def ReplicateDeal_view(request, id):
    if request.method == 'POST':
        form = DealsForm(request.POST)
        newDeal = form.save(False)
        newDeal.club = Club.objects.get(user = request.user)
        hr, min = map(float, request.POST['Duration'].split(':'))
        newDeal.endTime=timezone.now() + datetime.timedelta(hours=hr, minutes=min)
        newDeal.save()
        return redirect('/clubs/currentDeal/')
        
    else:    
        deal = Deals.objects.get(id = id)
        form = DealsForm(instance = deal)
        TimeLeft = "00:00"
        args = {'form': form, 'use': 'edit', 'timeLeft': str(TimeLeft)}
        return render(request, 'clubs/createDeals.html', args)     

def CurrentDeal_view(request):
    #deals = Deals.objects.annotate(timeLeft = sum(F('startTime'), F('startTime'))).filter(club__user = request.user)
    deals = Deals.objects.filter(club__user = request.user, endTime__gt = timezone.now())
    PassedDeals = Deals.objects.filter(club__user = request.user, endTime__lte = timezone.now())
    #deals = deals.objects.aggregate(timeLeft = 'endTime' - timezone.now)
    args={'deals': deals, 'currentDate': timezone.now(), 'passedDeals': PassedDeals}
    return render(request, 'clubs/currentDeals.html', args)

def logout_view(request):
    logout(request)
    return redirect('/clubs/')     

def createUser(request):
    RegForm = RegistrationForm(request.POST or None, request.FILES or None)
    ClubForm = ClubsForm(request.POST or None, request.FILES or None)
    args = {'RegForm': RegForm, 'ClubForm': ClubForm}
    if request.method == 'POST':
        print(request)
        
        RegForm = RegistrationForm(request.POST)
        ClubForm = ClubsForm(request.POST)
        print("ERRORS:")
        print(RegForm.errors)
        print(ClubForm.errors)
        if RegForm.is_valid() and ClubForm.is_valid():
            Reg = RegForm.save()
            club = ClubForm.save(False)
            club.user = Reg
            club.save()
            new_user = authenticate(username=RegForm.cleaned_data['username'],
                                    password=RegForm.cleaned_data['password1'],
                                    )
            login(request, new_user)
            return redirect('/clubs/')
        else:
            return render_to_response('clubs/createUser.html', args)
            
    else:
        
        
        return render(request, 'clubs/createUser.html', args)


