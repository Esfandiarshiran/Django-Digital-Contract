from django.shortcuts import render
from .models import TeamMembers


# Create your views here.

def about_us(request):
    # introduce = SiteSetting.objects.first().introduce
    # description = SiteSetting.objects.first().description
    team_members = TeamMembers.objects.all()

    context = {

        'team_members': team_members,

    }
    return render(request, 'Docusign_AboutUs/about_us.html', context)
