# Generated by Django 2.1.7 on 2019-05-01 05:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ('resreq', '0005_auto_20190501_0059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='prj_mgr',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='resreq.PrjMgr'),
        ),
    ]
