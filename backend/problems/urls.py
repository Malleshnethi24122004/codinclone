from django.urls import path
from .views import ProblemListCreateAPIView

urlpatterns = [
    path('', ProblemListCreateAPIView.as_view(), name='problem-list-create'),
]
