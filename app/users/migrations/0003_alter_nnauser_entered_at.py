# Generated by Django 4.2.6 on 2024-02-14 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_remove_nnauser_is_tutor_nnauser_tutor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nnauser',
            name='entered_at',
            field=models.DateField(blank=True, null=True),
        ),
    ]
