"""This python file controls the behavior of the built-in Django admin page"""

from django.contrib import admin
from catalog.models import PrjMgr, Project, Item


class ItemInline(admin.TabularInline):  # Shows list of items using a standard predefined Django class.
    model = Item
    extra = 0


class ProjectInline(admin.TabularInline):  # Shows list of projects using a standard predefined Django class.
    model = Project
    extra = 0


class PrjMgrAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'emp_num', 'date_joined')
    fields = ['first_name', 'last_name', 'date_joined']
    inlines = [ProjectInline]


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('prj_num', 'prj_mgr', 'summary')
    inlines = [ItemInline]


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_filter = ('prj', 'item_num', 'status')
    list_display = ('prj', 'item_num', 'status', 'description', 'sector', 'date_created')


admin.site.register(PrjMgr, PrjMgrAdmin)