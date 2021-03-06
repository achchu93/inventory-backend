# Generated by Django 3.2.9 on 2021-11-28 10:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('InventoryApp', '0006_auto_20211128_1433'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transfer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('status', models.CharField(choices=[(1, 'Process'), (2, 'Completed'), (3, 'Hold')], max_length=2, null=True)),
                ('note', models.CharField(max_length=255, null=True)),
                ('from_location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='from_location', to='InventoryApp.location')),
            ],
            options={
                'db_table': 'transfer',
            },
        ),
        migrations.CreateModel(
            name='TransferItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('requested_quantity', models.IntegerField()),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='InventoryApp.item')),
                ('transfer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='InventoryApp.transfer')),
            ],
            options={
                'db_table': 'transfer_item',
                'unique_together': {('transfer', 'item')},
            },
        ),
        migrations.AddField(
            model_name='transfer',
            name='items',
            field=models.ManyToManyField(related_name='transfers', through='InventoryApp.TransferItem', to='InventoryApp.Item'),
        ),
        migrations.AddField(
            model_name='transfer',
            name='requested_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='transfer',
            name='to_location',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='to_location', to='InventoryApp.location'),
        ),
    ]
