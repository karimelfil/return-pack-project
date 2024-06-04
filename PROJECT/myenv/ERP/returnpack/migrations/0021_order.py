# Generated by Django 5.0.6 on 2024-05-30 05:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('returnpack', '0020_alter_warehouse_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_date', models.DateField(default='default value')),
                ('notes', models.CharField(default='no notes ', max_length=100)),
                ('item_price', models.FloatField()),
                ('returnablepackage_price', models.FloatField()),
                ('status', models.CharField(default='Pending', max_length=10)),
                ('order_number', models.CharField(default='unkown order', max_length=20)),
                ('shipping_address', models.CharField(default='self pickup', max_length=30)),
                ('total_amount', models.FloatField()),
                ('payment_method', models.CharField(default='cash', max_length=20)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='returnpack.customer')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='returnpack.item')),
                ('packaging', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='returnpack.packaging')),
            ],
        ),
    ]
