# Generated by Django 2.1.7 on 2019-03-12 08:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actors',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=150)),
                ('last_name', models.CharField(max_length=150)),
                ('birthdate', models.DateField()),
                ('sex', models.CharField(choices=[('male', 'MALE'), ('female', 'FEMALE'), ('other', 'OTHER')], default='male', max_length=6)),
                ('nationality', models.CharField(max_length=150)),
                ('is_alive', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Awards',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Movies',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('description', models.TextField()),
                ('release_date', models.DateField()),
                ('logo', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('actors', models.ManyToManyField(blank=True, to='movies.Actors')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.Categories')),
            ],
        ),
    ]
