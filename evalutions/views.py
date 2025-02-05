from django.shortcuts import render
from rest_framework import status
from evaluation_core.helpers.response import ResponseInfo
from rest_framework.response import Response
from rest_framework import generics
from .models import EvaluationRequest
from evalutions.serializer import EvaluationRequestSerializer
# Create your views here.


class SubmitEvaluationRequest(generics.GenericAPIView):
    def __init__(self, **kwargs):
        self.respone_format = ResponseInfo().response
        super(SubmitEvaluationRequest,self).__init__(**kwargs)

    serializer_class = EvaluationRequest

    def post(self, request):
        try:
            serializer = EvaluationRequestSerializer(data=request.data)
            if not serializer.is_valid():
                self.response_format['status_code']   = status.HTTP_400_BAD_REQUEST
                self.response_format['status']        = False
                self.response_format['errors']        = serializer.errors
                return Response(self.response_format,status=status.HTTP_500_INTERNAL_SERVER_ERROR)s
            evaluation = serializer.save(status='pending')
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:


class RetrieveEvaluationResult(generics.GenericAPIView):
    def get(self, request, id):
        try:
            evaluation = EvaluationRequest.objects.get(id=id)
            serializer = EvaluationRequestSerializer(evaluation)
            return Response(serializer.data)
        except EvaluationRequest.DoesNotExist:
            return Response({"error": "Evaluation not found"}, status=status.HTTP_404_NOT_FOUND)