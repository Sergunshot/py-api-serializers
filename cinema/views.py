from rest_framework import viewsets

from cinema.models import Genre, Actor, CinemaHall, Movie, MovieSession
from cinema.serializers import (GenreSerializer, ActorSerializer,
                                CinemaHallSerializer,
                                MovieSerializer,
                                MovieSessionSerializer,
                                MovieRetrieveSerializer,
                                MovieListSerializer,
                                MovieSessionListSerializer,
                                MovieSessionRetrieveSerializer,
                                GenreListSerializer,
                                GenreRetrieveSerializer,
                                ActorListSerializer,
                                ActorRetrieveSerializer,
                                CinemaHallListSerializer,
                                CinemaHallRetrieveSerializer)


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

    def get_serializer_class(self):
        if self.action == "list":
            return GenreListSerializer
        elif self.action == "retrieve":
            return GenreRetrieveSerializer
        return GenreSerializer


class ActorViewSet(viewsets.ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer

    def get_serializer_class(self):
        if self.action == "list":
            return ActorListSerializer
        elif self.action == "retrieve":
            return ActorRetrieveSerializer
        return ActorSerializer


class CinemaHallViewSet(viewsets.ModelViewSet):
    queryset = CinemaHall.objects.all()
    serializer_class = CinemaHallSerializer

    def get_serializer_class(self):
        if self.action == "list":
            return CinemaHallListSerializer
        elif self.action == "retrieve":
            return CinemaHallRetrieveSerializer
        return CinemaHallSerializer


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    def get_serializer_class(self):
        if self.action == "list":
            return MovieListSerializer
        elif self.action == "retrieve":
            return MovieRetrieveSerializer
        return MovieSerializer

    def get_queryset(self):
        queryset = self.queryset
        if self.action == "list":
            return (queryset.prefetch_related("genres").
                    prefetch_related("actors"))
        elif self.action == "retrieve":
            return (queryset.prefetch_related("genres").
                    prefetch_related("actors"))
        return queryset


class MovieSessionViewSet(viewsets.ModelViewSet):
    queryset = MovieSession.objects.all()
    serializer_class = MovieSessionSerializer

    def get_serializer_class(self):
        if self.action == "list":
            return MovieSessionListSerializer
        if self.action == "retrieve":
            return MovieSessionRetrieveSerializer
        return MovieSessionSerializer

    def get_queryset(self):
        queryset = self.queryset
        if self.action == "list":
            return (queryset.select_related("cinema_hall").
                    select_related("movie"))
        elif self.action == "retrieve":
            return (queryset.select_related("movie").
                    prefetch_related("movie__genres").
                    prefetch_related("movie__actors"))
        return queryset
