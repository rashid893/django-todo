from django.db import models
from django.utils import timezone

class Task(models.Model):
    title = models.CharField(max_length=255, db_index=True)
    notes = models.TextField(blank=True, null=True)
    done = models.BooleanField(default=False, db_index=True)
    created_at = models.DateTimeField(default=timezone.now, db_index=True)
    completed_at = models.DateTimeField(blank=True, null=True, db_index=True)

    class Meta:
        ordering = ["done", "-created_at"]

    def __str__(self):
        return self.title