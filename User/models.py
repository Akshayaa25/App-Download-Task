from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=20, default="")
    password = models.CharField(max_length=20, default="")
    confirmpassword = models.CharField(max_length=20, default="")

    def total_points(self):
        tasks = self.task_set.all()
        return sum(task.points for task in tasks)


class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    appname = models.CharField(max_length=20,default="")
    points = models.IntegerField(default="")
    screenshot = models.ImageField(upload_to='screenshot/', blank=True, null=True)