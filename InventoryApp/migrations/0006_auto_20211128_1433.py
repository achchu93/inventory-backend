# Generated by Django 3.2.9 on 2021-11-28 09:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('InventoryApp', '0005_auto_20211120_0959'),
    ]

    operations = [
        migrations.CreateModel(
            name='InventoryReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('started_at', models.DateTimeField()),
                ('closed_at', models.DateTimeField(null=True)),
                ('status', models.CharField(choices=[(1, 'Process'), (2, 'Completed'), (3, 'Hold')], max_length=2)),
                ('closed_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='closed_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'inventory_report',
            },
        ),
        migrations.CreateModel(
            name='InventoryReportItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('inventory_report', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='InventoryApp.inventoryreport')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='InventoryApp.item')),
            ],
            options={
                'db_table': 'inventory_report_item',
                'unique_together': {('inventory_report', 'item')},
            },
        ),
        migrations.AddField(
            model_name='inventoryreport',
            name='items',
            field=models.ManyToManyField(related_name='inventory_reports', through='InventoryApp.InventoryReportItem', to='InventoryApp.Item'),
        ),
        migrations.AddField(
            model_name='inventoryreport',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='InventoryApp.location'),
        ),
        migrations.AddField(
            model_name='inventoryreport',
            name='started_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='started_by', to=settings.AUTH_USER_MODEL),
        ),
    ]
