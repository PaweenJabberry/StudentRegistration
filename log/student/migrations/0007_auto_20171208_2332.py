# Generated by Django 2.0 on 2017-12-08 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0006_department_dep_logo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='Dep_logo',
            field=models.CharField(max_length=500),
        ),
    ]
