# Generated by Django 5.0.1 on 2024-02-11 14:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cohort',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('description', models.TextField(blank=True, null=True)),
                ('year', models.IntegerField(default=2024)),
                ('start_date', models.DateTimeField(blank=True, null=True)),
                ('end_date', models.DateTimeField(blank=True, null=True)),
                ('is_active', models.BooleanField()),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modeified', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='IMuser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=40)),
                ('last_name', models.CharField(max_length=40)),
                ('is_active', models.BooleanField()),
                ('user_type', models.CharField(choices=[('EIT', 'EIT'), ('TEACHING_FELLOW', 'TEACHING_FELLOW'), ('ADMIN_STAFF', 'ADMIN_STAFF'), ('ADMIN', 'ADMIN')], max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='CohortMember',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField()),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modeified', models.DateTimeField(auto_now=True)),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cohort_name', to='users.cohort')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='member_user_type', to='users.imuser')),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cohort_member', to='users.imuser')),
            ],
        ),
        migrations.AddField(
            model_name='cohort',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='author_name', to='users.imuser'),
        ),
    ]