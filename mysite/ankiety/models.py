from django.db import models

# Każda tabela ma kilka zmiennych, każda zmiennych musi być reprezentowana przez typ danych, poniżej użwamy właśnie 'Field'. 'CharField' jest dla pól znakowych, z wartością maksymalną znaków ustawioną na 200, co jest obowiązkowe!. 'DateTimeField' oznacza datę publikacji. Pole 'IntegerField' jest to pole liczbowe, a wartość domyślna 'default' jest opcjonalna. 'ForeignKey' dodatkowy, obcy klucz za pomocą którego łączymy tabelę Choice z Question. 
class Question(models.Model):
    # czyli mamy tabelę Questions z polami question_text i pub_date
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

class Choice(models.Model):
    # czyli mamy tabelę Choice z polami question, choice_text i votes
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)