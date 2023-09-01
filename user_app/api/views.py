from rest_framework import generics, status
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView

from rest_framework_simplejwt.tokens import RefreshToken

from user_app.api.serializers import RegistrationSerializer


class RegistrationView(APIView):
    
    def post(self, request):
        print(request.body)
        serializer = RegistrationSerializer(data = request.data)
        data = {}
        if (serializer.is_valid()):
            account = serializer.save()
            
            data['username'] = account.username
            data['email'] = account.email
            refresh = RefreshToken.for_user(account)
            
            data['token'] = {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
            }
            
            # data['token'] =  Token.objects.get(user = account).key
            data['response'] = 'Registration successful'
                        
            return Response( data, status = status.HTTP_201_CREATED)
    
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class LogoutView(APIView):
    
    def post(self, request):
        
        request.user.auth_token.delete()
        return Response(status = status.HTTP_200_OK)