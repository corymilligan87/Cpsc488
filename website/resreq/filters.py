import django_filters
from .models import Item, Project, PrjMgr


class PrjMgrFilter(django_filters.FilterSet):
    class Meta:
        model = PrjMgr
        fields = {
            'last_name': ['icontains'],
            'emp_num': ['icontains'],
            'role': ['icontains'],
            'projects__prj_num': ['icontains'],
            'projects__prj_status': ['icontains'],
        }


class ProjectFilter(django_filters.FilterSet):
    class Meta:
        model = Project
        fields = {
            'prj_num': ['icontains'],
            'items__item_num': ['icontains'],
            'prj_status': ['icontains'],
        }


class ItemFilter(django_filters.FilterSet):
    class Meta:
        model = Item
        fields = {
            'item_num': ['icontains'],
            'status': ['icontains'],
            'sector': ['icontains'],
            'description': ['icontains'],
        }



