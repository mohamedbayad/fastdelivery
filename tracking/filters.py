import django_filters
from .models import *

class TrackingFilter(django_filters.FilterSet):
    class Meta:
        model = Tracking
        fields = ["tracking_number"]
        # fields = "__all__"