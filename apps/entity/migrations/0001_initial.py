# Generated by Django 2.2.4 on 2019-09-11 07:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Entity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('business_registration_number', models.CharField(max_length=255, null=True)),
                ('tax_registration_number', models.CharField(max_length=255, null=True)),
                ('address_line1', models.CharField(max_length=255, null=True)),
                ('address_line2', models.CharField(max_length=255, null=True)),
                ('city', models.CharField(max_length=255, null=True)),
                ('state', models.CharField(max_length=255, null=True)),
                ('country', models.CharField(max_length=255, null=True)),
                ('pin_code', models.CharField(max_length=10, null=True)),
                ('deleted', models.BooleanField(default=False)),
                ('is_registered', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_by', models.CharField(max_length=255)),
                ('updated_by', models.CharField(max_length=255, null=True)),
            ],
            options={
                'db_table': 'entity',
            },
        ),
        migrations.CreateModel(
            name='EntityDocument',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content_type', models.CharField(max_length=255, null=True)),
                ('content_url', models.CharField(max_length=255, null=True)),
                ('vimeo_url', models.CharField(max_length=255, null=True)),
                ('name', models.CharField(max_length=255, null=True)),
                ('deleted', models.BooleanField(default=False)),
                ('attachment', models.FileField(null=True, upload_to='')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('created_by', models.CharField(max_length=255)),
                ('updated_by', models.CharField(max_length=255, null=True)),
                ('entity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='entity_documents', to='entity.Entity')),
            ],
            options={
                'db_table': 'entity_documents',
            },
        ),
        migrations.CreateModel(
            name='Entity_Role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(max_length=255)),
                ('user_id', models.CharField(max_length=255)),
                ('deleted', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_by', models.CharField(max_length=255)),
                ('updated_by', models.CharField(max_length=255, null=True)),
                ('entity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='entity_role', to='entity.Entity')),
            ],
            options={
                'db_table': 'entity_role',
                'unique_together': {('role', 'user_id', 'entity')},
            },
        ),
    ]
