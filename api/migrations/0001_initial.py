# Generated by Django 3.0.8 on 2021-03-25 01:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=32)),
                ('bio', models.TextField(blank=True, max_length=500, null=True)),
                ('website', models.TextField(blank=True, max_length=100, null=True)),
                ('profile_name', models.TextField(blank=True, max_length=32, null=True)),
                ('gender', models.CharField(max_length=10, null=True)),
                ('birth', models.DateField(blank=True, null=True)),
                ('photo', models.ImageField(null=True, upload_to='profileImages')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]