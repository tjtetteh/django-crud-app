from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView 
from .models import User
from .serializer import UserSerializer
from django.shortcuts import get_object_or_404

# Create your views here.
class Users (APIView):
    def get(self, request, user_id=None):
        # get a single user with id
        if user_id is not None:
            user = get_object_or_404(User, id=user_id)
            serializer = UserSerializer(user)
            return Response (serializer.data, status=status.HTTP_200_OK)

        #get all users
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response (serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        # create a new user
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response (serializer.data, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

    def put (self, request, user_id=None):
        #update an existing user
        if not user_id:
            return Response({"error": "User ID is required to update user"}, status=status.HTTP_400_BAD_REQUEST)
        
        user = get_object_or_404(User, id=user_id)
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete (self, request, user_id=None):
        if not user_id:
            return Response({"error": "User ID is required to delete user"}, status=status.HTTP_400_BAD_REQUEST)
    
        user = get_object_or_404(User, id=user_id)
        user.delete()
        return Response({"message": "User has been deleted successfully"}, status=status.HTTP_200_OK)

    


 
    
