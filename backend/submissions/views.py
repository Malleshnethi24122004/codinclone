from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Submission
from .serializers import SubmissionSerializer
from rest_framework.permissions import IsAuthenticated

class SubmissionViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated] 
    queryset = Submission.objects.all()
    serializer_class = SubmissionSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        submission = serializer.save(user=self.request.user, status='Evaluating')
        
        # Simulate code evaluation (we will sandbox this later)
        if "print(" in submission.code:
            submission.status = "Accepted"
            submission.output = "Sample output"
        else:
            submission.status = "Error"
            submission.output = "No print statement found"

        submission.save()
