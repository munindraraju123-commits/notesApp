from rest_framework import viewsets, permissions
from .models import Note
from .serializers import NoteSerializer

class NoteViewSet(viewsets.ModelViewSet):
    serializer_class = NoteSerializer
    permission_classes = [permissions.IsAuthenticated]  

    def get_queryset(self):
        return Note.objects.filter(owner=self.request.user).order_by('-last_update')

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
