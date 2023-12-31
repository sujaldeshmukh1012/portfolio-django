# Generated by Django 4.2.1 on 2023-06-08 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0002_contact_added_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='comment',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='reason',
            field=models.CharField(choices=[('GENERAL', 'General'), ('HIRING', 'Hiring'), ('CONSULT', 'Consult'), ('OTHER', 'Other')], default='JANUARY', max_length=30),
        ),
    ]
