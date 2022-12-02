
from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('index', views.index, name='index'),
    path('logouts', views.logouts, name='logouts'),
    path('deposition_index',views.deposition_index,name='deposition_index'),
    path('create_desiposition',views.create_desiposition,name='create_desiposition'),
    path('sub_deposition_index',views.sub_deposition_index,name='sub_deposition_index'),
    path('create_sub_desiposition',views.create_sub_desiposition,name='create_sub_desiposition'),
    path('client_index',views.client_index,name='client_index'),
    path('create_client',views.create_client,name='create_client'),
    path('team_index',views.team_index,name='team_index'),
    path('create_team',views.create_team,name='create_team'),
    path('create_ticket',views.create_ticket,name='create_ticket'),
    path('get_ticket_details/<int:pk>',views.get_ticket_details,name='get_ticket_details'),
    path('assign_ticket/<int:pk>',views.assign_ticket,name='assign_ticket'),
    path('resolve_ticket/<int:pk>',views.resolve_ticket,name='resolve_ticket'),
    path('close_ticket/<int:pk>',views.close_ticket,name='close_ticket'),
    path('pending_ticket/<int:pk>',views.pending_ticket,name='pending_ticket'),
    path('ajax/load-dispositions/', views.load_dispositions, name='ajax_load_dispositions'),  # <-- this one here
    path('ajax/load-agents/', views.load_agents, name='ajax_load_agents'),  # <-- this one here
    
    ]
    