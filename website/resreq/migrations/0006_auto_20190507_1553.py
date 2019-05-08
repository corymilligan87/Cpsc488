# Generated by Django 2.1.7 on 2019-05-07 19:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('resreq', '0005_auto_20190507_1452'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalitem',
            name='prj',
            field=models.ForeignKey(blank=True, db_constraint=False, default=0, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='resreq.Project'),
        ),
        migrations.AlterField(
            model_name='item',
            name='prj',
            field=models.ForeignKey(default=0, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='items', to='resreq.Project'),
        ),
        migrations.AlterField(
            model_name='project',
            name='prj_mgr',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='projects', to='resreq.PrjMgr'),
        ),
    ]
