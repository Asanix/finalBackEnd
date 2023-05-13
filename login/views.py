from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from europharm.models import Profile


@login_required
def dashboard(request):
    profile = Profile.objects.all()
    return render(request, '../template/account/dashboard.html', {'profile': profile})
