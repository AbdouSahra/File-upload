# Generated by Django 3.1.2 on 2021-02-01 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('editor', models.CharField(max_length=100)),
                ('upload_date', models.DateTimeField(auto_now_add=True)),
                ('file', models.FileField(upload_to='files/zip')),
            ],
        ),
    ]