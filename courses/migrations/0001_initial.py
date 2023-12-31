# Generated by Django 4.2.1 on 2023-06-05 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('duration', models.CharField(max_length=100)),
                ('tutor', models.CharField(max_length=100)),
                ('poster', models.ImageField(upload_to='courses-poster')),
                ('roadmap', models.TextField()),
                ('technology', models.TextField()),
                ('created_on', models.DateTimeField()),
                ('starts_on', models.DateField()),
            ],
        ),
    ]
