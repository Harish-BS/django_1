# Generated by Django 5.0.6 on 2024-06-14 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0002_employee_role'),
    ]

    operations = [
        migrations.CreateModel(
            name='employee_dept',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dept', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='employee_role',
            name='role',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
