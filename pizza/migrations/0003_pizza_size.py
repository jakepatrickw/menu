# Generated by Django 3.0.5 on 2021-04-27 20:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('pizza', '0002_auto_20210427_1334'),
    ]

    operations = [
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Pizza',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topping1', models.CharField(max_length=100)),
                ('topping2', models.CharField(max_length=100)),
                ('size', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pizza.Size')),
            ],
        ),
    ]