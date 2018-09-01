from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from django.http import JsonResponse

from .pagination import PageTalhao
from .models import *
from .serializers import *


class TalhaoList(APIView):
    # inserir dados
    def post(self, request):
        try:
            serializer = TalhaoSerializer(data=request.data)

            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except Exception:
            return JsonResponse({"mensagem": "Erro no servidor"},
                                status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    # listagem de todos os dados
    def get(self, request):
        try:

            talhoes_list = Talhao.objects.all()
            paginator = PageTalhao()
            page_result = paginator.paginate_queryset(talhoes_list, request)
            serializer = TalhaoSerializer(page_result, many=True)
            return paginator.get_paginated_response(serializer.data)

        except Exception:

            return JsonResponse({"mensagem": "Erro no servidor"},
                                status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class TalhaoDetail(APIView):
    # busca por id
    def get(self, request, id=0):
        try:

            if id == 0:
                return JsonResponse({"mensagem": "ID inválido"},
                                    status=status.HTTP_400_BAD_REQUEST)

            talhao = Talhao.objects.get(pk=id)
            serializer = TalhaoSerializer(talhao)
            return Response(serializer.data, status=status.HTTP_200_OK)

        except Talhao.DoesNotExist:
            return JsonResponse({"erro": "Talhão não encontrado"},
                                status=status.HTTP_404_NOT_FOUND)
        except Exception:
            return JsonResponse({"mensagem": "Erro no servidor"},
                                status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    # alteração por id
    def put(self, request, id=0):
        try:

            if id == 0:
                return JsonResponse({"mensagem": "ID inválido"},
                                    status=status.HTTP_400_BAD_REQUEST)

            talhao = Talhao.objects.get(pk=id)
            serializer = TalhaoSerializer(talhao, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except Talhao.DoesNotExist:
            return JsonResponse({"erro": "Talhão não encontrado"},
                                status=status.HTTP_404_NOT_FOUND)
        except Exception:
            return JsonResponse({"mensagem": "Erro no servidor"},
                                status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    #     deletar por id
    def delete(self, request, id=0):
        try:
            if id == 0:
                return JsonResponse({"mensagem": "ID inválido"},
                                    status=status.HTTP_400_BAD_REQUEST)
            talhao = Talhao.objects.get(pk=id)
            talhao.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

        except Talhao.DoesNotExist:
            return JsonResponse({"erro": "Talhão não encontrado"},
                                status=status.HTTP_404_NOT_FOUND)
        except Exception:
            return JsonResponse({"mensagem": "Erro no servidor"},
                                status=status.HTTP_500_INTERNAL_SERVER_ERROR)
