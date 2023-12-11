from django.urls import path
from .views import team_member_list, team_member_add, team_member_edit

urlpatterns = [
    path('', team_member_list, name='team_member_list'),
    path('add/', team_member_add, name='team_member_add'),
    path('edit/<int:pk>/', team_member_edit, name='team_member_edit'),
]
