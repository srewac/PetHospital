# Generated by Django 2.0.2 on 2018-03-20 11:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Disease', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=100)),
                ('correct', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=1000)),
                ('score', models.IntegerField(default=2)),
                ('sub_disease', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Disease.SubDisease')),
            ],
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('duration', models.IntegerField(default=60)),
                ('close_time', models.DateTimeField(verbose_name='close date')),
            ],
        ),
        migrations.CreateModel(
            name='TestPaper',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('desc', models.CharField(max_length=1000)),
                ('disease', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Disease.Disease')),
            ],
        ),
        migrations.CreateModel(
            name='TestPaper_Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Test.Question')),
                ('testpaper', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Test.TestPaper')),
            ],
        ),
        migrations.AddField(
            model_name='testpaper',
            name='testpaper_with_question',
            field=models.ManyToManyField(through='Test.TestPaper_Question', to='Test.Question'),
        ),
        migrations.AddField(
            model_name='test',
            name='test_paper',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Test.TestPaper'),
        ),
        migrations.AddField(
            model_name='choice',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Test.Question'),
        ),
    ]
