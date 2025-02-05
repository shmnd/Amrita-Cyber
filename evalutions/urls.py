from django.urls import path
from evalutions.views import SubmitEvaluationRequest,RetrieveEvaluationResult
urlpatterns = [
    path('evaluate/', SubmitEvaluationRequest.as_view()),
    path('evaluate/<int:id>/', RetrieveEvaluationResult.as_view()),

]
