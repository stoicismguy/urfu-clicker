# Generated by Django 4.2.6 on 2024-06-02 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0003_core_autoclick_power'),
    ]

    operations = [
        migrations.AddField(
            model_name='boost',
            name='name',
            field=models.CharField(default='Безымянный препарат', max_length=50),
        ),
    ]