from django.shortcuts import render
from rest_framework import viewsets,status
from .models import Service,Rating
from .serializers import ServiceSerializer,RatingSerializer,UserSerializer
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework.decorators import action
from rest_framework.authentication import TokenAuthentication
from django.contrib.auth.models import User


# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer



class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated,)

    @action(detail=True, methods=['POST'])
    def rate_service(self, request,pk=None):
        if 'stars' in request.data:
            service=Service.objects.get(id=pk)
            stars=request.data['stars']
            user=request.user
            #print('user',user)
            #user=User.objects.get(id=1) => fixed
            #print('user',user.username)

            try:
                rating=Rating.objects.get(user=user.id,service=service.id)
                rating.stars=stars
                rating.save()
                serializer=RatingSerializer(rating,many=False)
                response = {'message': 'Rating updated','result':serializer.data}
                return Response(response, status=status.HTTP_200_OK)
            except:
                rating=Rating.objects.create(user=user, service=service,stars=stars)
                serializer = RatingSerializer(rating, many=False)
                response = {'message': 'Rating created', 'result': serializer.data}
                return Response(response, status=status.HTTP_200_OK)


        else:
            response = {'message': 'you need to rate the service'}
            return Response(response, status=status.HTTP_400_BAD_REQUEST)



class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def update(self, request, *args, **kwargs):
        response = {'message': 'you cant update rating like that '}
        return Response(response, status=status.HTTP_400_BAD_REQUEST)

    def create(self, request, *args, **kwargs):
        response = {'message': 'you cant create rating like that '}
        return Response(response, status=status.HTTP_400_BAD_REQUEST)