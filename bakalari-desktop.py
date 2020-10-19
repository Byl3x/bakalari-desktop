#!/usr/bin/python
import gi
import requests
gi.require_version("Gtk", "3.0")
gi.require_version('WebKit2', '4.0')
from gi.repository import Gtk
from gi.repository import WebKit2 as WebKit
import gettoken
server = "<server>"
username = "<username>"
password = "<heslo>"
class BearerAuth(requests.auth.AuthBase):
    def __init__(self, token):
        self.token = token
    def __call__(self, r):
        r.headers["authorization"] = "Bearer " + self.token
        return r

maintoken = gettoken.getAccessToken(server, username, password)
logintoken = gettoken.getLoginToken(server, maintoken[0])
def updateToken(accesstoken):
    global maintoken
    maintoken = gettoken.refreshToken(server, maintoken[1])
    return maintoken

def getAverageGrades(accesstoken):
    try:
        returnstr= ""
        response = requests.get(server+"/3/marks", auth=BearerAuth(accesstoken[0])).json()
        gradesbysubject = response['Subjects']
        count = 0
        for i in gradesbysubject:
            marks = gradesbysubject[count]
            count += 1
            subjectdata = marks["Subject"]
            averagegrade = marks["AverageText"]
            subjectname = subjectdata["Name"]
            returnstr += subjectname+": "+averagegrade+"\n"
            if returnstr == "":
                returnstr = "No grades"
        return returnstr
    except: updateToken(maintoken)
def getAllGrades(accesstoken):
    returnstr=""
    response = requests.get(server+"/3/marks", auth=BearerAuth(accesstoken[0])).json()
    gradesbysub = response["Subjects"]
    j = 0
    k = 0
    for i in gradesbysub:
        subject = gradesbysub[j]
        subdata = subject["Subject"]
        subjectname = subdata["Name"]
        marks = subject["Marks"]
        j += 1
        returnstr += "<big><b>"+subjectname+"</b></big>\n"
        k = 0
        for i in marks:
            actmarks = marks[k]
            k += 1
            number = actmarks["MarkText"]
            weight = actmarks["Weight"]
            markstr = str(number)
            returnstr += "Grade: "+markstr+" Weight: "+str(weight)+"\n"
    return returnstr

def getAllHomework(accesstoken):
    try:
        response = requests.get(server+"/3/homeworks", auth=BearerAuth(accesstoken[0])).json()
        response = str(response)+"\nFor some reason, this doesn't work"
        return response
    except: updateToken(maintoken)
def getUserInfo(accesstoken):
    try:
        response = requests.get(server+"/3/user", auth=BearerAuth(accesstoken[0])).json()
        parsedresponse = "Name and class: "+response['FullName']+"\n"
        parsedresponse = parsedresponse+ "School Name: "+response['SchoolOrganizationName']+"\n"
        parsedresponse = parsedresponse+"User Account Type: "+response['UserTypeText']+"\n"
        parsedresponse = parsedresponse+"Study Year: "+str(response['StudyYear'])+"\n"
        return parsedresponse
    except: updateToken(maintoken)
class Handler:
    def showgrades(self, button):
        print("Showing Grades...")
        g1label.set_text(str(getAverageGrades(maintoken)))
    def showhomework(self, button):
        print("Showing Homework...")
        hwlabel.set_text(str(getAllHomework(maintoken)))
    def showuserinfo(self, button):
        print("Showing User Info...")
        ilabel.set_text(getUserInfo(maintoken))
    def showtimetable(self, button):
        print("Showing Timetable")
        browser.load_uri("https://www.gvp.cz/info/Timetable/Public/Actual/Class/XA")
    def updatetoken(self, button):
        updateToken(maintoken)
        print("Updating Token...")
    def showallgrades(self, button):
        print("Showing All Grades...")
        g2label.set_markup(str(getAllGrades(maintoken)))
builder = Gtk.Builder() 
builder.add_from_file("bakadesktop.glade") 
builder.connect_signals(Handler()) 
window = builder.get_object("mainwindow")
hwlabel = builder.get_object("homeworklabel")
g1label = builder.get_object("avggradelabel")
g2label = builder.get_object("allgradelabel")
ilabel = builder.get_object("infolabel")
browser = WebKit.WebView()
browser.set_editable(False)
scrolled_win = builder.get_object("browserwindow")
scrolled_win.add(browser)
window.set_default_size(1280,720)
window.show_all()
browser.show()
Gtk.main()
