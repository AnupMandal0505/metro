from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken  # Import RefreshToken for JWT blacklisting

class LogoutAPI(APIView):
    def post(self, request):
        # Assuming you're using JWT and the token is included in the request headers
        token = request.headers.get('Authorization').split()[1]

        try:
            decoded_token = RefreshToken(token)
            decoded_token.blacklist()

            return Response({'message': 'Logged out successfully'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)