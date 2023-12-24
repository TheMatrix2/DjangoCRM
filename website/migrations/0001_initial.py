# Generated by Django 4.2.5 on 2023-12-22 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('middle_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=100)),
                ('phone', models.CharField(max_length=15, null=True)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('course_id_1', models.IntegerField(default=0)),
                ('course_id_2', models.IntegerField(default=0)),
                ('course_id_3', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('name_of_teacher', models.CharField(max_length=100)),
                ('number_of_students', models.IntegerField(default=0)),
            ],
        ),
    ]