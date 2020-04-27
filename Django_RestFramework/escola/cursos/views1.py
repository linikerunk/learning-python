from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Curso, Avaliacao
from .serializers import CursoSerializer, AvaliacaoSerializer

# Create your views here.


class CursoAPIView(APIView):
    """ API de Curso RESTFRAMEWORK """
    def get(self, request):
        # # print(request.user.email)
        cursos = Curso.objects.all()
        serializer = CursoSerializer(cursos, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CursoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"id": serializer.data['id'], "titulo": serializer.data['titulo']}, status=status.HTTP_201_CREATED)


class AvaliacaoAPIView(APIView):
    """ Outra API para teste """

    def get(self, request):
        # print(request.user.email)
        avaliacao = Avaliacao.objects.all()
        serializer = AvaliacaoSerializer(avaliacao, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AvaliacaoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
