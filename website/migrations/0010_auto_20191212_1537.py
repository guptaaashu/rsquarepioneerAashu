# Generated by Django 2.2.7 on 2019-12-12 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0009_auto_20191212_1338'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pbsuser',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='profiles'),
        ),
    ]
