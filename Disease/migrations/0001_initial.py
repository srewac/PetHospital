# Generated by Django 2.0.2 on 2018-03-20 11:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Disease',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='DiseaseExample',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='GeneralProcess',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('desc', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Picture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pic_url', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Process',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('desc', models.CharField(max_length=1000)),
                ('disease_example', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Disease.DiseaseExample')),
            ],
        ),
        migrations.CreateModel(
            name='SubDisease',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('desc', models.CharField(max_length=1000)),
                ('pic_url', models.CharField(blank=True, default=None, max_length=500)),
                ('disease', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Disease.Disease')),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video_url', models.CharField(max_length=500)),
                ('process', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Disease.Process')),
            ],
        ),
        migrations.AddField(
            model_name='picture',
            name='process',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Disease.Process'),
        ),
        migrations.AddField(
            model_name='generalprocess',
            name='sub_disease',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Disease.SubDisease'),
        ),
        migrations.AddField(
            model_name='diseaseexample',
            name='sub_disease',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Disease.SubDisease'),
        ),
    ]
