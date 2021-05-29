# this is not the best way to create Dailygoal model, I will change it later
from django.db import models
from django import forms
from taggit.managers import TaggableManager

GOAL_STATUS = (
        ('DONE','done'),
        ('UNDONE', 'undone'),
        ('UNWRITTEN', 'unwritten'),
        )


class Dailygoal(models.Model):
    date = models.DateField()
    goal1 = models.CharField(max_length=200, blank=True, null=True)
    goal1_status = models.CharField(choices=GOAL_STATUS, max_length=15, default='UNWRITTEN')
    goal2 = models.CharField(max_length=200, blank=True, null=True)
    goal2_status = models.CharField(choices=GOAL_STATUS, max_length=15, default='UNWRITTEN')
    goal3 = models.CharField(max_length=200, blank=True, null=True)
    goal3_status = models.CharField(choices=GOAL_STATUS, max_length=15, default='UNWRITTEN')
    goal4 = models.CharField(max_length=200, blank=True, null=True)
    goal4_status = models.CharField(choices=GOAL_STATUS, max_length=15, default='UNWRITTEN')
    goal5 = models.CharField(max_length=200, blank=True, null=True)
    goal5_status = models.CharField(choices=GOAL_STATUS, max_length=15, default='UNWRITTEN')
    goal6 = models.CharField(max_length=200, blank=True, null=True)
    goal6_status = models.CharField(choices=GOAL_STATUS, max_length=15, default='UNWRITTEN')
    goal7 = models.CharField(max_length=200, blank=True, null=True)
    goal7_status = models.CharField(choices=GOAL_STATUS, max_length=15, default='UNWRITTEN')
    other_goals = models.TextField(blank=True, null=True)
    tags = TaggableManager(blank=True)
    created_by = models.ForeignKey('auth.User', related_name='daily_goals', on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs) # Call the "real" save() method.
        if self.goal1 and self.goal1_status == 'UNWRITTEN':
            self.goal1_status = 'UNDONE'
            super().save(*args, **kwargs)
        if self.goal2 and self.goal2_status == 'UNWRITTEN':
            self.goal2_status = 'UNDONE'
            super().save(*args, **kwargs)
        if self.goal3 and self.goal3_status == 'UNWRITTEN':
            self.goal3_status = 'UNDONE'
            super().save(*args, **kwargs)
        if self.goal4 and self.goal4_status == 'UNWRITTEN':
            self.goal4_status = 'UNDONE'
            super().save(*args, **kwargs)
        if self.goal5 and self.goal5_status == 'UNWRITTEN':
            self.goal5_status = 'UNDONE'
            super().save(*args, **kwargs)
        if self.goal6 and self.goal6_status == 'UNWRITTEN':
            self.goal6_status = 'UNDONE'
            super().save(*args, **kwargs)
        if self.goal7 and self.goal7_status == 'UNWRITTEN':
            self.goal7_status = 'UNDONE'
            super().save(*args, **kwargs)

    def total_goals(self):
        total_goals = 0
        if self.goal1:
            total_goals = total_goals + 1
        if self.goal2:
            total_goals = total_goals + 1
        if self.goal3:
            total_goals = total_goals + 1
        if self.goal4:
            total_goals = total_goals + 1
        if self.goal5:
            total_goals = total_goals + 1
        return total_goals


    def __str__(self):
        return self.goal1


    def get_absolute_url(self):
        return reverse('daily_goal_details', kwargs={'pk', self.pk})


