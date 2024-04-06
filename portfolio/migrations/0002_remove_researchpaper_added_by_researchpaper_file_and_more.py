# Generated by Django 4.2.11 on 2024-03-31 06:45

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='researchpaper',
            name='added_by',
        ),
        migrations.AddField(
            model_name='researchpaper',
            name='file',
            field=models.FileField(default='', upload_to='research_papers/'),
        ),
        migrations.AddField(
            model_name='researchpaper',
            name='publication_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='researchpaper',
            name='title',
            field=models.CharField(max_length=200),
        ),
    ]