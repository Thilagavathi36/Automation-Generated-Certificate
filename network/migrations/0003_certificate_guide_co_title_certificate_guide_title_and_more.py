# Generated by Django 5.1.2 on 2024-10-24 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0002_certificate_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='certificate',
            name='guide_co_title',
            field=models.CharField(choices=[('Mr.', 'Mr.'), ('Ms.', 'Ms.'), ('Mrs.', 'Mrs.')], default='Mr.', max_length=5),
        ),
        migrations.AddField(
            model_name='certificate',
            name='guide_title',
            field=models.CharField(choices=[('Mr.', 'Mr.'), ('Ms.', 'Ms.'), ('Mrs.', 'Mrs.')], default='Mr.', max_length=5),
        ),
        migrations.AddField(
            model_name='certificate',
            name='name_title',
            field=models.CharField(choices=[('Mr.', 'Mr.'), ('Ms.', 'Ms.'), ('Mrs.', 'Mrs.')], default='Mr.', max_length=5),
        ),
    ]
