# Generated by Django 4.0.1 on 2022-01-15 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_greeny_link_greeny_owner_alter_product_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(blank=True, default='Fall far this hotel. When describe former fish strong old pass. Particular foot sometimes nearly administration. Rise fear election civil eight. Or human leader between board none against. Not rise leader involve fall.', null=True),
        ),
        migrations.AlterField(
            model_name='reply',
            name='content',
            field=models.TextField(default='Partner experience wish cold heart animal market.'),
        ),
        migrations.AlterField(
            model_name='reply',
            name='name',
            field=models.CharField(default='Melody Moore', max_length=50),
        ),
        migrations.AlterField(
            model_name='review',
            name='content',
            field=models.TextField(default='Actually easy officer. Weight feel same arrive along.'),
        ),
        migrations.AlterField(
            model_name='review',
            name='name',
            field=models.CharField(default='Tim Phelps', max_length=20),
        ),
    ]
