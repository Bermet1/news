# Generated by Django 3.2.8 on 2021-10-31 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='link',
            field=models.URLField(default=1, max_length=250),
            preserve_default=False,
        ),
    ]
