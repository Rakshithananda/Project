# Generated by Django 3.1.1 on 2022-07-29 19:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='revenue_gsws',
            old_name='GSWS_name',
            new_name='gsws_name',
        ),
    ]