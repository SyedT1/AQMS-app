from django.shortcuts import render
from django.http import HttpResponse
import mysql.connector
from django.shortcuts import render
from plotly.offline import plot
from plotly.graph_objs import Scatter
import plotly.express as px
import pandas as pd
# def index(request):
#     x_data = [0,1,2,3]
#     y_data = [x**2 for x in x_data]
#     plot_div = plot([Scatter(x=x_data, y=y_data,
#                         mode='lines', name='test',
#                         opacity=0.8, marker_color='green')],
#                output_type='div')
#     return render(request, "loadchart/ajaira.html", context={'plot_div': plot_div})


def index(request):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="123456",
        database="testdb"
    )
    mycursor = mydb.cursor()
    mycursor.execute("select AVG(PM25) as PM25, YEAR(time) as Year  from testdb.aqi_table group by Year")
    data = mycursor.fetchall()
    df = pd.DataFrame(data)
    fig = px.bar(df,x =1, y=0,title='Yearly Average AQI',labels={
                     '1': "Year",
                     '0' : "Average PM2.5"
                 },log_x=False, log_y=False)
    fig.update_layout(xaxis={'dtick': 1})
    return render(request, "loadchart/barchart.html", context={'re':fig.show()})
    # myresult = mycursor.fetchall()
    # arr = myresult[0]
    # context =  {
    #     'time':arr[0],
    #     'PM25':arr[1],
    #     'avg_temp':arr[2],
    #     'rain_precp':arr[3],
    #     'wind_spd':arr[4],
    #     'visibility':arr[5],
    #     'cloud_cov':arr[6],
    #     'rela_hum':arr[7],
    #     'division':arr[9]
    # }
    # df = pd.DataFrame(dict(
    #    x = [1, 3, 2, 4],
    #    y = [1, 2, 3, 4]
    # ))
    # fig = px.line(df, x="year", y="lifeExp", color='country')
    # return render(request, "loadchart/ajaira.html", context={'re':fig.show()})


def goto(request):
    dwell = request.GET["country"]
    context = {
        'country':dwell
    }
    return render(request,'loadchart/something.html',context)


def showhome(request):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="123456",
        database="testdb"
    )
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM aqi_table WHERE Division='Dhaka' ORDER BY time DESC LIMIT 1")
    myresult = mycursor.fetchall()
    arr = myresult[0]
    context =  {
        'time':arr[0],
        'PM25':arr[1],
        'avg_temp':arr[2],
        'rain_precp':arr[3],
        'wind_spd':arr[4],
        'visibility':arr[5],
        'cloud_cov':arr[6],
        'rela_hum':arr[7],
        'division':arr[9]
    }
    return render(request,'loadchart/home.html',context)