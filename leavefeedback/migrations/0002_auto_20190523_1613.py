# Generated by Django 2.2.1 on 2019-05-23 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leavefeedback', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LeaveModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=100)),
                ('good', models.CharField(max_length=1000)),
                ('improve', models.CharField(max_length=1000)),
            ],
        ),
        migrations.DeleteModel(
            name='AskModel',
        ),
    ]
