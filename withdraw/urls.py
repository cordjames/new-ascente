from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from .views import EmailView

urlpatterns = [
   path('email/', csrf_exempt(EmailView.as_view())),
]
