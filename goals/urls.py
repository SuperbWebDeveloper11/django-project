from django.urls import path
from . import views

app_name = 'goals'

urlpatterns = [
    path('daily/', views.daily_goals_index, name='daily_goals_list'),
    path('daily/add/', views.create_daily_goal, name='create_daily_goal'),
    path('daily/<int:pk>/', views.daily_goal_details, name='daily_goal_details'),
    path('daily/<int:pk>/edit/', views.edit_daily_goal, name='edit_daily_goal'),
    path('daily/<int:pk>/delete/', views.delete_daily_goal, name='delete_daily_goal'),
]

