# Generated by Django 4.2.14 on 2024-08-02 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='worktype',
            name='description',
            field=models.TextField(default=''),
        ),
    ]
