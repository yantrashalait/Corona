# Generated by Django 2.2.9 on 2020-03-22 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AapatKalinSewa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=255)),
                ('phone_number', models.CharField(max_length=255)),
                ('contact_person_or_institute', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('source', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='news/')),
                ('date_added', models.CharField(max_length=255)),
                ('long_description', models.TextField()),
                ('short_description', models.TextField()),
            ],
        ),
    ]