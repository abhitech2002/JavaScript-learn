# Generated by Django 5.1.2 on 2024-10-26 09:59

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('world', '0002_chaivarity_description'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ChaiCertificate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('certificate_number', models.CharField(max_length=100)),
                ('issued_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('valid_untill', models.DateTimeField()),
                ('chai', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='certificate', to='world.chaivarity')),
            ],
        ),
        migrations.CreateModel(
            name='ChaiReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField()),
                ('comment', models.TextField()),
                ('date_added', models.DateTimeField(default=django.utils.timezone.now)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to=settings.AUTH_USER_MODEL)),
                ('chai', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='world.chaivarity')),
            ],
        ),
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('location', models.CharField(default='', max_length=100)),
                ('ChaiVarity', models.ManyToManyField(blank=True, related_name='stores', to='world.chaivarity')),
            ],
        ),
    ]