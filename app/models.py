from django.db import models


class Grade(models.Model):
    g_id = models.IntegerField()


class Student(models.Model):
    s_name = models.CharField(max_length=10)
    s_grade = models.ForeignKey(Grade, on_delete=models.CASCADE, null=True)
