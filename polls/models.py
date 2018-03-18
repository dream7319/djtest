from django.db import models
from django.utils import timezone
import datetime

# Create your models here.
class Question(models.Model):
    questionText = models.CharField(db_column="question_text",max_length= 200)
    pubDate = models.DateTimeField(db_column="pub_date")

    def __str__(self):
        return self.questionText

    def was_published_recently(self):
        return self.pubDate >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    question = models.ForeignKey(Question,on_delete=models.CASCADE)
    choiceText = models.CharField(db_column= 'choice_text',max_length=200)
    votes = models.IntegerField(db_column='votes',default=0)

    def __str__(self):
        return self.choiceText
