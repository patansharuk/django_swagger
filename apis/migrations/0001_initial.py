# Generated by Django 4.2.11 on 2024-05-02 15:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Showroom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('location', models.CharField(max_length=70)),
            ],
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model_no', models.IntegerField()),
                ('model_name', models.CharField(max_length=70)),
                ('showroom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apis.showroom')),
            ],
        ),
    ]