from django.db import models
from django.conf import settings


class Projects(models.Model):
    title = models.CharField(max_length=300)
    description = models.CharField(max_length=1000)
    type = models.CharField(max_length=100)
    author_user_id = models.ForeignKey(
        to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
        related_name="author_user_project")


class Contributors(models.Model):
    PERMISSIONS = (
        ("1", "Permission 1"),
        ("2", "Permission 2"),
        ("3", "Permission 3"),
    )
    user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    project = models.ForeignKey(to=Projects, on_delete=models.CASCADE,
                                related_name="contributors")
    permission = models.CharField(max_length=300, choices=PERMISSIONS)
    role = models.CharField(max_length=300)


class Issues(models.Model):
    title = models.CharField(max_length=300)
    desc = models.CharField(max_length=1000)
    tag = models.CharField(max_length=300)
    priority = models.CharField(max_length=300)
    project = models.ForeignKey(to=Projects, on_delete=models.CASCADE)
    status = models.CharField(max_length=300)
    author_user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
        related_name="author_user_issue")
    assignee_user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
        related_name="assignee_user_issue")
    created_time = models.DateTimeField(auto_now_add=True)


class Comments(models.Model):
    description = models.CharField(max_length=1000)
    author_user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
        related_name="author_user_comment")
    issue = models.ForeignKey(to=Issues, on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True)
