# Generated by Django 3.2.6 on 2021-08-14 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20210813_1029'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='auth_provider',
            field=models.CharField(default='email', max_length=255),
        ),
    ]