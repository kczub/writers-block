# Generated by Django 4.0.3 on 2022-03-10 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_remove_post_updated_post_published_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='pub_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='date published'),
        ),
    ]
