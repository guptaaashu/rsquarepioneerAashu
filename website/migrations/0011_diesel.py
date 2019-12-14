# Generated by Django 2.2.7 on 2019-12-14 06:42

import datetime
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0010_auto_20191212_1537'),
    ]

    operations = [
        migrations.CreateModel(
            name='Diesel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('diesel_consumed', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)])),
                ('date', models.DateField(blank=True, default=datetime.datetime.now)),
                ('bus', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bus', to='website.Bus')),
            ],
        ),
    ]
