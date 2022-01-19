# Generated by Django 4.0.1 on 2022-01-19 08:44

from django.db import migrations, models
import main.models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0022_alter_brand_rating_count_alter_product_description_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='status',
            field=models.CharField(choices=[('stock in', 'Stock In'), ('stock out', 'Stock Out')], default='stock in', max_length=9),
        ),
        migrations.AlterField(
            model_name='testimonial',
            name='rating',
            field=models.IntegerField(default=5, validators=[main.models.validate_rating]),
        ),
    ]
