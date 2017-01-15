from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

from datetime import datetime


# Create your models here.
class Article(models.Model):
  """The article"""
  title = models.CharField(max_length=100, default='Brez naslova')
  content = models.TextField()
  pub_date = models.DateTimeField( default=datetime.now )
  author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
	
  class Meta:
		permissions = (
      ('edit_own_article', 'Can edit his own the article'),
    )
  

class Comment(models.Model):
  """The comment to the article"""
  comment = models.TextField()
  pub_date = models.DateTimeField( default=datetime.now )
  author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
  article_id = models.ForeignKey(Article, on_delete=models.CASCADE, blank=False)
  class Meta:
  	permissions = (
      ('edit_own_comment', 'Can edit his own comment'),
    )

