# Generated by Django 3.2.18 on 2023-05-13 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0009_remove_article_publish'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='publish',
            field=models.DateField(blank=True, null=True),
        ),
    ]