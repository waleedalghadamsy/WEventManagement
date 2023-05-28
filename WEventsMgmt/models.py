from django.db import models

# Create your models here.

class GlobalHelper:
    users = {}
    events = []

class Event(models.Model):
    id = 0 #= models.SmallAutoField()
    name = '' #= models.CharField(max_length=150)
    date = '' #= models.DateField()
    status = 'CREATED' #= models.CharField(7) #TextChoices("CREATED", "PUBLISHED", "HELD")
    regUsers = []
    
    def __init__(self, name, date):
        self.name = name
        self.date = date
        self.status = 'CREATED'
        self.id = len(GlobalHelper.events) + 1
        GlobalHelper.events.append(self)

    def registerUser(self, loginName):
        if len(self.regUsers) == 0 or all(lgNm != loginName for lgNm in self.regUsers):
            self.regUsers.append(loginName)
            return True
        else:
            return False
    
    def publish(self):
        self.status = 'PUBLISHED'

class User(models.Model):
    id = models.IntegerField(default=1, primary_key=True)
    fullName = models.CharField(max_length=75)
    loginName = models.CharField(max_length=25)
    password = models.CharField(max_length=10)
    roleId = models.IntegerField(default=1)

    def __init__(self, fullName, loginName, password, roleId):
        # Check whether already exists
        if not isUserAlreadyRegistered(loginName):
            self.fullName = fullName
            self.loginName = loginName
            self.password = password
            self.roleId = roleId
            #self.id = 888
            self.id = len(GlobalHelper.users) + 1
            GlobalHelper.users[loginName] = self
        else:
            return
    
    def login(self, loginName, password):
        return self.isUserAlreadyRegistered(loginName) and any(usr.password == password for usr in GlobalHelper.usrs.values())

def isUserAlreadyRegistered(loginName):
        return len(GlobalHelper.users) > 0 and loginName in GlobalHelper.users.keys()