# Generated by Django 3.2.9 on 2021-11-18 08:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('InventoryApp', '0003_auto_20211117_1508'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('quantity', models.IntegerField(null=True)),
                ('last_bought_price', models.FloatField(null=True)),
                ('order_by', models.DateTimeField(null=True)),
                ('file_name', models.CharField(max_length=255, null=True)),
                ('status', models.CharField(choices=[(1, 'Active'), (0, 'Inactive')], max_length=2)),
            ],
            options={
                'db_table': 'item',
            },
        ),
        migrations.CreateModel(
            name='ItemCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'item_category',
            },
        ),
        migrations.CreateModel(
            name='Sku',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sku', models.CharField(max_length=255)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='InventoryApp.item')),
            ],
            options={
                'db_table': 'sku',
            },
        ),
        migrations.AddField(
            model_name='item',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='InventoryApp.itemcategory'),
        ),
    ]
