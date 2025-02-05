from celery import shared_task
from time import sleep
from evalutions.models import EvaluationRequest

@shared_task
def process_evaluation(evaluation_id):
    evaluation = EvaluationRequest.objects.get(id=evaluation_id)
    # Simulate evaluation processing
    sleep(10)
    evaluation.result = "Simulated evaluation result"
    evaluation.status = 'completed'
    evaluation.save()