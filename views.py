from django.shortcuts import render,redirect,get_object_or_404,HttpResponseRedirect
from django.urls import reverse
from .models import *
from .forms import *
from django.contrib.auth import login, logout,authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import get_user_model
from django.contrib.auth.models import auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required,permission_required
from datetime import datetime, timedelta
from pytz import timezone 


user = get_user_model()



def login(request):
    if request.method=='POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None :
                login(request,user)
                return redirect('login')
            else:
                messages.error(request,"Invalid username or password")
        else:
            messages.error(request,"Invalid username or password")
    return render(request, 'cclog/login.html',context={'form':AuthenticationForm()})

def logouts(request):
    auth.logout(request)
    return redirect('login')

@login_required(login_url='login')
@permission_required("cclog.view_desposition", raise_exception=True)
def deposition_index(request):
    object = Desposition.objects.all().order_by('-id')
    return render(request,'cclog/depositions.html',{'object':object})


@login_required(login_url='login')
@permission_required("cclog.view_subdespositions", raise_exception=True)
def sub_deposition_index(request):
    object = SubDespositions.objects.all()
    return render(request,'cclog/sub_depositions.html',{'object':object})

@login_required(login_url='login')
@permission_required("cclog.view_clients", raise_exception=True)
def client_index(request):
    object = Clients.objects.all()
    return render(request,'cclog/client.html',{'object':object})

@login_required(login_url='login')
@permission_required("cclog.view_team", raise_exception=True)
def team_index(request):
    object = Team.objects.all()
    return render(request,'cclog/team.html',{'object':object})

@login_required(login_url='login')
@permission_required("cclog.view_ticket", raise_exception=True)
def index(request):
    object = Ticket.objects.all()
    return render(request,'cclog/index.html',{'object':object})


@login_required(login_url='login')
@permission_required("cclog.add_desposition", raise_exception=True)
def create_desiposition(request):
    if request.method =='POST':
        form = DepositionForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('deposition_index'))
    form = DepositionForm()
    return render(request,'cclog/create_desposition.html',{'form':form})


@login_required(login_url='login')
@permission_required("cclog.add_subdespositions", raise_exception=True)
def create_sub_desiposition(request):
    if request.method =='POST':
        form = SubDepositionForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('sub_deposition_index'))
    form = SubDepositionForm()
    return render(request,'cclog/create_subdesposition.html',{'form':form})

@login_required(login_url='login')
@permission_required("cclog.add_clients", raise_exception=True)
def create_client(request):
    if request.method =='POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('client_index'))
    form = ClientForm()
    return render(request,'cclog/create_client.html',{'form':form})

@login_required(login_url='login')
@permission_required("cclog.add_team", raise_exception=True)
def create_team(request):
    if request.method =='POST':
        form = TeamForm(request.POST)
        if form.is_valid():
            form.save()
            
            return HttpResponseRedirect(reverse('team_index'))
    form = TeamForm()
    return render(request,'cclog/create_team.html',{'form':form})

@login_required(login_url='login')
@permission_required("cclog.add_ticket", raise_exception=True)
def create_ticket(request):
    if request.method =='POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.created_by = request.user
            obj.save()
            #form.save()
            return HttpResponseRedirect(reverse('index'))
        else:
            print(form.errors.as_data()) # here you print errors to terminal
    form = TicketForm()
    return render(request,'cclog/create_ticket.html',{'form':form})

@login_required(login_url='login')
def get_ticket_details(request,pk,template_name='cclog/ticket_detail.html'):
    object = get_object_or_404(Ticket, pk=pk)

    return render(request,template_name,{'object':object})

@login_required(login_url='login')
@permission_required("cclog.change_ticket", raise_exception=True)
def assign_ticket(request,pk,template_name= 'cclog/assign_ticket.html'):
    obj = get_object_or_404(Ticket,pk=pk)
    form = AssignForm(request.POST or None,instance=obj,initial={'status': 'Assigned'})
  
    if request.method =='POST':
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('index'))
        else:
            print(form.errors.as_data()) # here you print errors to terminal
    return render(request,template_name,{'form':form})

@login_required(login_url='login')
@permission_required("cclog.change_ticket", raise_exception=True)
def resolve_ticket(request,pk,template_name= 'cclog/resolve_ticket.html'):
    obj = get_object_or_404(Ticket,pk=pk)
    form = ResolveForm(request.POST or None,instance=obj,initial={'status': 'Resolved'})
  
    if request.method =='POST':
        if form.is_valid():
            obj = form.save(commit=False)
            obj.resolved_by = request.user
            obj.save()
            return HttpResponseRedirect(reverse('index'))
        else:
            print(form.errors.as_data()) # here you print errors to terminal
    return render(request,template_name,{'form':form})

@login_required(login_url='login')
@permission_required("cclog.change_ticket", raise_exception=True)
def close_ticket(request,pk,template_name= 'cclog/close_ticket.html'):
    obj = get_object_or_404(Ticket,pk=pk)
    form = CloseForm(request.POST or None,instance=obj,initial={'status': 'Closed'})
  
    if request.method =='POST':
        if form.is_valid():
            obj = form.save(commit=False)
            obj.closed_by = request.user
            obj.save()
            #form.save()
            return HttpResponseRedirect(reverse('index'))
        else:
            print(form.errors.as_data()) # here you print errors to terminal

    
    return render(request,template_name,{'form':form})

@login_required(login_url='login')
@permission_required("cclog.change_ticket", raise_exception=True)
def pending_ticket(request,pk,template_name= 'cclog/pending_ticket.html'):
    east_africa = timezone('Africa/Nairobi')
 
    obj = get_object_or_404(Ticket,pk=pk)
    form = PendingForm(request.POST or None,instance=obj,initial={'status': 'Pending','escalation_status': 'No'})
  
    if request.method =='POST':
        if form.is_valid():
            obj = form.save(commit=True)
            obj.pending_by = request.user
            obj.escalation_date = format(datetime.now(east_africa)+ + timedelta(hours=1), '%Y-%m-%d %H:%M') 
            obj.save()
            return HttpResponseRedirect(reverse('index'))
        else:
            print(form.errors.as_data())

    
    return render(request,template_name,{'form':form})


def load_dispositions(request):
    despositions_id = request.GET.get('despositions')
    sub_deposition = SubDespositions.objects.filter(deposition_id=despositions_id).order_by('sub_deposition_name')
    return render(request, 'cclog/despositions_dropdown_list_options.html', {'sub_deposition': sub_deposition})


def load_agents(request):
    team_id = request.GET.get('team_id')
    agent = CustomUser.objects.filter(team_id=team_id).order_by('username')
    return render(request, 'cclog/agents_dropdown_list_options.html', {'agent': agent})





