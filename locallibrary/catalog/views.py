"""This is the python file which dispatches logic to each view."""

# Necessary imports from Django libs.
from django.shortcuts import render  # For rendering html template.
from catalog.models import Project, PrjMgr, Item  # Importing model information.
from django.views import generic  # Importing standardized useful views.
from django.contrib.auth.mixins import LoginRequiredMixin  # Importing out-of-the-boz authentication functionality.


def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_projects = Project.objects.all().count()
    num_items = Item.objects.all().count()
    num_items_available = Item.objects.filter(status__exact='A').count()
    num_project_managers = PrjMgr.objects.count()
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    context = {
        'num_projects': num_projects,
        'num_items': num_items,
        'num_items_available': num_items_available,
        'num_project_managers': num_project_managers,
        'num_visits': num_visits,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)


class ProjectListView(generic.ListView):  # View function for project list view.
    model = Project


class ProjectDetailView(generic.DetailView):  # View function for project detail view.
    model = Project


class PrjMgrListView(generic.ListView):  # View function for project manager list view.
    model = PrjMgr


class PrjMgrDetailView(generic.DetailView):  # View function for project manager detail view.
    model = PrjMgr


class ItemsAvailableListView(LoginRequiredMixin, generic.ListView):  # View function for assigned items view.
    """Generic class-based view listing resources assigned to current user."""
    model = Item
    template_name = 'catalog/available_items.html'
    paginate_by = 50

    def get_queryset(self):  # Returns any items which are deployed. .filter(prj_mgr=self.request.user)
        return Item.objects.filter(status__exact='A')

import datetime

from django.contrib.auth.decorators import permission_required
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse

from catalog.forms import SetCompletionDateForm


def set_completion_date(request, pk):
    """View function for setting completion date for a project."""
    project = get_object_or_404(Project, pk=pk)

    # If this is a POST request then process the Form data
    if request.method == 'POST':

        # Create a form instance and populate it with data from the request (binding):
        form = SetCompletionDateForm(request.POST)

        # Check if the form is valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required (here we just write it to the model due_back field)
            project.completion_date = form.cleaned_data['completion_date']
            project.save()

            # redirect to a new URL:
            return HttpResponseRedirect(reverse('projects') )

    # If this is a GET (or any other method) create the default form.
    else:
        proposed_completion_date = datetime.date.today() + datetime.timedelta(weeks=3)
        form = SetCompletionDateForm(initial={'renewal_date': proposed_completion_date})

    context = {
        'form': form,
        'project': Project,
    }

    return render(request, 'catalog/set_completion_date.html', context)