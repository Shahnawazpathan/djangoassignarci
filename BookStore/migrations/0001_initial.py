# Generated by Django 4.2.6 on 2023-10-11 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=30)),
                ('published_date', models.DateField()),
                ('isbn_number', models.CharField(max_length=50)),
                ('page_count', models.IntegerField()),
                ('cover_image', models.ImageField(upload_to='cover_image')),
                ('language', models.CharField(max_length=50)),
            ],
        ),
    ]
