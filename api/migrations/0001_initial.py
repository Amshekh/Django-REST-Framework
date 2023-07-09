# Generated by Django 4.2 on 2023-07-06 16:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('company_id', models.AutoField(primary_key=True, serialize=False)),
                ('company_name', models.CharField(max_length=75)),
                ('company_location', models.CharField(max_length=75)),
                ('company_type', models.CharField(choices=[('IT', 'IT'), ('Non IT', 'Non IT'), ('SaaS', 'SaaS'), ('CSP', 'CSP'), ('Mobile Phone based Company', 'Mobile Phone based Company')], max_length=100)),
                ('company_aboutus', models.TextField()),
                ('date_added', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('emp_id', models.AutoField(primary_key=True, serialize=False)),
                ('emp_name', models.CharField(max_length=100)),
                ('emp_post', models.CharField(choices=[('Full Stack Python Web Developer', 'Full Stack Python Web Developer'), ('Python Programmer', 'Python Programmer'), ('Data Analyst', 'Data Analyst'), ('Software Engineer', 'Software Engineer'), ('Software Tester', 'Software Tester'), ('Web Developer', 'Web Developer'), ('Java Developer', 'Java Developer'), ('PL/SQL Developer', 'PL/SQL Developer'), ('Front-End Developer', 'Front-End Developer'), ('Game Developer', 'Game Developer'), ('Graphic Designer', 'Graphic Designer')], max_length=75)),
                ('emp_address', models.CharField(max_length=100)),
                ('emp_ctc', models.CharField(max_length=12)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.company')),
            ],
        ),
    ]
