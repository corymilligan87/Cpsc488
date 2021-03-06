# Generated by Django 2.1.7 on 2019-05-07 19:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('resreq', '0006_auto_20190507_1553'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalitem',
            name='prj',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='resreq.Project'),
        ),
        migrations.AlterField(
            model_name='item',
            name='prj',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='items', to='resreq.Project'),
        ),
    ]
