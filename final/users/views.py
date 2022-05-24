from rest_framework import views
from .serializers import UserRegistrationSerializer

class Login(views.APIView):

    def post(self, request):
        serializer = 
