from rest_framework import generics, status
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from friends.api.serializers import FriendSerializer
from friends.models import Friend
from users.models import User


class FriendListCreateView(generics.ListCreateAPIView):
    serializer_class = FriendSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Friend.objects.filter(user=user)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = self.request.user
            friend = serializer.save(user=user)
            response_data = {
                'message': 'Friend created successfully',
                'friend': FriendSerializer(friend).data
            }
            return Response(response_data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FriendRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = FriendSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Friend.objects.filter(user=user)

    def get_object(self):
        friend_id = self.kwargs['pk']
        return get_object_or_404(self.get_queryset(), id=friend_id)

