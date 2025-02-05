from django.urls import path
from evalutions.views import SubmitEvaluationRequest,RetrieveEvaluationResult
urlpatterns = [
    path('evaluate/', SubmitEvaluationRequest.as_view(), name='submit-evaluation'),
    # path('evaluate-result', RetrieveEvaluationResult.as_view(), name='retrieve-evaluation'),
    path('evaluate/<int:id>/', RetrieveEvaluationResult.as_view(), name='retrieve-evaluation'),

]
