from datetime import datetime

from django.utils.timesince import timesince

from rest_framework import serializers

from jobs.models import JobOffer

class JobSerializer(serializers.ModelSerializer):
    # time_since_publication = serializers.SerializerMethodField()
    
    class Meta:
        model = JobOffer
        fields = "__all__" # When we want all the fields of our model
        # fields = ("title", "description") # Choose only the fields we want to serialize
        # exclude = ("id") # Exclude, for example, the id from the serialization