from django.shortcuts import render,redirect,get_object_or_404
from django.core.exceptions import ObjectDoesNotExist
from .forms import  RatingsForm
from django.http.response import HttpResponseRedirect
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Profile,Projects,Rating
from django.contrib.auth.models import User
from .serializer import ProfileSerializer,ProjectsSerializer

# Create your views here.
def index(request):  

    # Function that gets the date
    
    
    return render(request, 'index.html')

def projects(request):  

    # Function that gets the date
    post = Projects.objects.all()
    
    
    
    return render(request, 'projects.html',{'posts':post})



def project_details(request, project_id):
   current_user = request.user
   all_ratings = Rating.objects.filter(project_id=project_id).all()
   project = Projects.objects.get(pk = project_id)
   ratings = Rating.objects.filter(user=request.user,project=project_id).first()
   rating_status = None
   if ratings is None:
       rating_status = False
   else:
       rating_status = True
   if request.method == 'POST':
       form = RatingsForm(request.POST)
       if form.is_valid():
           rate = form.save(commit=False)
           rate.user = request.user
           rate.project = project
           rate.save()
           post_ratings = Rating.objects.filter(project=project_id)
#calculating design
           design_ratings = [design.design_rating for design in post_ratings]
           design_rating_average = sum(design_ratings) / len(design_ratings)
#calculating content
           content_ratings = [content.content_rating for content in post_ratings]
           content_rating_average = sum(content_ratings) / len(content_ratings)
#calculating usability
           usability_ratings = [usability.usability_rating for usability in post_ratings]
           usability_rating_average = sum(usability_ratings) / len(usability_ratings)
 
     
#calculating average
           aggregate_average_rate = (design_rating_average + usability_rating_average + content_rating_average) / 3
           print(aggregate_average_rate)
           rate.design_rating_average = round(design_rating_average, 2)
           rate.usability_rating_average = round(usability_rating_average, 2)
           rate.content_rating_average = round(content_rating_average, 2)
           rate.aggregate_average_rate = round(aggregate_average_rate, 2)
           rate.save()
           return HttpResponseRedirect(request.path_info)
   else:
       form = RatingsForm()
   return render(request, 'details.html', {'current_user':current_user,'all_ratings':all_ratings,'project':project,'rating_form': form,'rating_status': rating_status})

def delete(request,project_id):
    current_user = request.user
    project = Projects.objects.get(pk=project_id)
    if project:
        project.delete_project()
    return redirect('details.html')
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