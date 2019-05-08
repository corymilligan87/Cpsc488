from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('projects/', views.ProjectListView.as_view(), name='projects'),
    path('project/<int:pk>', views.ProjectDetailView.as_view(), name='project-detail'),
    path('prjmgrs/', views.PrjMgrListView.as_view(), name='prjmgrs'),
    path('prjmgr/<int:pk>', views.PrjMgrDetailView.as_view(), name='prjmgr-detail'),
    path('project/<int:pk>/reschedule/', views.reschedule_project_mgmt, name='reschedule-project'),
    path('prjmgr/create/', views.PrjMgrCreate.as_view(), name='prjmgr-create'),
    path('prjmgr/<int:pk>/update/', views.PrjMgrUpdate.as_view(), name='prjmgr-update'),
    path('prjmgr/<int:pk>/delete/', views.PrjMgrDelete.as_view(), name='prjmgr-delete'),
    path('project/create/', views.ProjectCreate.as_view(), name='project-create'),
    path('project/<int:pk>/update/', views.ProjectUpdate.as_view(), name='project-update'),
    path('project/<int:pk>/delete/', views.ProjectDelete.as_view(), name='project-delete'),
    path('item/create/', views.ItemCreate.as_view(), name='item-create'),
    path('item/<int:pk>/update/', views.ItemUpdate.as_view(), name='item-update'),
    path('item/<int:pk>/delete/', views.ItemDelete.as_view(), name='item-delete'),
    path('items/', views.ItemListView.as_view(), name='items'),
    path('item/<int:pk>', views.ItemDetailView.as_view(), name='item-detail'),
    path('history/', views.history, name='history'),
    path('item-search/', views.ItemSearchView.as_view(), name='item-search'),
    path('project-search/', views.ProjectSearchView.as_view(), name='project-search'),
    path('prjmgr-search/', views.PrjMgrSearchView.as_view(), name='prjmgr-search'),

]
