# Generated by Django 4.2.1 on 2023-06-09 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0004_alter_contact_comment_alter_contact_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='comment',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.EmailField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='contact',
            name='name',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='contact',
            name='phone',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='contact',
            name='reason',
            field=models.CharField(choices=[('GENERAL', 'General'), ('HIRING', 'Hiring'), ('CONSULT', 'Consult'), ('OTHER', 'Other')], default='JANUARY', max_length=30),
        ),
    ]
