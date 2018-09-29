# Generated by Django 2.1.1 on 2018-09-29 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qa', '0002_vote_secret'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vote',
            name='secret',
        ),
        migrations.AddField(
            model_name='question',
            name='secret',
            field=models.BooleanField(default=False),
        ),
    ]