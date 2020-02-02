# Generated by Django 2.2.5 on 2020-02-02 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0008_announcements'),
    ]

    operations = [
        migrations.CreateModel(
            name='chefuser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('currentrating', models.TextField()),
                ('highestrating', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='forceuser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('currentrating', models.TextField()),
                ('highestrating', models.TextField()),
            ],
        ),
    ]