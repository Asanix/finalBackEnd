from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from europharm.models import Profile


@login_required
def dashboard(request):
    length = Profile.objects.all().count()
    if length == 0:
        profile = Profile.objects.all()
    else:
        profile = Profile.objects.all()[length-1]

    context = {
        'profile': profile,
        'length': length
    }

    return render(request, '../template/account/dashboard.html', context)