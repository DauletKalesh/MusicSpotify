# Generated by Django 3.1.7 on 2022-05-01 21:07

from django.db import migrations, models
import django.db.models.deletion
import utils.upload
import utils.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Albums',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': 'Album',
                'verbose_name_plural': 'Albums',
            },
        ),
        migrations.CreateModel(
            name='Artists',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Artist',
                'verbose_name_plural': 'Artists',
            },
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Genre',
                'verbose_name_plural': 'Genres',
            },
        ),
        migrations.CreateModel(
            name='Tracks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('track_name', models.CharField(max_length=255)),
                ('release_date', models.DateField()),
                ('category', models.SmallIntegerField(blank=True, choices=[(0, 'At home'), (1, 'Gaming'), (2, 'Workout'), (3, 'Party'), (4, 'Kids&Family')], null=True)),
                ('searched_num', models.BigIntegerField(blank=True, null=True)),
                ('duration', models.TimeField(blank=True, null=True)),
                ('music_doc', models.FileField(upload_to=utils.upload.track_document_path, validators=[utils.validators.validate_track_format, utils.validators.validate_track_size])),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.albums')),
                ('genre', models.ManyToManyField(related_name='Genres', to='main.Genre')),
            ],
            options={
                'verbose_name': 'Track',
                'verbose_name_plural': 'Tracks',
            },
        ),
        migrations.AddField(
            model_name='albums',
            name='artist',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.artists'),
        ),
    ]
