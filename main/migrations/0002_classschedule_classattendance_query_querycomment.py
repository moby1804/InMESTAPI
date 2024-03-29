# Generated by Django 5.0.1 on 2024-02-11 15:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClassSchedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('description', models.TextField(blank=True, null=True)),
                ('state_date_and_time', models.IntegerField()),
                ('end_date_and_time', models.IntegerField()),
                ('is_repeated', models.BooleanField()),
                ('repeat_frequency', models.IntegerField()),
                ('is_active', models.BooleanField()),
                ('organizer', models.CharField(max_length=30)),
                ('venue', models.CharField(max_length=40, null=True)),
                ('cohort', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cohort_schedule', to='users.cohort')),
            ],
        ),
        migrations.CreateModel(
            name='ClassAttendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_present', models.BooleanField()),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('attendee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='attendee_name', to='users.imuser')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='attendance_author', to='users.imuser')),
                ('class_schedule', models.ManyToManyField(related_name='attendance_schedule', to='main.classschedule')),
            ],
        ),
        migrations.CreateModel(
            name='Query',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('description', models.TextField(blank=True, null=True)),
                ('resolution_status', models.CharField(choices=[('PENDING', 'PENDING'), ('IN_PROGRESS', 'IN_PROGRESS'), ('DECLINED', 'DECLINED'), ('RESOLVED', 'RESOLVED')], max_length=30)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('assigned_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assignQuery_user', to='users.imuser')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='query_author', to='users.imuser')),
                ('submitted_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_query', to='users.imuser')),
            ],
        ),
        migrations.CreateModel(
            name='QueryComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=2000)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment_author', to='users.imuser')),
                ('query', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='query_title', to='main.query')),
            ],
        ),
    ]
