from WEventsMgmt import models
from WEventsMgmt import dbconnect

def getAllUsers():
    crsr = dbconnect.postgresConnect()
    crsr.execute("SELECT * FROM public.Users")
    return crsr.fetchall()

def addUserToDb(user):
    crsr = dbconnect.postgresConnect()
    crsr.execute("INSERT INTO public.Users VALUES({0}, '{1}', '{2}', '{3}', {4})".format(user.Id, user.fullName, user.loginName, user.password, user.roleId))

def addExampleUserToDb():
    crsr = dbconnect.postgresConnect()
    crsr.execute("INSERT INTO public.Users VALUES(10000, 'User 10000', 'login10000', 'pw10000', 99")
    return crsr.rowcount

def getUserById(userId):
    crsr = dbconnect.postgresConnect()
    crsr.execute("SELECT * FROM public.Users WHERE Id = {0}".format(userId))
    return crsr.fetchone()

