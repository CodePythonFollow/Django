from django.db import models


class Grade(models.Model):
    g_id = models.IntegerField()


class Student(models.Model):
<<<<<<< HEAD
    s_name = models.CharField(max_length=10)
    s_grade = models.ForeignKey(Grade, on_delete=models.CASCADE)  # 级联删除
=======

    s_name = models.CharField(max_length=10)
    s_grade = models.ForeignKey(Grade, on_delete=models.CASCADE, null=True)
>>>>>>> 750569be8370ed206f930d91d6e8d31fd4a2e3a8
