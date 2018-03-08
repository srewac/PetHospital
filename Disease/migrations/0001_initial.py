# Generated by Django 2.0.2 on 2018-03-08 07:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Test', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Disease',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('testpaper', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Test.TestPaper')),
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
                ('desc', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Process',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('desc', models.CharField(max_length=1000)),
                ('pic_url', models.CharField(default=None, max_length=500)),
                ('video_url', models.CharField(default=None, max_length=500)),
                ('disease_example', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Disease.DiseaseExample')),
            ],
        ),
        migrations.CreateModel(
            name='SubDisease',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('desc', models.CharField(max_length=1000)),
                ('pic_url', models.CharField(default=None, max_length=500)),
                ('disease', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Disease.Disease')),
                ('question', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Test.Question')),
            ],
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
