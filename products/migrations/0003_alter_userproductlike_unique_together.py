# Generated by Django 3.2.6 on 2021-09-06 22:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
        ('products', '0002_descriptionimage'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='userproductlike',
            unique_together={('user', 'product')},
        ),
    ]
