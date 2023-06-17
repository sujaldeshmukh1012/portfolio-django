# Generated by Django 4.2.1 on 2023-06-09 05:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0010_alter_courseintrest_course_alter_courseintrest_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courseintrest',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.courses'),
        ),
        migrations.AlterField(
            model_name='courseintrest',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='courseintrest',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='courseintrest',
            name='phone_number',
            field=models.IntegerField(null=True),
        ),
    ]
