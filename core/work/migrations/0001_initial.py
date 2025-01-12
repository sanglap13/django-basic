# Generated by Django 4.2.14 on 2024-08-02 07:08

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='workType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='workType/')),
                ('date_added', models.DateTimeField(default=django.utils.timezone.now)),
                ('work_type', models.CharField(choices=[('Web', 'Web Development'), ('Mob', 'Mobile Development'), ('UX', 'UI/UX Design'), ('DM', 'Digital Marketing'), ('CW', 'Content Writing'), ('GD', 'Graphic Design')], max_length=3)),
            ],
        ),
    ]
