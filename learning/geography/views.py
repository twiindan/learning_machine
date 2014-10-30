from django.shortcuts import render

# Create your views here.

# -*- coding: utf-8 -*-

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.renderers import UnicodeJSONRenderer, BrowsableAPIRenderer
from geography.models import Geography, QuestionsByUserModel
from geography.serializer import GeographySerializer, PlaySerializer, UserSerializer, \
    QuestionsByUserModelSerializer
from random import choice
from django.contrib.auth.models import User
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from django.http import Http404



class QuestionBase(APIView):

    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAdminUser,)

    def get(self, request, format=None):

        geography = Geography.objects.all()
        serializer = GeographySerializer(geography)
        return Response(serializer.data)

    def post(self, request, format=None):

        serializer = GeographySerializer(data=request.DATA)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        elif serializer.errors == ({'question': [u'Geography with this Question already exists.']}):
            return Response(serializer.errors, status=status.HTTP_409_CONFLICT)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class QuestionDetail(APIView):

    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAdminUser,)

    def get_object(self, pk):
        try:
            return Geography.objects.get(pk=pk)
        except Geography.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):

        geography = self.get_object(pk)
        serializer = GeographySerializer(geography)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        geography = self.get_object(pk)
        serializer = GeographySerializer(geography, data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        geography = self.get_object(pk)
        geography.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class PlayBase(APIView):

    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)

    renderer_classes = (UnicodeJSONRenderer, BrowsableAPIRenderer)


    def get_object(self, pk):

        try:
            geography = Geography.objects.get(pk=pk)
            return geography
        except Geography.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def choose_question(self, questions_by_user):

        question_list = []
        print len(question_list)
        for question in questions_by_user:

            if question.box == 0:
                question_list.append(question)
            else:
                if question.boxing_question(question.box):
                    question_list.append(question)


        print len(question_list)

#        for question in question_list:
#
#            print question.username
#            print question.question_id
#            print question.box

        return choice(question_list)


    def get(self, request, format=None):

        all_valid_questions = Geography.objects.all()
        questions_by_user = QuestionsByUserModel.objects.filter(username=request.user)

        if len(all_valid_questions) == 0:
            return Response('No Questions loaded in the DataBase')

        if len(questions_by_user) == 0:

            for question in all_valid_questions:

                a1 = QuestionsByUserModel(username=request.user, question_id=question.pk, box=0)
                a1.save()

        elif len(questions_by_user) != len(all_valid_questions):

            print ('ALL VALID QUESTIONS: {}\n "QUESTIONS BY USER: {}'.format(len(all_valid_questions),
                                                                             len(questions_by_user)))

            for question in all_valid_questions:

                print question.pk

            return Response('User have not the same number of questions: {}'.format(len(questions_by_user)))

        question_id = self.choose_question(questions_by_user).id
        geography = self.get_object(pk=question_id)
        serializer = PlaySerializer(geography)
        return Response(serializer.data)

    def post(self, request, format=None):


        pk = request.DATA['id']
        geography = self.get_object(pk=pk)
        question_filter = QuestionsByUserModel.objects.filter(username=request.user, question_id=pk)

        user_question = QuestionsByUserModel.objects.get(pk=question_filter[0].pk)


        if (geography.answer.lower() == request.DATA['answer'].lower()):

            if user_question.box < 3:
                user_question.box += 1
                user_question.save()

            serializer = QuestionsByUserModelSerializer(user_question)

            return Response('Acertaste! {}'.format(serializer.data), status=status.HTTP_200_OK)

        else:

            user_question.box = 0
            user_question.save()

            serializer = QuestionsByUserModelSerializer(user_question)

            return Response('Fallaste! {}'.format(serializer.data), status=status.HTTP_200_OK)


class UserView(APIView):

    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAdminUser,)

    def post(self, request, format=None):

        serializer = UserSerializer(data=request.DATA)
        if serializer.is_valid():
            user = User.objects.create_user(serializer.data['username'], serializer.data['email'],
                                            serializer.data['password'])
            user.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def get(self, pk):

        user = User.objects.all()
        serializer = UserSerializer(user)
        return Response(serializer.data)

class UserDetailedView(APIView):

    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAdminUser,)

    def get_object(self, pk):

        try:
            return User.objects.get(username=pk)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):

        user = self.get_object(pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def delete(self, request, pk, format=None):
        user = self.get_object(pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)