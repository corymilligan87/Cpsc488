# Generated by Django 2.1.7 on 2019-05-07 02:51

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('resreq', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicalitem',
            name='item_uuid',
            field=models.UUIDField(default=uuid.uuid4),
        ),
        migrations.AddField(
            model_name='item',
            name='item_uuid',
            field=models.UUIDField(default=uuid.uuid4),
        ),
        migrations.AlterField(
            model_name='historicalitem',
            name='item_num',
            field=models.IntegerField(blank=True, db_index=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='item_num',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
