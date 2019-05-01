# Generated by Django 2.1.7 on 2019-05-01 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resreq', '0014_auto_20190501_1030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalitem',
            name='sector',
            field=models.CharField(choices=[('North-West', 'NW'), ('North-Center', 'NC'), ('North-East', 'NE'), ('Central-West', 'CW'), ('Central-Center', 'CC'), ('Central-East', 'CE'), ('South-West', 'SW'), ('South-Center', 'SC'), ('South-East', 'SE'), ('Off Site', 'OS')], default='NW', max_length=25),
        ),
        migrations.AlterField(
            model_name='item',
            name='sector',
            field=models.CharField(choices=[('North-West', 'NW'), ('North-Center', 'NC'), ('North-East', 'NE'), ('Central-West', 'CW'), ('Central-Center', 'CC'), ('Central-East', 'CE'), ('South-West', 'SW'), ('South-Center', 'SC'), ('South-East', 'SE'), ('Off Site', 'OS')], default='NW', max_length=25),
        ),
    ]
