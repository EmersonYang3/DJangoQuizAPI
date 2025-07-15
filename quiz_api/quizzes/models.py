from django.db import models

class Quiz(models.Model):
    title = models.CharField(max_length=250)
    description = models.CharField(max_length=500)
    subject_tags = models.JSONField(default=list)
    difficulty = models.IntegerField(default=1)
    imageUrl = models.URLField(default="https://i.sstatic.net/y9DpT.jpg")

    def __str__(self):
        return self.title
    
class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='questions')

    text = models.TextField(max_length=250)
    subject_tags = models.JSONField(default=list)
    difficulty = models.IntegerField(default=1)
    imageUrl = models.URLField(default="https://i.sstatic.net/y9DpT.jpg")

    def __str__(self):
        return self.text
    
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='choices')

    text = models.CharField(max_length=250)
    correct = models.BooleanField(default=False)

    def __str__(self):
        return self.text