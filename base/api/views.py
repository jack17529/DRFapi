from django.http import response
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework import status
from base.models import Profiles, Resumes
from .serializers import ProfileSerializer, ResumeSerializer

# from rest_framework.parsers import JSONParser
# from django.http.response import JsonResponse

from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated

# I have used function based views.

@api_view(['GET'])
def getRoutes(request):
    # serializer_class = UserSerializer

    routes=[
        'GET,POST       /api/profiles/',
        'GET,PUT,DELETE /api/profiles/:id',
        'GET,PUT,POST   /api/profiles/:id/resumes',
        'POST           /api/token/',
        'POST           /api/token/refresh'
    ]
    return Response(routes)


@api_view(['GET', 'POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def getAddProfiles(request):
    """
    List all the profiles or create a new porfile.
    """

    if request.method == 'GET':
        profiles = Profiles.undeleted_objects.filter()  # will only provide undeleted profiles.
        serializer = ProfileSerializer(profiles,many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        # {
        #     "name": "John Doe",
        #     "summary": "Frontend Engineer",
        # }

        serializer=ProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET', 'PUT', 'DELETE'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def getUpdateRemoveProfile(request,pk):
    """
    Retrieve, update or delete a profile.
    """

    try:
        profile = Profiles.undeleted_objects.get(id=pk)
    except Profiles.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = ProfileSerializer(profile,many=False)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ProfileSerializer(profile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        # profile.delete()
        # try soft delete here.
        profile.soft_delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# The profile which are soft deleted should not show the resumes.
@api_view(['GET', 'PUT', 'POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def getUpdateAddResumes(request,pk):
    """
    Retrieve, update and add resumes.
    """

    try:
        profile = Profiles.undeleted_objects.get(id=pk)
    except Profiles.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    try:
        resumes = Resumes.objects.filter(profile_id=pk)
    except Resumes.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    # we may only want the admin users to do this request in production.
    if request.method == 'GET':
        serializer = ResumeSerializer(resumes,many=True)
        return Response(serializer.data)

    if request.method == 'PUT' or request.method == 'POST':
        serializer=ResumeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # if request.method == 'POST':
    #     serializer=ResumeSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['POST'])
# @authentication_classes([JWTAuthentication])
# @permission_classes([IsAuthenticated])
# def addResume(request):
#     """
#     Upload a resume.
#     """

#     if request.method == 'POST':
#         serializer=ResumeSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)