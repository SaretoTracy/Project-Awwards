from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Profile,Projects
from .serializer import ProfileSerializer,ProjectsSerializer

# Create your views here.
def index(request):  

    # Function that gets the date
    
    
    return render(request, 'index.html')

def projects(request):  

    # Function that gets the date
    
    
    return render(request, 'projects.html')

class ProfileList(APIView):
   def get(self, request, format=None):
       all_Profile = Profile.objects.all()
       serializers = ProfileSerializer(all_Profile, many=True)
       return Response(serializers.data)
    def post(self, request, format=None):
    serializers = ProfileSerialize(data=request.data)
    if serializers.is_valid():
        serializers.save()
        return Response(serializers.data, status=status.HTTP_201_CREATED)
    return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


class ProjectsList(APIView):
   def get(self, request, format=None):
       all_Projects = Projects.objects.all()
       serializers = ProjectsSerializer(all_Projects, many=True)
       return Response(serializers.data)

    def post(self, request, format=None):
    serializers = ProjectsSerialize(data=request.data)
    if serializers.is_valid():
        serializers.save()
        return Response(serializers.data, status=status.HTTP_201_CREATED)
    return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)