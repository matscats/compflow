# Generated by Django 5.1.3 on 2024-12-05 20:35

import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('subject', '0002_alter_subject_prerequisites'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('period', models.CharField(max_length=6, validators=[django.core.validators.RegexValidator(message="O formato deve ser 'NNNN.N', onde N é um número e o dígito após o ponto deve ser 1 ou 2.", regex='^\\d{4}\\.[12]$')])),
                ('subjects', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='schedules', to='subject.subject')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='schedules', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('user', 'period')},
            },
        ),
    ]
