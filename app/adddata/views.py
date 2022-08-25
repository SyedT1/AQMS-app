from django.shortcuts import render
import mysql.connector
# Create your views here.
def addAQI(request):
    # dwell = request.GET["division"]
    # print('jolonto dolil lives in {}'.format(dwell))
    return render(request,'adddata/a1.html')
  #return render(request,'adddata/a1.html')
  
  
def showpage(request):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="123456",
        database="testdb"
    )
    mycursor = mydb.cursor()
    mycursor.execute("INSERT INTO divs(division) VALUES('{}')".format(mycursor))
    return render(request,'adddata/a1.html')