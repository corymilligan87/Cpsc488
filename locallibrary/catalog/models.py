"""This is the python file in which all models are built for program."""

# These import standard tools from Django framework for models, url path construction and authorization.
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
import uuid


class Project(models.Model):
    """Model representing a project."""
    prj_num = models.AutoField(primary_key=True)
    prj_mgr = models.ForeignKey('PrjMgr', on_delete=models.SET_NULL, null=True)
    summary = models.TextField(max_length=1000, help_text="Enter project description")
    date_created = models.DateField(auto_now=True)
    completion_date = models.DateField(auto_now=False, null=True)

    def get_absolute_url(self):
        """Returns the project number built in to URL for access a particular project instance."""
        return reverse('project-detail', args=[str(self.prj_num)])

    def __str__(self):
        """String for representing the project object."""
        return "Project - " + str(self.prj_num)


class Item(models.Model):
    """Model representing a specific item that can be assigned to project."""
    item_num = models.UUIDField(primary_key=True, default=uuid.uuid4,
                          help_text="Unique ID for this particular item across whole library")
    prj = models.ForeignKey('Project', on_delete=models.SET_NULL, null=True)
    # assigned_to = models.ForeignKey('PrjMgr', on_delete=models.SET_NULL, null=True)

    AVAILABLE = 'A' # Begin STATUS_CHOICES.
    RESERVED = 'R'
    DEPLOYED = 'D'
    STATUS_CHOICES = (
        (AVAILABLE, 'Available'),
        (RESERVED, 'Reserved'),
        (DEPLOYED, 'Deployed'),
    )
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default=AVAILABLE)

    BUILDING_MATL = 'BLD' # Begin DESCRIPTION_CHOICES.
    LIVING = 'LVR'
    KITCHEN = 'KIT'
    BEDROOM = 'BDR'
    BATHROOM = 'BAT'
    CLOTHING = 'CLT'
    OUTDOOR = 'OUT'
    PET_SUPPLIES = 'PET'
    RECREATIONAL = 'REC'
    VEHICLE = 'VEH'
    DESCRIPTION_CHOICES = (
        (BUILDING_MATL, 'Building Materials'),
        (LIVING, 'Living Room'),
        (KITCHEN, 'Kitchen'),
        (BEDROOM, 'Bedroom'),
        (BATHROOM, 'Bathroom'),
        (CLOTHING, 'Clothing'),
        (OUTDOOR, 'Outdoor'),
        (PET_SUPPLIES, 'Pet Supplies'),
        (RECREATIONAL, 'Recreational'),
        (VEHICLE, 'Vehicle'),
    )
    description = models.CharField(max_length=3, choices=DESCRIPTION_CHOICES, default=BUILDING_MATL)

    NORTHWEST = 'NW' # Begin SECTOR_CHOICES.
    NORTHCENTER = 'NC'
    NORTHEAST = 'NE'
    CENTERWEST = 'CW'
    CENTERCENTER = 'CC'
    CENTEREAST = 'CE'
    SOUTHWEST = 'SW'
    SOUTHCENTER = 'SC'
    SOUTHEAST = 'SE'
    SECTOR_CHOICES = (
        (NORTHWEST, 'North-West'),
        (NORTHCENTER, 'North-Center'),
        (NORTHEAST, 'North-East'),
        (CENTERWEST, 'Central-West'),
        (CENTERCENTER, 'Central-Center'),
        (CENTEREAST, 'Central-East'),
        (SOUTHWEST, 'South-West'),
        (SOUTHCENTER, 'South-Center'),
        (SOUTHEAST, 'South-East'),
    )
    sector = models.CharField(max_length=2, choices=SECTOR_CHOICES, default=NORTHWEST)
    notes = models.CharField(max_length=500, default='Notes')
    date_created = models.DateTimeField(auto_now=True)

    def __str__(self):
        """String for representing the item object."""
        return '{0} - {1} -{2}'.format(self.prj.prj_num, self.item_num, self.status)


class PrjMgr(models.Model):
    """Model representing a project manager."""
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    emp_num = models.AutoField(primary_key=True)
    date_of_birth = models.DateField(null=True, blank=True)
    date_joined = models.DateField('joined', null=True, blank=True)

    class Meta:
        ordering = ['last_name', 'first_name']

    def get_absolute_url(self):
        """Returns project manager emp_number built in to URL to access a particular project manager detail view."""
        return reverse('prjmgr-detail', args=[str(self.emp_num)])

    def __str__(self):
        """String for representing the Model object."""
        return '{0}, {1} - {2}'.format(self.last_name, self.first_name, self.emp_num)
