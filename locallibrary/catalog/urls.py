"""This is the python file which hold all the URLs for the catalog application"""

from django.urls import path
from . import views

# Path string/ function passed at string / path name for reference in html
urlpatterns = [
    path('', views.index, name='index'),
    path('projects/', views.ProjectListView.as_view(), name='projects'),
    path('project/<int:pk>', views.ProjectDetailView.as_view(), name='project-detail'),
    path('prjmgrs/', views.PrjMgrListView.as_view(), name='prjmgrs'),
    path('prjmgr/<int:pk>', views.PrjMgrDetailView.as_view(), name='prjmgr-detail'),
    path('available-items/', views.ItemsAvailableListView.as_view(), name='available-items'),
    path('project/<int:pk>/completion/', views.set_completion_date, name='project-completion-date'),
]
