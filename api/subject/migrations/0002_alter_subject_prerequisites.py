# Generated by Django 5.1.3 on 2024-11-23 03:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subject', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='prerequisites',
            field=models.ManyToManyField(blank=True, db_constraint=False, related_name='required_by', to='subject.subject'),
        ),
    ]