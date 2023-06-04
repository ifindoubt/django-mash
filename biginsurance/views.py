# Create your views here.

from rest_framework.response import Response
from rest_framework import status, generics
from .models import Client as ClientView
from .serializers import ClientSerializer
import math
from datetime import datetime

class ClientSpecs(generics.GenericAPIView):
    serializer_class = ClientSerializer
    queryset = ClientView.objects.all()

    def get(self, request):
        page_num = int(request.GET.get("page", 1))
        limit_num = int(request.GET.get("limit", 10))
        start_num = (page_num - 1) * limit_num
        end_num = limit_num * page_num
        search_param = request.GET.get("search")
        clients = ClientView.objects.all()
        total_clients = clients.count()
        if search_param:
            clients = clients.filter(title__icontains=search_param)
        serializer = self.serializer_class(clients[start_num:end_num], many=True)
        return Response({
            "status": "success",
            "total": total_clients,
            "page": page_num,
            "last_page": math.ceil(total_clients / limit_num),
            "clients": serializer.data
        })

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer == "date_of_birth":
            ClientView.change_date_format(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": {"clients": serializer.data}}, status=status.HTTP_201_CREATED)
        else:
            return Response({"status": "fail", "message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class ClientDetail(generics.GenericAPIView):
    queryset = ClientView.objects.all()
    serializer_class = ClientSerializer

    def get_client(self, pk):
        try:
            return ClientView.objects.get(pk=pk)
        except:
            return None

    def get(self, request, pk):
        clients = self.get_client(pk=pk)
        if clients == None:
            return Response({"status": "fail", "message": f"Client with Id: {pk} not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = self.serializer_class(clients)
        return Response({"status": "success", "data": {"clients": serializer.data}})

    def update(self, request, pk):
        clients = self.get_client(pk)
        if clients == None:
            return Response({"status": "fail", "message": f"Client with Id: {pk} not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = self.serializer_class(
            clients, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.validated_data['updatedAt'] = datetime.now()
            serializer.save()
            return Response({"status": "success", "data": {"clients": serializer.data}})
        return Response({"status": "fail", "message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        clients = self.get_client(pk)
        if clients == None:
            return Response({"status": "fail", "message": f"Client with Id: {pk} not found"}, status=status.HTTP_404_NOT_FOUND)

        clients.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)