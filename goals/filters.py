import django_filters
from .models import Dailygoal


# we'll use this class to filter products based on model attributes
class DailygoalFilter(django_filters.FilterSet):

    class Meta:
        model = Dailygoal
        fields = {
                # 'tags': ['icontains', ],
                'date': ['exact', 'year__gte', 'year__lte', 'month__gte', 'month__lte'],
        }

