# Generated by Django 4.2.1 on 2023-05-17 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('email_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='agent_work_record',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=200)),
                ('user_name', models.CharField(max_length=200)),
                ('work_record', models.CharField(max_length=200)),
                ('date_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]