from django.db import models as m

# Create your models here.

class Topic(m.Model):
    name = m.CharField(max_length = 90)

    def __str__(self):
        return self.name

class Quiz(m.Model):
    topic = m.ForeignKey(Topic, on_delete = m.SET_NULL, null = True)
    name = m.CharField(max_length = 90)
    created = m.DateTimeField(auto_now_add = True)
    updated =  m.DateTimeField(auto_now = True)

    def __str__(self):
        return self.name

class Question(m.Model):
    quiz = m.ForeignKey(Quiz, on_delete = m.CASCADE)
    q_text = m.TextField()
    created = m.DateTimeField(auto_now_add = True)
    updated =  m.DateTimeField(auto_now = True)

