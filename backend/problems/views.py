from rest_framework import generics, permissions
from .models import Problem
from .serializers import ProblemSerializer

class ProblemListCreateAPIView(generics.ListCreateAPIView):
    queryset = Problem.objects.all()
    serializer_class = ProblemSerializer

    # Allow only authenticated users to create problems, anyone can list
    def get_permissions(self):
        if self.request.method == 'POST':
            return [permissions.IsAuthenticated()]
        return [permissions.AllowAny()]
