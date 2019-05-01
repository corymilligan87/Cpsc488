# Generated by Django 2.1.7 on 2019-05-01 05:13

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('resreq', '0006_auto_20190501_0101'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalitem',
            name='description',
            field=models.CharField(
                choices=[('Building Materials', 'Building Materials'), ('Living Room', 'Living Room'),
                         ('Kitchen', 'Kitchen'), ('Bedroom', 'Bedroom'), ('Bathroom', 'Bathroom'),
                         ('Clothing', 'Clothing'), ('Outdoor', 'Outdoor'), ('Pet Supplies', 'Pet Supplies'),
                         ('Recreational', 'Recreational'), ('Vehicle', 'Vehicle')], default='BLDG', max_length=4),
        ),
        migrations.AlterField(
            model_name='historicalitem',
            name='sector',
            field=models.CharField(
                choices=[('North-West', 'North-West'), ('North-West', 'North-Center'), ('North-West', 'North-East'),
                         ('Central-West', 'Central-West'), ('Central-Center', 'Central-Center'),
                         ('Central-East', 'Central-East'), ('South-West', 'South-West'),
                         ('South-Center', 'South-Center'), ('South-East', 'South-East'), ('Off Site', 'Off site')],
                default='North-West', max_length=14),
        ),
        migrations.AlterField(
            model_name='historicalitem',
            name='status',
            field=models.CharField(
                choices=[('Available', 'Available'), ('Reserved', 'Reserved'), ('Deployed', 'Deployed')],
                default='Available', max_length=9),
        ),
        migrations.AlterField(
            model_name='historicalprjmgr',
            name='role',
            field=models.CharField(
                choices=[('Project Manager I', 'Project Manager I'), ('Project Manager II', 'Project Manager II'),
                         ('Project Manager III', 'Project Manager III'), ('Project Planner', 'Project Planner'),
                         ('Project Coordinator', 'Project Coordinator'), ('Supervisor', 'Supervisor')],
                default='Project Manager I', max_length=25),
        ),
        migrations.AlterField(
            model_name='historicalproject',
            name='prj_status',
            field=models.TextField(choices=[('Complete', 'Complete'), ('Behind Schedule', 'Behind Schedule'),
                                            ('In Progress', 'In Progress'), ('Planning', 'Planning'),
                                            ('Scheduled', 'Scheduled')], default='Scheduled', max_length=12),
        ),
        migrations.AlterField(
            model_name='item',
            name='description',
            field=models.CharField(
                choices=[('Building Materials', 'Building Materials'), ('Living Room', 'Living Room'),
                         ('Kitchen', 'Kitchen'), ('Bedroom', 'Bedroom'), ('Bathroom', 'Bathroom'),
                         ('Clothing', 'Clothing'), ('Outdoor', 'Outdoor'), ('Pet Supplies', 'Pet Supplies'),
                         ('Recreational', 'Recreational'), ('Vehicle', 'Vehicle')], default='BLDG', max_length=4),
        ),
        migrations.AlterField(
            model_name='item',
            name='sector',
            field=models.CharField(
                choices=[('North-West', 'North-West'), ('North-West', 'North-Center'), ('North-West', 'North-East'),
                         ('Central-West', 'Central-West'), ('Central-Center', 'Central-Center'),
                         ('Central-East', 'Central-East'), ('South-West', 'South-West'),
                         ('South-Center', 'South-Center'), ('South-East', 'South-East'), ('Off Site', 'Off site')],
                default='North-West', max_length=14),
        ),
        migrations.AlterField(
            model_name='item',
            name='status',
            field=models.CharField(
                choices=[('Available', 'Available'), ('Reserved', 'Reserved'), ('Deployed', 'Deployed')],
                default='Available', max_length=9),
        ),
        migrations.AlterField(
            model_name='prjmgr',
            name='role',
            field=models.CharField(
                choices=[('Project Manager I', 'Project Manager I'), ('Project Manager II', 'Project Manager II'),
                         ('Project Manager III', 'Project Manager III'), ('Project Planner', 'Project Planner'),
                         ('Project Coordinator', 'Project Coordinator'), ('Supervisor', 'Supervisor')],
                default='Project Manager I', max_length=25),
        ),
        migrations.AlterField(
            model_name='project',
            name='prj_status',
            field=models.TextField(choices=[('Complete', 'Complete'), ('Behind Schedule', 'Behind Schedule'),
                                            ('In Progress', 'In Progress'), ('Planning', 'Planning'),
                                            ('Scheduled', 'Scheduled')], default='Scheduled', max_length=12),
        ),
    ]
