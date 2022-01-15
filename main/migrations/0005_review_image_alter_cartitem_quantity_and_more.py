# Generated by Django 4.0.1 on 2022-01-14 19:26

from django.db import migrations, models
import main.models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_category_options_alter_reply_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='image',
            field=models.ImageField(default='profile.jpeg', upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='cartitem',
            name='quantity',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(blank=True, default='Firm clear while game yourself dinner. Myself later country level. Clear west hear model sometimes little building. And it sport policy we thousand for. Third main matter few short woman. During financial town some present next would institution.', null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.CharField(default=main.models.generate_price, max_length=20),
        ),
        migrations.AlterField(
            model_name='product',
            name='tags',
            field=models.CharField(default='organic, raw, processed, inorganic', help_text='seperate tags with a comma and single space', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='reply',
            name='content',
            field=models.TextField(default='South job player just house wife.'),
        ),
        migrations.AlterField(
            model_name='reply',
            name='name',
            field=models.CharField(default='Bethany Phillips', max_length=50),
        ),
        migrations.AlterField(
            model_name='review',
            name='content',
            field=models.TextField(default='Name detail later I church join sell agency. In finish radio though glass right.'),
        ),
        migrations.AlterField(
            model_name='review',
            name='name',
            field=models.CharField(default='Emily Williams', max_length=20),
        ),
        migrations.AlterField(
            model_name='review',
            name='rating',
            field=models.PositiveSmallIntegerField(default=main.models.generate_rating),
        ),
        migrations.AlterField(
            model_name='variant',
            name='price',
            field=models.DecimalField(decimal_places=2, default=main.models.generate_price, max_digits=7),
        ),
    ]