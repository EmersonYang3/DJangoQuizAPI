from django.urls import path
from quizzes.views import QuizView, QuizzesView, QuestionView, QuestionsView, ChoiceView, ChoicesView

urlpatterns = [
    path("api/quizzes/", QuizzesView.as_view()),
    path("api/quiz/<int:quiz_id>/", QuizView.as_view()),

    path("api/question/<int:question_id>/", QuestionView.as_view()),
    path("api/questions/<int:quiz_id>/", QuestionsView.as_view()),

    path("api/choice/<int:choice_id>/", ChoiceView.as_view()),
    path("api/choices/<int:question_id>/", ChoicesView.as_view())
]