from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Movie,Rewiew,Director
from .serializers import MovieSerializers,DirectorSerializers,RewiewSerilizers
from rest_framework import status

@api_view(['GET'])
def movie_detail_api_view(request,id):
    try:
        movie = Movie.objects.get(id=id)
    except Movie.DoesNotExist:
        return Response(data={'error':'Movie not found!'},
                        status=status.HTTP_404_NOT_FOUND)
    data = MovieSerializers(movie).data
    return Response(data=data)

@api_view(['GET'])
def movie_list_api_view(request):
    movie = Movie.objects.all()
    data = MovieSerializers(movie,many=True).data
    return Response(data=data)




@api_view(['GET'])
def director_detail_api_view(request,id):
    try:
        director = Director.objects.get(id=id)
    except Director.DoesNotExist:
        return Response(data={'error':'Director not found!'},
                        status=status.HTTP_404_NOT_FOUND)
    data = DirectorSerializers(director).data
    return Response(data=data)


@api_view(['GET'])
def director_list_api_view(request):
    director = Director.objects.all()
    data = DirectorSerializers(director,many=True).data
    return Response(data=data)



@api_view(['GET'])
def rewiew_detail_api_view(request,id):
    try:
        rewiew = Rewiew.objects.get(id=id)
    except Rewiew.DoesNotExist:
        return Response(data={'error':'Rewiew not found!'},
                        status=status.HTTP_404_NOT_FOUND)
    data = RewiewSerilizers(rewiew).data
    return Response(data=data)



@api_view(['GET'])
def rewiew_list_api_view(request):
    rewiew = Rewiew.objects.all()
    data = RewiewSerilizers(rewiew,many=True).data
    return Response(data=data)

