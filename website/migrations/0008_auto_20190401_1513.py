# Generated by Django 2.1.7 on 2019-04-01 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0007_auto_20190325_1707'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='categories',
            field=models.ManyToManyField(related_name='product_category', to='website.Category'),
        ),
    ]
