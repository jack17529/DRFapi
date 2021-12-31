from rest_framework.serializers import ModelSerializer
from base.models import Profiles, Resumes
# from django.contrib.auth import get_user_model

# class UserSerializer(ModelSerializer):
#     class Meta:
#         model = get_user_model()
#         fields = ('id','username')

class ProfileSerializer(ModelSerializer):
    class Meta:
        model = Profiles
        fields='__all__'

class ResumeSerializer(ModelSerializer):
    class Meta:
        model = Resumes
        fields='__all__'
        # fields=['file','id','updated','created']