# Generated by Django 3.2.18 on 2023-05-13 07:02

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0006_article_publish'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='publish',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
