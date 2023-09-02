from django.db import models
from django.contrib.auth.models import User


class UserExtention(models.Model):
    grade = models.IntegerField(default=None, blank=True, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="userextention")

    def __str__(self):
        return self.user.username
    
    def usertype(self):
        if self.grade == None:
            return "Teacher"
        return self.grade


class Merit(models.Model):
    code = models.CharField(max_length=256)
    description = models.TextField()
    points = models.IntegerField()

    def __str__(self):
        return f"{self.points}: {self.description}"


class Record(models.Model):
    teacher = models.ForeignKey(User, on_delete=models.SET_NULL, related_name="teacher", null=True)
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name="student")
    merit = models.ForeignKey(Merit, on_delete=models.CASCADE)
    comment = models.CharField(max_length=255)

    def __str__(self):
        return f"Record: {self.pk}, {self.teacher}, {self.student}, {self.merit}"