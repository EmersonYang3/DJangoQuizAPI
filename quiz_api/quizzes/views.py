from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Quiz, Question, Choice
from .serializers import QuizSerializer, QuestionSerializer, ChoiceSerializer

class QuizView(APIView):
    def get(self, request, quiz_id):
        quiz = get_object_or_404(Quiz, id=quiz_id)
        serializer = QuizSerializer(quiz, context={'request': request})
        return Response(serializer.data)

class QuizzesView(APIView):
    def get(self, request):
        quizzes = Quiz.objects.all()
        serializer = QuizSerializer(quizzes, many=True, context={'request': request})
        return Response(serializer.data)

class QuestionView(APIView):
    def get(self, request, question_id):
        question = get_object_or_404(Question, id=question_id)
        serializer = QuestionSerializer(question, context={'request': request})
        return Response(serializer.data)

class QuestionsView(APIView):
    def get(self, request, quiz_id):
        questions = Question.objects.filter(quiz=quiz_id)
        serializer = QuestionSerializer(questions, many=True, context={'request': request})

        return Response(serializer.data)
    
class ChoiceView(APIView):
    def get(self, request, choice_id):
        choice = get_object_or_404(Choice, id = choice_id)
        serializer = ChoiceSerializer(choice, context={'request': request})

        return Response(serializer.data)
    
class ChoicesView(APIView):
    def get(self, request, question_id):
        choices = Choice.objects.filter(question = question_id)
        serializer = ChoiceSerializer(choices, many=True, context={'request': request})

        return Response(serializer.data)