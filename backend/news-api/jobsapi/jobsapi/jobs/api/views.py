from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404

from jobs.models import JobOffer
from jobs.api.serializers import JobSerializer

@api_view(["GET", "POST"])
def job_list_create_api_view(request):
    if request.method == "GET":
        jobs = JobOffer.objects.filter(active=True)
        serializer = JobSerializer(jobs, many=True)
        return Response(serializer.data)
    
    """ elif request.method == "POST":
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_404_BAD_REQUEST) """
        
@api_view(["GET", "PUT", "DELETE"])
def job_detail_api_view(request, pk):
    try:
        job = JobOffer.objects.get(pk=pk)
    except JobOffer.DoestNotExist:
        return Response({
            "error": {
                "code": 404,
                "message": "Job not found!"
            }
        }, status=status.HTTP_404_NOT_FOUND)
        
    if request.method == "GET":
        serializer = JobSerializer(job)
        return Response(serializer.data)
    
    elif request.method == "PUT":
        serializer = JobSerializer(job, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_404_BAD_REQUEST)
    
    elif request.method == "DELETE":
        job.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
        
class JobListCreateAPIView(APIView):
    def get(self, request):
        jobs = JobOffer.objects.all()
        serializer = JobSerializer(jobs, many=True)
        return Response(serializer.data)
        
    def post(self, request):
        serializer = JobSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class JobDetailAPIView(APIView):
    def get_object(self, pk):
        article = get_object_or_404(Article, pk=pk)
        return article
    
    def get(self, request, pk):
        article = self.get_object(pk)
        serializer = JobSerializer(article)
        return Response(serializer.data)
    
    def put(self, request, pk):
        article = self.get_object(pk)
        serializer = JobSerializer(article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_404_BAD_REQUEST)
    
    def delete(self, request, pk):
        article = self.get_object(pk)
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)