# Generated by Django 4.0.1 on 2022-01-14 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_product_image_url_alter_product_no'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterModelOptions(
            name='reply',
            options={'verbose_name_plural': 'Replies'},
        ),
        migrations.AddField(
            model_name='instance',
            name='email',
            field=models.EmailField(default='greeny@elishae.me', max_length=254),
        ),
        migrations.AddField(
            model_name='instance',
            name='phone',
            field=models.CharField(default='(+234) 902 515 9360', max_length=50),
        ),
    ]