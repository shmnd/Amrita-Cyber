# Generated by Django 5.1.5 on 2025-02-05 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EvaluationRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('input_prompt', models.TextField(blank=True, null=True)),
                ('status', models.CharField(blank=True, choices=[('Pending', 'Pending'), ('Completed', 'Completed')], default='Pending', max_length=20, null=True)),
                ('result', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
    ]
