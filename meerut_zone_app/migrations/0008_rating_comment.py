# Generated by Django 5.0.6 on 2024-05-26 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meerut_zone_app', '0007_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='rating',
            name='comment',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]
