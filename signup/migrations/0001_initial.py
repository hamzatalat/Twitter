# Generated by Django 3.0.dev20190710083734 on 2019-07-12 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SignUpData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_text', models.CharField(max_length=200)),
                ('email_text', models.CharField(max_length=200)),
                ('password_text', models.CharField(max_length=200)),
            ],
        ),
    ]
