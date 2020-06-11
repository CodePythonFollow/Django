from django.db import models


class Grade(models.Model):
    g_id = models.IntegerField()


class Strudent(models.Model):

    s_name = models.CharField(max_length=10)
    s_grade = models.ForeignKey(Grade)