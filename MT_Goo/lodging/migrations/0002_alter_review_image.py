# Generated by Django 4.2.3 on 2023-08-06 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lodging', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='image',
            field=models.ImageField(null=True, upload_to='review/'),
        ),
    ]
