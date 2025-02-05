from django.shortcuts import render
from rest_framework import status
from evaluation_core.helpers.response import ResponseInfo
from rest_framework.response import Response
from rest_framework import generics
from evalutions.serializer import EvaluationRequestSerializer
from drf_yasg.utils import swagger_auto_schema
from evalutions.models import EvaluationRequest
# Create your views here.


class SubmitEvaluationRequest(generics.GenericAPIView):
    def __init__(self, **kwargs):
        self.response_format = ResponseInfo().response
        super(SubmitEvaluationRequest,self).__init__(**kwargs)

    serializer_class = EvaluationRequestSerializer
    @swagger_auto_schema(tags=['Home'])
    def post(self, request):
        try:
            serializer = self.serializer_class(data=request.data)
            if not serializer.is_valid():
                self.response_format['status_code']   = status.HTTP_400_BAD_REQUEST
                self.response_format['status']        = False
                self.response_format['errors']        = serializer.errors
                return Response(self.response_format,status=status.HTTP_500_INTERNAL_SERVER_ERROR)
                        
            evaluation = serializer.save(status='pending')

            self.response_format["status_code"] = status.HTTP_201_CREATED
            self.response_format["status"] = True
            self.response_format["message"] = "Evaluation request submitted successfully."
            self.response_format["data"] = serializer.data
            return Response(self.response_format, status=status.HTTP_201_CREATED)

        except Exception as e:
            self.response_format["status_code"] = status.HTTP_500_INTERNAL_SERVER_ERROR
            self.response_format["status"] = False
            self.response_format["message"] = "An error occurred while processing the request."
            self.response_format["errors"] = {"error": str(e)}
            return Response(self.response_format, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class RetrieveEvaluationResult(generics.GenericAPIView):

    def __init__(self, **kwargs):
        self.response_format = ResponseInfo().response
        super(RetrieveEvaluationResult,self).__init__(**kwargs)

    serializer_class = EvaluationRequestSerializer 
        
    @swagger_auto_schema(tags=['Home'])
    def get(self, request, id):
        try:
            print(id,'iddddddddddddd')
            evaluation = EvaluationRequest.objects.get(id=id)
            print(evaluation,'eval222222222222222222222')
            serializer = self.serializer_class(evaluation)
            
            self.response_format["status_code"] = status.HTTP_200_OK
            self.response_format["status"] = True
            self.response_format["message"] = "Evaluation result retrieved successfully."
            self.response_format["data"] = serializer.data
            return Response(self.response_format, status=status.HTTP_200_OK)

        except EvaluationRequest.DoesNotExist:
            self.response_format["status_code"] = status.HTTP_404_NOT_FOUND
            self.response_format["status"] = False
            self.response_format["message"] = "Evaluation not found."
            self.response_format["errors"] = {"id": "No evaluation exists with the given ID."}
            return Response(self.response_format, status=status.HTTP_404_NOT_FOUND)

        except Exception as e:
            self.response_format["status_code"] = status.HTTP_500_INTERNAL_SERVER_ERROR
            self.response_format["status"] = False
            self.response_format["message"] = "An error occurred while retrieving the evaluation result."
            self.response_format["errors"] = {"error": str(e)}
            return Response(self.response_format, status=status.HTTP_500_INTERNAL_SERVER_ERROR)