from .models import Ticket
from datetime import datetime

def ticket_escalation_check():
    today = datetime.today.strftime('%Y-%m-%d')
    qs = Ticket.objects.filter(escalation_status='No')
    for obj in qs:
        exp = obj.escalation_date.strftime('%Y-%m-%d')
        print(exp)
        if exp < today:
            obj.escalation_status='Yes'
            obj.status='Escalated'
            obj.save()

