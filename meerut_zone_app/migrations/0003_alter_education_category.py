# Generated by Django 5.0.6 on 2024-05-18 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meerut_zone_app', '0002_alter_hospital_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='education',
            name='category',
            field=models.CharField(choices=[('Govt-School', 'Govt-School'), ('CBSE Board School', 'CBSE Board School'), ('ICSE Board School', 'ICSE Board School'), ('College', 'College'), ('University', 'University')], max_length=200),
        ),
    ]
