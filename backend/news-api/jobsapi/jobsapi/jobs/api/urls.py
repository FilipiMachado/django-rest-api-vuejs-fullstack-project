from django.urls import path
from jobs.api.views import (JobListCreateAPIView, JobDetailAPIView)
# article_list_create_api_view
# job_list_create_api_view

""" from news.api.views import (article_list_create_api_view, 
                            article_detail_api_view) """

urlpatterns = [
    path("jobs/", JobListCreateAPIView.as_view(), name="job-list"),
    path("jobs/<int:pk>", JobDetailAPIView.as_view(), name="job-detail"),
]
