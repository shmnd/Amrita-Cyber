from django.db import models

# Create your models here.

class AbstractDateFields(models.Model):
    created_at = models.DateTimeField(auto_now_add=True,editable=False,blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True,editable=False,blank=True, null=True)

    class Meta:
        abstract=True
class EvaluationRequest(AbstractDateFields):

    class Status(models.TextChoices):
        pending    = "Pending"
        completed = 'Completed'

    input_prompt = models.TextField(blank=True, null=True)
    status = models.CharField(blank=True, null=True,max_length=20, choices=Status.choices,default=Status.pending)
    result = models.TextField(blank=True, null=True)
    

    def __str__(self):
        return f"EvaluationRequest {self.id}"