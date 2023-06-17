# Generated by Django 4.2.1 on 2023-06-06 12:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_courses_deadline_for_pricedrop_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseIntrest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('date_added', models.DateTimeField()),
                ('phone_number', models.IntegerField(null=True)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.courses')),
            ],
        ),
    ]