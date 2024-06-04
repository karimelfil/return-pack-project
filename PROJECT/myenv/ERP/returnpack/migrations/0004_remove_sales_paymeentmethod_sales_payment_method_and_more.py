# Generated by Django 5.0.6 on 2024-05-27 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('returnpack', '0003_remove_category_description_item_weight_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sales',
            name='paymeentmethod',
        ),
        migrations.AddField(
            model_name='sales',
            name='payment_method',
            field=models.CharField(default='default value', max_length=50),
        ),
        migrations.AlterField(
            model_name='purchase',
            name='amount',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='sales',
            name='amount',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='sales',
            name='currency',
            field=models.CharField(default='default value', max_length=50),
        ),
        migrations.AlterField(
            model_name='sales',
            name='date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='sales',
            name='quantity',
            field=models.IntegerField(),
        ),
    ]