# Generated by Django 2.2.2 on 2022-03-29 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BookInfo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('bname', models.CharField(max_length=100)),
                ('bdate', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]