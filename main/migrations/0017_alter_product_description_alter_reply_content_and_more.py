# Generated by Django 4.0.1 on 2022-01-18 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_category_image_category_product_count_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(blank=True, default='Occur heavy fear sell relationship nice. Election foot glass something address him. Often dog hope respond window story effort road. Action exactly player without.', null=True),
        ),
        migrations.AlterField(
            model_name='reply',
            name='content',
            field=models.TextField(default='Class hard one trade where.'),
        ),
        migrations.AlterField(
            model_name='reply',
            name='name',
            field=models.CharField(default='Christopher Carey', max_length=50),
        ),
        migrations.AlterField(
            model_name='review',
            name='content',
            field=models.TextField(default='Support dream chair drug first about change.'),
        ),
        migrations.AlterField(
            model_name='review',
            name='name',
            field=models.CharField(default='Shelby King', max_length=20),
        ),
        migrations.AlterField(
            model_name='teammember',
            name='name',
            field=models.CharField(default='Juan Baxter', max_length=20),
        ),
        migrations.AlterField(
            model_name='testimonial',
            name='content',
            field=models.TextField(default='Itself TV water loss.'),
        ),
        migrations.AlterField(
            model_name='testimonial',
            name='name',
            field=models.CharField(default='Sophia Harding', max_length=20),
        ),
    ]