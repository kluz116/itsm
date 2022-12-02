from django import forms
from .models import *
from django.contrib.auth import get_user_model
user = get_user_model()

class DepositionForm(forms.ModelForm):
    class Meta:
        model = Desposition
        fields = "__all__"

class SubDepositionForm(forms.ModelForm):
    class Meta:
        model = SubDespositions
        fields = "__all__"

class ClientForm(forms.ModelForm):
    class Meta:
        model = Clients
        fields= "__all__"

class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields= "__all__"
#class Lol(forms.)
class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields= ['client_id','title','despositions','sub_despositions','description']
        widgets = {'description': forms.TextInput(attrs={'row': 4,'col':3,'placeholder':'Description'}),
                   'title': forms.TextInput(attrs={'row': 4,'col':3,'placeholder':'Title'}),
                   'client_id': forms.Select(attrs={'class':'select2'}),
                   'despositions': forms.Select(attrs={'class':'select2'}),
                   'sub_despositions': forms.Select(attrs={'class': 'select2bs4', 'data-size': '10',
                                                                'data-live-search': 'true', 'data-style': 'btn-white'})}

           


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['sub_despositions'].queryset = SubDespositions.objects.none()

        if 'despositions' in self.data:
            try:
                despositions_id = int(self.data.get('despositions'))
                self.fields['sub_despositions'].queryset = SubDespositions.objects.filter(deposition_id=despositions_id).order_by('sub_deposition_name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['sub_despositions'].queryset = self.instance.despositions.city_set.order_by('sub_deposition_name')
    
    

class AssignForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields= ['team_id','agent','status']
        widgets = {
        
        'status': forms.TextInput(attrs={'readonly': True}),
        'team_id': forms.Select(attrs={'class':'select2'}),
    
    }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['agent'].queryset =  CustomUser.objects.none() 

        if 'team_id' in self.data:
            try:
                team_id = int(self.data.get('team_id'))
                self.fields['agent'].queryset = user.objects.filter(team_id=team_id).order_by('first_name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        '''elif self.instance.pk:
            self.fields['agent'].queryset = self.instance.team_id.order_by('first_name')'''
    



class ResolveForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields= ['resolution_date','resolution_comment','status']
        widgets = {
        'resolution_comment': forms.TextInput(attrs={'row': 4,'col':3}),
        'status': forms.TextInput(attrs={'readonly': True}),
        'resolution_date': forms.DateInput(format=('%m/%d/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
    }


class CloseForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields= ['close_date','rating','status']
        widgets = {
        
        'status': forms.TextInput(attrs={'readonly': True}),
        'close_date': forms.DateInput(format=('%m/%d/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
    }
 

class PendingForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields= ['pending_date','pending_comment','status','escalation_status']
        widgets = {
        
        'status': forms.TextInput(attrs={'readonly': True}),
        'escalation_status': forms.TextInput(attrs={'readonly': True}),
        'escalation_date': forms.DateInput(format=('%m/%d/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
        'pending_date': forms.DateInput(format=('%m/%d/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
        'pending_comment': forms.TextInput(attrs={'row': 4,'col':3}),
    }
 
 