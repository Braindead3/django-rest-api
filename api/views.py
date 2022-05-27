from rest_framework import generics, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .permissions import IsAdminOrReadOnly, IsOwnerOrAdminOrReadOnly
from .models import Cloth, Category
from .serializers import ClothSerializer, CategorySerializer


class ClothListCreateView(generics.ListCreateAPIView):
    queryset = Cloth.objects.all()
    serializer_class = ClothSerializer


class ClothUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cloth.objects.all()
    serializer_class = ClothSerializer
    permission_classes = (IsAuthenticated,)


class CategoryCreateView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


# class ClothViewSet(viewsets.ModelViewSet):
#     serializer_class = ClothSerializer
#     permission_classes = (IsOwnerOrAdminOrReadOnly,)
#
#     def get_queryset(self):
#         pk = self.kwargs.get('pk')
#
#         if pk:
#             return Cloth.objects.filter(pk=pk)
#         return Cloth.objects.all()
#
#     @action(methods=['GET'], detail=False)
#     def categories(self, request):
#         categories = Category.objects.all()
#         return Response({'categories': [category.name for category in categories]})

# class ClothView(APIView):
#
#     def get(self, request):
#         cloth = Cloth.objects.all()
#         return Response({'posts': ClothSerializer(cloth, many=True).data}, status=status.HTTP_200_OK)
#
#     def post(self, request):
#         serializer = ClothSerializer(data=request.data)
#         if serializer.is_valid(raise_exception=True):
#             serializer.save()
#             return Response({'post': serializer.data}, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def put(self, request, *args, **kwargs):
#         pk = kwargs.get('pk', None)
#         if not pk:
#             return Response({'error': 'Method PUT not allowed. Pk does not exist.'})
#
#         try:
#             instance = Cloth.objects.get(pk=pk)
#         except:
#             return Response({'error': 'Method PUT not allowed. Object not found.'})
#
#         serializer = ClothSerializer(data=request.data, instance=instance)
#         if serializer.is_valid(raise_exception=False):
#             serializer.save()
#             return Response({'data': serializer.data})
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, request, *args, **kwargs):
#         pk = kwargs.get('pk', None)
#         if not pk:
#             return Response({'error': 'Method PUT not allowed. Pk does not exist.'})
#
#         instance = Cloth.objects.get(pk=pk)
#         instance.delete()
#
#         return Response({'data': 'has been deleted'}, status=status.HTTP_204_NO_CONTENT)
