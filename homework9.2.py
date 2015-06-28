import sqlite3
from wsgiref.simple_server import make_server
import re

def hello_world_app(environ, start_response):
    #print("ENVIRON:", environ)
    message=""
    status = '200 OK'
    headers = [('Content-type', 'html; charset=utf-8')]
    start_response(status, headers)
    if(len(environ['QUERY_STRING'])>1):
        message += "<br> Your data has been recieved:"
        animal=''
        count=''
        for param in environ['QUERY_STRING'].split("&"):
            message += "<br>"+param
            sparam = param.split("=")
            if sparam[0] == "animal":
                animal = sparam[1]
            elif sparam[0] == "count":
                count = sparam[1]
        conn = sqlite3.connect("zoo.sqlite") #create connection to zoo.sqlite database, creates the database if it doesn't already exist
        cursor = conn.cursor() #provides are cursor to the above connection (the means of executing the SQL queries)
        try:
            cursor.execute("create table animal_count (name text, count integer)") #execute the create table query
        except Exception as e:
            print(e)
        cursor.execute("insert into animal_count(name, count) values('" + animal + "', " + count + ")")
        conn.commit()
        conn.close()
    message += "<h1>Welcome to the Zoo</h1>"
    message += "<form><br>Animal:<input type=text name='animal'>"
    message += "<br><br>Count:<input type=text name='count'>"
    message += "<br><br><input type='submit' name='Submit' ></form>"
    return[bytes(message,'utf-8')]


httpd = make_server('', 8000, hello_world_app)
print("Serving on port 8000...")

httpd.serve_forever()
