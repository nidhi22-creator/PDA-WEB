# Generated by Django 2.2.4 on 2019-09-11 07:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('entity', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Program',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=260)),
                ('deleted', models.BooleanField(default=False)),
                ('active', models.BooleanField(default=True)),
                ('description', models.TextField()),
                ('start_date', models.DateField(blank=True, null=True)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('created_by', models.CharField(max_length=255)),
                ('updated_by', models.CharField(max_length=255, null=True)),
                ('entity', models.ForeignKey(default=31, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='programs', to='entity.Entity')),
            ],
            options={
                'db_table': 'program',
            },
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('deleted', models.BooleanField(default=False)),
                ('active', models.BooleanField(default=False)),
                ('description', models.TextField(blank=True, null=True)),
                ('is_session_linked', models.BooleanField(default=False)),
                ('session_linked', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('created_by', models.CharField(max_length=255)),
                ('updated_by', models.CharField(max_length=255, null=True)),
                ('program', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='topics', to='program.Program')),
            ],
            options={
                'db_table': 'topic',
            },
        ),
        migrations.CreateModel(
            name='ProgramDocument',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, null=True)),
                ('deleted', models.BooleanField(default=False)),
                ('content_type', models.CharField(max_length=255, null=True)),
                ('content_url', models.CharField(max_length=255, null=True)),
                ('vimeo_url', models.CharField(max_length=255, null=True)),
                ('attachment', models.FileField(null=True, upload_to='')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('created_by', models.CharField(max_length=255)),
                ('updated_by', models.CharField(max_length=255, null=True)),
                ('program', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='documents', to='program.Program')),
            ],
            options={
                'db_table': 'program_documents',
            },
        ),
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, null=True)),
                ('deleted', models.BooleanField(default=False)),
                ('active', models.BooleanField(default=False)),
                ('content_type', models.CharField(max_length=255, null=True)),
                ('content_url', models.CharField(max_length=255, null=True)),
                ('vimeo_url', models.CharField(max_length=255, null=True)),
                ('attachment', models.FileField(null=True, upload_to='')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('created_by', models.CharField(max_length=255)),
                ('updated_by', models.CharField(max_length=255, null=True)),
                ('topic', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='contents', to='program.Topic')),
            ],
            options={
                'db_table': 'content',
            },
        ),
        migrations.CreateModel(
            name='Program_Roles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(max_length=255)),
                ('user_id', models.CharField(max_length=255)),
                ('deleted', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('created_by', models.CharField(max_length=255)),
                ('updated_by', models.CharField(max_length=255, null=True)),
                ('program', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='program_roles', to='program.Program')),
            ],
            options={
                'db_table': 'program_roles',
                'unique_together': {('role', 'user_id', 'program')},
            },
        ),
        migrations.CreateModel(
            name='Eligible_Program_Admin',
            fields=[
                ('user_id', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField()),
                ('deleted', models.BooleanField(default=False)),
                ('updated_at', models.DateField(auto_now=True, null=True)),
                ('entity', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='eligible_program_admin', to='entity.Entity')),
            ],
            options={
                'db_table': 'eligible_program_admin',
                'unique_together': {('user_id', 'entity')},
            },
        ),
    ]
