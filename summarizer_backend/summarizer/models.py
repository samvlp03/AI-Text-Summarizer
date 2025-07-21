from django.db import models
from django.contrib.auth.models import User

class Summary(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    original_text = models.TextField()
    summary_text = models.TextField()
    length = models.CharField(max_length=20)  # short, medium, long
    tonality = models.CharField(max_length=20)  # formal, casual, academic, etc.
    temperature = models.FloatField(default=0.7)
    top_p = models.FloatField(default=0.9)
    focus = models.CharField(max_length=100, blank=True)
    is_favorite = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    model_used = models.CharField(max_length=50, default='llama3.2:1b')
    
    def __str__(self):
        return f"Summary {self.id}"

class ExportFormat(models.Model):
    name = models.CharField(max_length=50)
    mime_type = models.CharField(max_length=100)
    extension = models.CharField(max_length=10)

    def __str__(self):
        return self.name