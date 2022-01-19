# Generated by Django 4.0.1 on 2022-01-19 12:15

import autoslug.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0028_order_delivery_order_delivery_time_order_discount_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='coupon',
            name='link',
            field=models.URLField(default='/'),
        ),
        migrations.AddField(
            model_name='order',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=False, null=True, populate_from='no'),
        ),
    ]
