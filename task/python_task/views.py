import json
import MySQLdb
import pandas as pd
from rest_framework import response
from rest_framework.views import APIView


class GetSheet(APIView):

  def post(self,request):
    
    data = pd.read_excel(request.FILES['file'])
    alldata = data.to_json(orient ='records')
    jsonalldata = json.loads(alldata)
    db = MySQLdb.connect( os.environ.get('DB_HOST'), os.environ.get('DB_USER'), os.environ.get('DB_PASSWORD'), os.environ.get('DB_NAME') )
    tblname = str(request.FILES['file']).replace('.xlsx','')
    cols = []
    col=""
    for i in jsonalldata[0].keys():
      v = "_".join(i.split())
      cols.append(v)
    col = ','.join(cols)
          
    insert = db.cursor()
    column = []

    checktbl = "SELECT * FROM information_schema.tables WHERE `table_name` = '{}'"
    tblexist = insert.execute(checktbl.format(tblname))
    if(tblexist == 0):
          
      print("*"*1000)
      for i in jsonalldata[0].keys():
        column.append("_".join(i.split())+' varchar(50)')

      createtbl = "Create table " + tblname+" (" +','.join(column)+')'
      print(createtbl)
      uid = list(jsonalldata[0].keys())
      uniqueindex = "CREATE UNIQUE INDEX "+ uid[0] +" ON "+ tblname+" ("+col+")"
      insert.execute(createtbl)
      insert.execute(uniqueindex)
      db.commit()

    for i in jsonalldata:
      values = []
      for j in i.values():
        values.append(str(j))
      val = '\',\''.join(values)
    
      sqlquery = "INSERT IGNORE INTO " + tblname + " ("+col+") VALUES ("+'\''+val+'\''+")"
      # print(sqlquery)

      insert.execute(sqlquery)
      db.commit()

    return response.Response(jsonalldata)
