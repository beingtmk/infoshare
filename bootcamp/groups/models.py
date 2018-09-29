from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _
from bootcamp.articles.models import Article
from bootcamp.news.models import News
from bootcamp.qa.models import Question


# Create your models here.
class Group(models.Model):
    EVENT = "E"
    CLUB = "C"
    TYPE = (
        (EVENT, _("Event")),
        (CLUB, _("Club")),
    )

    image = models.ImageField(
        _('Group image'), upload_to='group_pictures/%Y/%m/%d/')
    description = models.CharField(max_length=1000)
    members = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='members')
    articles = models.ManyToManyField(Article, blank=True)
    news = models.ManyToManyField(News, blank=True)
    questions = models.ManyToManyField(Question, blank=True)
    requests = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='requests', blank=True)
    name = models.CharField(max_length=100, blank=True)
    type = models.CharField(max_length=100, choices=TYPE, blank=True)

class POR(models.Model):
    group = models.ForeignKey(
        Group, related_name="group", null=True,
        on_delete=models.SET_NULL)
    start = models.DateTimeField()
    end = models.DateTimeField()
    por = models.CharField(max_length=20)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, related_name="user",
        on_delete=models.SET_NULL)
