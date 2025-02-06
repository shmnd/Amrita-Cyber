import resend
from celery import shared_task
from time import sleep
from evalutions.models import EvaluationRequest
from django.conf import settings

@shared_task
def process_evaluation(evaluation_id):
    evaluation = EvaluationRequest.objects.get(id=evaluation_id)
    # Simulate evaluation processing
    sleep(5)
    evaluation.result = "Simulated evaluation result"
    evaluation.status = 'completed'
    evaluation.save()


    resend.api_key = settings.RESEND_API_KEY

    try:
        resend.Emails.send({

            "from": settings.RESEND_API_FROM,
            "to": settings.RESEND_API_TO,
            "subject": "Evaluation Completed",
            "html": f"<p>Your evaluation for prompt '{evaluation.input_prompt}' is complete. Result: {evaluation.result}</p>",
        })
    except Exception as e:
        print('Error in email :', e)

