import django_filters
from .models import *

class PackageFilter(django_filters.FilterSet):
    class Meta:
        model = NewPackage
        fields = "__all__"
        exclude = ["withdrawn_canceled", "withdrawn_refused", "withdrawn_livery", "amount_withdrawn", "date_created" ,"date_picked_up", "remark_exchange", "remark_refund", "picked_up", "client_name", "user", "article_name", "address", "remark"]