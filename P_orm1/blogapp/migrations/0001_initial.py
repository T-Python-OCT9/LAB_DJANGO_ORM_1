# Generated by Django 4.1.3 on 2022-11-02 21:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=512)),
                ('Content', models.TextField()),
                ('is_published', models.BooleanField()),
                ('publish_data', models.DateTimeField()),
            ],
        ),
    ]
