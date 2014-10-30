__author__ = 'arobres'
# -*- coding: utf-8 -*-

from rest_framework import serializers
from geography.models import Geography, QuestionsByUserModel
from django.contrib.auth.models import User

class GeographySerializer(serializers.ModelSerializer):
    class Meta:
        model = Geography
        fields = ('id', 'question', 'answer')

class PlaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Geography
        fields = ('id', 'question')

class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Geography
        fields = ('answer')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password', 'email')

class QuestionsByUserModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = QuestionsByUserModel
        fields = ('username', 'question_id', 'box')
