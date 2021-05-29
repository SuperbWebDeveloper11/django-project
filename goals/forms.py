from django import forms
from .models import Dailygoal


# This class will be used to display html5 date input
class DateInput(forms.DateInput):
    input_type = 'date'

# I will use this form to create goals for the first time
class CreateDailygoalForm(forms.ModelForm):
    class Meta:
        model = Dailygoal
        fields = ['date', 'goal1', 'goal2', 'goal3', 'goal4', 'goal5', 'goal6', 'goal7', 'other_goals', 'tags']
        widgets = {"date": DateInput}


# I will use this form to edit goals and change goals status
class EditDailygoalForm(forms.ModelForm):
    class Meta:
        model = Dailygoal
        fields = [
                'date',
                'goal1', 'goal1_status', 
                'goal2', 'goal2_status', 
                'goal3', 'goal3_status', 
                'goal4', 'goal4_status', 
                'goal5', 'goal5_status',
                'goal6', 'goal6_status',
                'goal7', 'goal7_status',
                ]
        widgets = {"date": DateInput}


