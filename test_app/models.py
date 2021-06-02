from django.db import models
from django.contrib.auth.models import User


class Test(models.Model):
    """Test"""
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Question(models.Model):
    """Question in the test"""
    CHOICE_OF_QUESTION_TYPE = [
        ('ONE', 'One right answer'),
        ('SOME', 'Several correct answers'),
        ('ENTER', 'Entering the correct answer'),
    ]
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    type = models.CharField(max_length=5, choices=CHOICE_OF_QUESTION_TYPE)
    text = models.TextField()

    def __str__(self):
        return self.text


class Answer(models.Model):
    """Variant of the answer to the question from the test."""
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    correct = models.BooleanField()

    def __str__(self):
        return self.text


class UserAnswer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
