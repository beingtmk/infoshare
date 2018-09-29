# Generated by Django 2.1.1 on 2018-09-29 09:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('articles', '0002_article_secret'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('news', '0002_news_secret'),
        ('qa', '0002_vote_secret'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='group_pictures/%Y/%m/%d/', verbose_name='Group image')),
                ('description', models.CharField(max_length=1000)),
                ('articles', models.ManyToManyField(to='articles.Article')),
                ('members', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
                ('news', models.ManyToManyField(to='news.News')),
                ('questions', models.ManyToManyField(to='qa.Question')),
            ],
        ),
        migrations.CreateModel(
            name='POR',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start', models.DateTimeField()),
                ('end', models.DateTimeField()),
                ('por', models.CharField(max_length=20)),
                ('group', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='group', to='groups.Group')),
            ],
        ),
    ]