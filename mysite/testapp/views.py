from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response

# Create your views here.
class testview(generics.GenericAPIView):

    def post(self, request):
        # return True
        response_dict = {"test":123}
        return Response({"status": True}, status=status.HTTP_200_OK)
