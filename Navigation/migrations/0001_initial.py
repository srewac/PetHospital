# Generated by Django 2.0.2 on 2018-03-15 11:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('desc', models.CharField(max_length=1000)),
                ('pic_url', models.CharField(blank=True, default=None, max_length=500)),
                ('video_url', models.CharField(blank=True, default=None, max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Room_Role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Navigation.Role')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Navigation.Room')),
            ],
        ),
        migrations.AddField(
            model_name='room',
            name='room_with_role',
            field=models.ManyToManyField(through='Navigation.Room_Role', to='Navigation.Role'),
        ),
    ]
