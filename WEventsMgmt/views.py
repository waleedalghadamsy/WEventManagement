import json
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import status
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.response import Response
from WEventsMgmt import models
from .forms import AddUserForm, CreateEventForm
from .serializers import UserSerializer
from WEventsMgmt import usersdbops
# Create your views here.

def index(request):
    #return HttpResponse("Yes. It is working well.")
    '''
    context = {
        "data": "This is from views code",
        "users": ["Waleed", "عبد الرزاق", "Ahmad", "Mahmood"],
        "events": ["E1", "Another", "Third"]
    }
    return render(request, "index.html", context)
    '''
    return render(request, "index.html")

def about(request):
    return HttpResponse("<h1>Welcome to the Events Management Project</h1>")

def usersIndex(request):
    #return HttpResponse("This is Users Index -- No. of users {0}".format(len(models.GlobalHelper.users)))
    allUsers = usersdbops.getAllUsers()

    context = { "theusers": allUsers }
    return render(request, "userstemplates/index.html", context)

def addNewUser(request):
    #return HttpResponse("Add New User page")
    form = AddUserForm()
    if request.method == "POST":
        form = AddUserForm(request.POST)

        flNm = form.cleaned_data['name']
        lgnNm = form.cleaned_data['loginName']
        pswrd = form.cleaned_data['password']

        newUser = models.User(flNm, lgnNm, pswrd)
    return render(request, "userstemplates/adduser.html", {'form': form})

def usersignin(request):
    return True

def eventsIndex(request):
    #return HttpResponse("Events Index -- No. of events {0}".format(len(models.GlobalHelper.events)))
    context = {
        "someevents": ["Ev1", "Second", "الثالث"]
    }
    return render(request, "eventstemplates/index.html", context)

def createNewEvent(request):
    #return HttpResponse("Create New Event")
    form = CreateEventForm()
    if request.method == "POST":
        form = CreateEventForm(request.POST)
        newEvent = models.Event()
        newEvent.name = form.cleaned_data['name']
        newEvent.date = form.cleaned_data['eventdate']
    return render(request, "eventstemplates/createevent.html", {'form': form})

def addUserToEvent(request):
    return HttpResponse("Add User to Event")

@api_view(['GET', 'POST'])
def usersAPIView(request):
    if request.method == 'GET':
        allUsers = models.User.objects.all
        serUsers = UserSerializer(allUsers)
        return Response(serUsers.data, status=status.HTTP_200_OK)
    
    elif request.method == 'POST':
        rcdUser = JSONParser.parse(request)
        serUser = UserSerializer(data=rcdUser)
        if serUser.is_valid():
            serUser.save()
            return Response(serUser.data, status=status.HTTP_201_CREATED)
        return Response(serUser.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def userDetailsAPIView(request, userId):
        #aUser = models.User.objects.get(id=userId)
        aUser = usersdbops.getUserById(userId=userId)

        if request.method == 'GET':
            serUser = UserSerializer(aUser)
            return Response(serUser.data)
        
        elif request.method == 'PUT':
            serUser = UserSerializer(aUser, data=request.data)
            if serUser.is_valid():
                serUser.save()
                return Response(serUser.data)
            return Response(serUser.errors, status=status.HTTP_400_BAD_REQUEST)
        
        elif request.method == 'DELETE':
            aUser.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def test1APIView(request):
    return Response("This is from Django test API")

@api_view(['GET'])
def test2APIView(request, name):
    return Response("كيف حالك يا {0}".format(name))

@api_view(['GET'])
def test3APIView(request):
    exmplUser = models.User("وليد الغدامسي", "waleed", "abcxyz", 99)
    xmplSerUser = UserSerializer(exmplUser)
    return Response(xmplSerUser.data)

@api_view(['POST'])
def test4APIView(request):
    #rcvdJsonUser = json.loads(request.body)
    #newUser = models.User(**rcvdJsonUser)
    #print("Test4 Request contents")
    #print(request.data)

    print("Test4 Request content type")
    print(request.content_type)
    print("-----")
    print("Test4 Request content")
    print(request.POST)

    newUser = deserializeUser(request.POST)

    if newUser is not None:
        return Response("User {0} successfully received".format(newUser.fullName), status=status.HTTP_201_CREATED)
    else:
        return Response("Error while instantiating user from JSON", status=status.HTTP_417_EXPECTATION_FAILED)

@api_view(['POST'])
def test5APIView(request):
    #rcvdJsonUser = json.loads(request.body)
    #newUser = models.User(**rcvdJsonUser)

    print("Test5 Request content type")
    print(request.content_type)
    print("-----")
    print("Test5 Request content")
    print(request.POST)

    newUser = deserializeUser(request.POST)

    if newUser is not None:
        nRows = usersdbops.addUserToDb(newUser)
        if nRows > 0:
            return Response("User {0} successfully stored to DB".format(newUser.fullName), status=status.HTTP_201_CREATED)
        else:
            return Response("Error while storing user to DB", status=status.HTTP_417_EXPECTATION_FAILED)
    else:
        return Response("Error while instantiating user from JSON", status=status.HTTP_417_EXPECTATION_FAILED)

def deserializeUser(jsonUser):
    jsonUsrDict = json.loads(jsonUser)
    aUser = models.User(**jsonUsrDict)
    return aUser