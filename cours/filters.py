import django_filters
from .models import cours


class coursFilters(django_filters.FilterSet):
    class Meta:
        model = cours
        fields = '__all__'
        exclude= ['debut','fin']