# Generated by Django 2.2.5 on 2020-03-02 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=150)),
                ('text', models.TextField(db_index=True)),
                ('img', models.CharField(max_length=600)),
                ('link', models.CharField(max_length=200)),
                ('year', models.CharField(max_length=6)),
                ('genre', models.CharField(max_length=50)),
                ('movie_id', models.CharField(max_length=50)),
            ],
        ),
    ]