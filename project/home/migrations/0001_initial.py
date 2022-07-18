# Generated by Django 3.1.1 on 2022-07-14 18:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Revenue_District',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dist_code', models.IntegerField(unique=True, verbose_name='District Code')),
                ('dist_name', models.CharField(max_length=30, verbose_name='District Name')),
            ],
        ),
        migrations.CreateModel(
            name='Revenue_Mandal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mandal_code', models.IntegerField(verbose_name='Mandal Code')),
                ('mandal_id', models.IntegerField(verbose_name='Mandal Id')),
                ('mandal_name', models.CharField(max_length=30, verbose_name='Mandal Name')),
                ('dist_code', models.ForeignKey(db_column='dist_code', on_delete=django.db.models.deletion.CASCADE, to='home.revenue_district', to_field='dist_code', verbose_name='District')),
            ],
            options={
                'unique_together': {('dist_code', 'mandal_code')},
            },
        ),
    ]
