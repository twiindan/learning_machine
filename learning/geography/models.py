from django.db import models
from django.utils import timezone
import datetime, calendar, time
from django.utils import timezone

# -*- coding: utf-8 -*-


class Geography(models.Model):

    created = models.DateTimeField(auto_now_add=True)
    question = models.CharField(max_length=100, blank=True, default='', unique=True)
    answer = models.CharField(max_length=100, blank=True, default='')

    def get_question(self):
        return self.question

    class Meta:
        ordering = ('created',)

class QuestionsByUserModel(models.Model):

    username = models.CharField(max_length=100, unique=False)
    question_id = models.IntegerField()
    box = models.IntegerField()
    date = models.DateTimeField(auto_now=True)

    def boxing_question(self, box):

        if box == 1:
            calculated_time = timezone.now() - datetime.timedelta(minutes=1)
        elif box == 2:
            calculated_time = timezone.now() - datetime.timedelta(minutes=5)
        elif box == 3:
            calculated_time = timezone.now() - datetime.timedelta(minutes=10)

        return self.date < calculated_time




