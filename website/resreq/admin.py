from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin
from .models import Item, Project, PrjMgr

admin.site.register(Item, SimpleHistoryAdmin)
admin.site.register(Project, SimpleHistoryAdmin)


class ProjectsInline(admin.TabularInline):
    model = Project
    extra = 0


class PrjMgrAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'role', 'emp_num')
    fields = ['first_name', 'last_name', 'role']
    inlines = [ProjectsInline]


admin.site.register(PrjMgr, PrjMgrAdmin)


class ItemsInline(admin.TabularInline):
    model = Item
    extra = 0


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('item_num', 'prj', 'description', 'sector', 'status')
    list_filter = ('item_num', 'prj', 'description', 'sector', 'status')
    inlines = [ItemsInline]


#admin.site.register(ProjectAdmin)
