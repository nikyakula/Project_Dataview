from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.db import connection
import pyodbc




# Create your views here.
def batchInfo(request):
    connection = pypyodbc.connect('Driver={SQL Server};' 'server=sql-clo-prod.c0cqs7rsnqyl.us-east-1.rds.amazonaws.com;' 'Database= clo_factorydb;' 'uid=clowebuser; pwd=R8b}EtjgP$n_H')
    cursor=connection.cursor()
    #return HttpResponse('Hello world')
    cursor.execute("SELECT batchID FROM rawload.batchException;")
    rows = cursor.fetchall()
    data = []
    for row in rows:
        data.append(row.batchID)
    return render(request, "sampledata.html", {"batch_info": data})
