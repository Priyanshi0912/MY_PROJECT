# Generated by Django 4.0.5 on 2022-07-27 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GroupApp', '0002_sheet_nameofsheet'),
    ]

    operations = [
        migrations.AddField(
            model_name='content',
            name='userName',
            field=models.CharField(default=12, max_length=50),
            preserve_default=False,
        ),
    ]