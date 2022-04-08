from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import  MoringaMerch
from .serializer import MerchSerializer

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