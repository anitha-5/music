from django.shortcuts import render

# Create your views here.

from rest_framework import generics
from .models import Songs, Playlist, Rating
from .serializers import SongsSerializer, PlaylistSerializer, RatingSerializer
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK,
    HTTP_201_CREATED,
    HTTP_204_NO_CONTENT
)
from rest_framework.response import Response
from django.contrib.auth.decorators import login_required

@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def login(request):
	username = request.data.get("username")
	password = request.data.get("password")
	if username is None or password is None:
		return Response({'error': 'Please provide both username and password'}, status=HTTP_400_BAD_REQUEST)
	user = authenticate(username=username, password=password)
	if not user:
		return Response({'error': 'Invalid Credentials'}, status=HTTP_404_NOT_FOUND)
	token, _ = Token.objects.get_or_create(user=user)
	return Response({'token': token.key}, status=HTTP_200_OK)

@csrf_exempt
@api_view(['GET', 'POST'])
@login_required
def songs_list(request, format=None):
    if request.method == 'GET':
        songs = Songs.objects.all()
        serializer = SongsSerializer(songs, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = SongsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

@csrf_exempt
@api_view(['GET', 'PUT', 'DELETE'])
@login_required
def songs_detail(request, pk, format=None):
    try:
        songs = Songs.objects.get(pk=pk)
    except Songs.DoesNotExist:
        return Response(status=HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = SongsSerializer(songs)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = SongsSerializer(songs, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        songs.delete()
        return Response(status=HTTP_204_NO_CONTENT)

@csrf_exempt
@api_view(['GET', 'POST'])
@login_required
def playlists_list(request, format=None):
    if request.method == 'GET':
        playlists = Playlist.objects.all()
        serializer = PlaylistSerializer(playlists, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = PlaylistSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

@csrf_exempt
@api_view(['GET', 'PUT', 'DELETE'])
@login_required
def playlists_detail(request, pk, format=None):
    try:
        playlists = Playlist.objects.get(pk=pk)
    except Playlist.DoesNotExist:
        return Response(status=HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PlaylistSerializer(playlists)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = PlaylistSerializer(playlists, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        playlists.delete()
        return Response(status=HTTP_204_NO_CONTENT)

@csrf_exempt
@api_view(['GET', 'POST'])
@login_required
def ratings_list(request, format=None):
    if request.method == 'GET':
        ratings = Rating.objects.all()
        serializer = RatingSerializer(ratings, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = RatingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

@csrf_exempt
@api_view(['GET', 'PUT', 'DELETE'])
@login_required
def ratings_detail(request, pk, format=None):
    try:
        ratings = Rating.objects.get(pk=pk)
    except Rating.DoesNotExist:
        return Response(status=HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = RatingSerializer(ratings)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = RatingSerializer(ratings, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        ratings.delete()
        return Response(status=HTTP_204_NO_CONTENT)

@csrf_exempt
@api_view(['GET'])
@login_required
def search(request, format=None):
    if request.method == 'GET':
        songs_list = Songs.objects.all()
        search_song_title = request.query_params.get('title')
        search_song_genre = request.query_params.get('genre')
        search_song_artist = request.query_params.get('artist')
        search_song_album = request.query_params.get('album')
        if search_song_title:
            songs_list = songs_list.filter(title=search_song_title)
        if search_song_genre:
            songs_list = songs_list.filter(genre=search_song_genre)
        if search_song_artist:
            songs_list = songs_list.filter(artist=search_song_artist)
        if search_song_album:
            songs_list = songs_list.filter(album=search_song_album)
        serializer = SongsSerializer(songs_list, many=True)
        return Response(serializer.data)

