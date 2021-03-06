# Generated by Django 4.0.1 on 2022-01-16 18:59

from django.db import migrations, models
import main.models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_product_label_product_labelclass_product_labelcolor_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='rating',
            field=models.PositiveSmallIntegerField(default=main.models.generate_rating, validators=[main.models.validate_rating]),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(blank=True, default='Everybody next between behind enjoy when skill take. Various success election enough. This reduce over.', null=True),
        ),
        migrations.AlterField(
            model_name='reply',
            name='content',
            field=models.TextField(default='Hospital against read to outside situation.'),
        ),
        migrations.AlterField(
            model_name='reply',
            name='name',
            field=models.CharField(default='Tanya Carroll', max_length=50),
        ),
        migrations.AlterField(
            model_name='review',
            name='content',
            field=models.TextField(default='Music land it allow life. Idea already expert full still activity personal message.'),
        ),
        migrations.AlterField(
            model_name='review',
            name='name',
            field=models.CharField(default='Jennifer Herrera', max_length=20),
        ),
        migrations.AlterField(
            model_name='review',
            name='rating',
            field=models.PositiveSmallIntegerField(default=main.models.generate_rating, validators=[main.models.validate_rating]),
        ),
    ]
