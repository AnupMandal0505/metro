from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from app.models import Client
from app.serializers.ClientSerializer import ClientSerializer

class ClientAPIView(APIView):
    def get(self, request, pk=None):
        """
        Retrieve all clients or a specific client by ID.
        """
        if pk:
            try:
                client = Client.objects.get(pk=pk)
                serializer = ClientSerializer(client)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except Client.DoesNotExist:
                return Response({"error": "Client not found."}, status=status.HTTP_404_NOT_FOUND)
        else:
            clients = Client.objects.all()
            serializer = ClientSerializer(clients, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        """
        Create a new client.
        """
        serializer = ClientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        """
        Update an existing client by ID.
        """
        try:
            client = Client.objects.get(pk=pk)
        except Client.DoesNotExist:
            return Response({"error": "Client not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = ClientSerializer(client, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        """
        Delete a client by ID.
        """
        try:
            client = Client.objects.get(pk=pk)
        except Client.DoesNotExist:
            return Response({"error": "Client not found."}, status=status.HTTP_404_NOT_FOUND)

        client.delete()
        return Response({"message": "Client deleted successfully."}, status=status.HTTP_204_NO_CONTENT)
