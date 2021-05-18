from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status
from .serializers import DocumentSerializer



class DocumentView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        document_serializer = DocumentSerializer(data=request.data)
        if document_serializer.is_valid():
            document_serializer.save()
            return Response(document_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(document_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
