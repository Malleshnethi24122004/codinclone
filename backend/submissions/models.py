from django.db import models
from django.conf import settings
from problems.models import Problem

class Submission(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="submissions")
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE, related_name="submissions")
    code = models.TextField()
    language = models.CharField(max_length=30, default='python')
    status = models.CharField(max_length=30, default='Pending')  # Pending, Accepted, Wrong Answer, Error, etc.
    output = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Submission by {self.user.username} for Problem {self.problem.id}"
