from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from django.views import View
from django.shortcuts import render, redirect
from .forms import ProfileComparisonForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

from .models import Profile

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('compare-profiles')  # Redirect to your home page
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})

class CompareProfilesView(View):
    template_name = 'compare_profiles.html'

    def get(self, request, *args, **kwargs):
        form = ProfileComparisonForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = ProfileComparisonForm(request.POST)
        if form.is_valid():
            favorite_color = form.cleaned_data['favorite_color']
            pet_name = form.cleaned_data['pet_name']
            maiden_name = form.cleaned_data['maiden_name']

            # Assuming CustomUser is your user model
            user = Profile.objects.get(user=request.user)

            if (
                favorite_color.lower() == user.favorite_color.lower() and
                pet_name.lower() == user.pet_name.lower() and
                maiden_name.lower() == user.maiden_name.lower()
            ):
                messages.success(request, 'Logging in')
                return redirect('dashboard')
            else:
                messages.error(request, 'Your answers are incorrect')

        return render(request, self.template_name, {'form': form})
    
@login_required
@csrf_exempt
def user_dashboard(request):
    user_profile = Profile.objects.get(user=request.user)

    # Render the dashboard template
    return render(request, 'dashboard.html', {'user_profile': user_profile})


    