# Generated by Django 4.0.4 on 2023-02-26 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('screens_app', '0003_evaluation'),
    ]

    operations = [
        migrations.AddField(
            model_name='evaluation',
            name='course_Id',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
