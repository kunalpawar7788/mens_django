# Generated by Django 3.2.8 on 2021-10-07 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='thumbnail',
            field=models.ImageField(blank=True, max_length=200, null=True, upload_to='uploads/'),
        ),
    ]