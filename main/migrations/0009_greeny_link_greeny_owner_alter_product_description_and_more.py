# Generated by Django 4.0.1 on 2022-01-15 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_alter_product_description_alter_reply_content_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='greeny',
            name='link',
            field=models.URLField(default='https://www.elishae.me/'),
        ),
        migrations.AddField(
            model_name='greeny',
            name='owner',
            field=models.CharField(default='Surge', max_length=20),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(blank=True, default='Including instead guess order walk star gas property. Finally role south administration customer service. Red benefit glass miss only deep reduce. Couple whatever foreign cold. Air she blood television movie herself.', null=True),
        ),
        migrations.AlterField(
            model_name='reply',
            name='content',
            field=models.TextField(default='Eight able debate table eat network.'),
        ),
        migrations.AlterField(
            model_name='reply',
            name='name',
            field=models.CharField(default='Sandra Nelson', max_length=50),
        ),
        migrations.AlterField(
            model_name='review',
            name='content',
            field=models.TextField(default='Education image growth environment have phone house. Tough back writer push impact.'),
        ),
        migrations.AlterField(
            model_name='review',
            name='name',
            field=models.CharField(default='Peter Hale', max_length=20),
        ),
    ]