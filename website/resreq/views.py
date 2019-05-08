from django.shortcuts import render
from django.views import generic
#
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
##
import datetime
from django.contrib.auth.decorators import permission_required
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from resreq.forms import RescheduleProjectForm
###
from resreq.models import Project, PrjMgr, Item
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .filters import ItemFilter, ProjectFilter, PrjMgrFilter


def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_projects = Project.objects.all().count()
    num_projects_overdue = Project.objects.filter(prj_status__exact='Behind Schedule').count()
    num_items = Item.objects.all().count()
    num_items_available = Item.objects.filter(status__exact='Available').count()
    num_prjmgrs = PrjMgr.objects.count()
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    context = {
        'num_projects': num_projects,
        'num_projects_overdue': num_projects_overdue,
        'num_items': num_items,
        'num_items_available': num_items_available,
        'num_prjmgrs': num_prjmgrs,
        'num_visits': num_visits,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)


class HistoryListView(LoginRequiredMixin, generic.ListView):
    model = Item.history
    paginate_by = 10


def history(request):
    """View function for history page of site."""
    proj_history = Project.history.all()
    item_history = Item.history.all()

    context = {
        'proj_history': proj_history,
        'item_history': item_history,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'resreq/history.html', context=context)


class ProjectSearchView(LoginRequiredMixin, generic.ListView):
    model = Project
    template_name = 'resreq/project_search.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = ProjectFilter(self.request.GET, queryset=self.get_queryset())
        return context


class ProjectListView(LoginRequiredMixin, generic.ListView):
    model = Project
    paginate_by = 10


class ProjectDetailView(LoginRequiredMixin, generic.DetailView):
    model = Project
    paginate_by = 1


class PrjMgrSearchView(LoginRequiredMixin, generic.ListView):
    model = PrjMgr
    template_name = 'resreq/prjmgr_search.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = PrjMgrFilter(self.request.GET, queryset=self.get_queryset())
        return context


class PrjMgrListView(LoginRequiredMixin, generic.ListView):
    model = PrjMgr
    paginate_by = 10


class PrjMgrDetailView(LoginRequiredMixin, generic.DetailView):
    model = PrjMgr
    paginate_by = 1


class ItemListView(LoginRequiredMixin, generic.ListView):
    model = Item
    paginate_by = 10


class ItemSearchView(LoginRequiredMixin, generic.ListView):
    model = Item
    template_name = 'resreq/item_search.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = ItemFilter(self.request.GET, queryset=self.get_queryset())
        return context


class ItemDetailView(LoginRequiredMixin, generic.DetailView):
    model = Item
    paginate_by = 1


@permission_required('user.is_staff')
def reschedule_project_mgmt(request, pk):
    """View function for rescheduling a project by mgmt."""
    prj = get_object_or_404(Project, pk=pk)

    # If this is a POST request then process the Form data
    if request.method == 'POST':

        # Create a form instance and populate it with data from the request (binding):
        form = RescheduleProjectForm(request.POST)

        # Check if the form is valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required (here we just write it to the model due_back field)
            prj.completion_date = form.cleaned_data['renewal_date']
            prj.save()

            # redirect to a new URL:
            return HttpResponseRedirect(reverse('all-borrowed'))

    # If this is a GET (or any other method) create the default form.
    else:
        proposed_renewal_date = datetime.date.today() + datetime.timedelta(weeks=3)
        form = RescheduleProjectForm(initial={'renewal_date': proposed_renewal_date})

    context = {
        'form': form,
        'prj': prj,
    }

    return render(request, 'resreq/project_reschedule.html', context)


###


class PrjMgrCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    permission_required = 'user.is_staff'
    model = PrjMgr
    fields = '__all__'


class PrjMgrUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    permission_required = 'user.is_staff'
    model = PrjMgr
    fields = '__all__'


class PrjMgrDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    permission_required = 'user.is_staff'
    model = PrjMgr
    success_url = reverse_lazy('prjmgrs')


class ProjectCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    permission_required = 'user.is_staff'
    model = Project
    fields = '__all__'


class ProjectUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    permission_required = 'user.is_staff'
    model = Project
    fields = '__all__'


class ProjectDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    permission_required = 'user.is_staff'
    model = Project
    success_url = reverse_lazy('projects')


class ItemCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    permission_required = 'user.is_staff'
    model = Item
    fields = ('prj', 'notes', 'date_added', 'status', 'sector', 'description')


class ItemUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    permission_required = 'user.is_staff'
    model = Item
    fields = ('prj', 'notes', 'date_added', 'status', 'sector', 'description')


class ItemDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    permission_required = 'user.is_staff'
    model = Item
    success_url = reverse_lazy('items')
