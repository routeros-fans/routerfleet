# Generated by Django 5.0.3 on 2024-04-03 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ExternalIntegration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('integration_type', models.CharField(choices=[('wireguard_webadmin', 'WireGuard WebAdmin')], max_length=100)),
                ('integration_url', models.URLField()),
                ('wireguard_webadmin_default_user_level', models.PositiveIntegerField(choices=[(10, 'Debugging Analyst'), (20, 'View Only User'), (30, 'Peer Manager'), (40, 'Manager'), (50, 'Administrator')], default=0)),
                ('token', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]