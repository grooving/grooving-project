from rest_framework.response import Response
# from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import update_last_login
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework import status
from login.serializers import ArtistSerializer, CustomerSerializer, LoginSerializer
from django.contrib.auth.models import User
from Grooving.models import Artist, Customer


class LoginManager(ObtainAuthToken):
    # permission_classes = (IsAuthenticated,)
    queryset = User.objects.all()
    # serializer_class = UserSerializer

    def post(self, request):
        authTokenSerializer = AuthTokenSerializer(data=request.data)
        if authTokenSerializer.is_valid(raise_exception=True):
            user = authTokenSerializer.validated_data['user']
            update_last_login(None, user)
            token, created = Token.objects.get_or_create(user=user)
            if token.key is not None:
                headers = {'x-auth': token.key}
                if Artist.objects.filter(user_id=token.user.id).first() is not None:
                    serialized = LoginSerializer(Artist.objects.get(user_id=token.user.id))
                    return Response(serialized.data, status=status.HTTP_200_OK, headers=headers)
                elif Customer.objects.filter(user_id=token.user.id).first() is not None:
                    serialized = LoginSerializer(Customer.objects.get(user_id=token.user.id))
                    return Response(serialized.data, status=status.HTTP_200_OK, headers=headers)
                return Response({"Artist/Customer not found"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            else:
                return Response({"Token not get/created"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)





