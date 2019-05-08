from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
import uuid
from simple_history.models import HistoricalRecords


class Project(models.Model):
    """Model representing a project."""
    prj_num = models.AutoField(primary_key=True)
    prj_mgr = models.ForeignKey('PrjMgr', related_name='projects', on_delete=models.SET_NULL, null=True, blank=True)
    summary = models.TextField(max_length=1000, help_text="Enter project description", null=True, blank=True)
    date_created = models.DateField(auto_now=True)
    completion_date = models.DateField(null=True, blank=True)
    history = HistoricalRecords()

    PROJECT_STATUS = (
        ('Behind Schedule', 'Behind Schedule'),
        ('Complete', 'Complete'),
        ('In Progress', 'In Progress'),
        ('Scheduled', 'Scheduled'),
        ('Planning', 'Planning'),
    )
    prj_status = models.TextField(
        max_length=12,
        choices=PROJECT_STATUS,
        default='Planning'
    )

    def get_absolute_url(self):
        """Returns the project number built in to URL for access a particular project instance."""
        return reverse('project-detail', args=[str(self.prj_num)])

    def __str__(self):
        """String for representing the project object."""
        return 'Prj Num: {0} -  Prj Mgr: {1} - Prj Status: {2} - Wrap Date: {3}' \
            .format(self.prj_num,
                    self.prj_mgr,
                    self.prj_status,
                    self.completion_date,
                    )


class Item(models.Model):
    """Model representing a specific item that can be assigned to a project."""
    item_num = models.AutoField(primary_key=True)
    item_uuid = models.UUIDField(default=uuid.uuid4)
    prj = models.ForeignKey('Project', related_name='items', on_delete=models.SET_NULL, null=True, blank=True)
    notes = models.CharField(max_length=500, blank=True)
    date_added = models.DateField(null=True, blank=True)
    history = HistoricalRecords()

    ITEM_STATUS = (
        ('Available', 'Available'),
        ('Reserved', 'Reserved'),
        ('Deployed', 'Deployed'),
    )
    status = models.TextField(
        max_length=25,
        choices=ITEM_STATUS,
        default='Available',
    )

    ITEM_DESCRIPTION = (
        ('Building Materials', 'Building Materials'),
        ('Living Room', 'Living Room'),
        ('Kitchen', 'Kitchen'),
        ('Bedroom', 'Bedroom'),
        ('Bathroom', 'Bathroom'),
        ('Clothing', 'Clothing'),
        ('Outdoor', 'Outdoor'),
        ('Pet Supplies', 'Pet Supplies'),
        ('Recreational', 'Recreational'),
        ('Vehicle', 'Vehicle'),
    )
    description = models.TextField(
        max_length=25,
        choices=ITEM_DESCRIPTION,
        default='Outdoor'
    )

    ITEM_SECTOR = (
        ('North-West', 'NW'),
        ('North-Center', 'NC'),
        ('North-East', 'NE'),
        ('Central-West', 'CW'),
        ('Central-Center', 'CC'),
        ('Central-East', 'CE'),
        ('South-West', 'SW'),
        ('South-Center', 'SC'),
        ('South-East', 'SE'),
        ('Off Site', 'OS'),
    )
    sector = models.CharField(
        max_length=25,
        choices=ITEM_SECTOR, default='NW'
    )

    def update_item_status(self):
        """Updates status assigned to project"""
        if self.prj:
            self.status = 'Reserved'

    def get_absolute_url(self):
        """Returns the project number built in to URL for access a particular project instance."""
        return reverse('item-detail', args=[str(self.item_num)])

    def __str__(self):
        """String for representing the item object."""
        if not self.prj:
            return 'Item Number: {0} -  Project Number: {1} - Status: {2} - Inventory Sector: {3} - Description: {4}' \
                .format(self.item_num,
                        "None",
                        self.status,
                        self.sector,
                        self.description)
        else:
            return 'Item Number: {0} -  Project Number: {1} - Status: {2} - Inventory Sector: {3} - Description: {4}' \
                .format(self.item_num,
                        self.prj.prj_num,
                        self.status,
                        self.sector,
                        self.description)


class PrjMgr(models.Model):
    """Model representing a project manager."""
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    emp_num = models.AutoField(primary_key=True)
    date_of_birth = models.DateField(null=True, blank=True)
    date_joined = models.DateField('joined', null=True, blank=True)
    history = HistoricalRecords()

    PRJMGR_ROLE = (
        ('Project Manager I', 'Project Manager I'),
        ('Project Manager II', 'Project Manager II'),
        ('Project Manager III', 'Project Manager III'),
        ('Project Planner', 'Project Planner'),
        ('Project Coordinator', 'Project Coordinator'),
        ('Supervisor', 'Supervisor'),
    )
    role = models.CharField(
        max_length=25,
        choices=PRJMGR_ROLE, default='Project Manager I'
    )

    class Meta:
        ordering = ['last_name', 'first_name']

    def get_absolute_url(self):
        """Returns project manager emp_number built in to URL to access a particular project manager detail view."""
        return reverse('prjmgr-detail', args=[str(self.emp_num)])

    def __str__(self):
        """String for representing the Model object."""
        return '{0} {1} - Role: {2} '.format(self.first_name, self.last_name, self.role, self.emp_num)
