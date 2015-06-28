import psutil, datetime
import sqlite3
from wsgiref.simple_server import make_server
import re

def server_status_app(environ, start_response):
    #print("ENVIRON:", environ)
    message=""
    status = '200 OK'
    headers = [('Content-type', 'html; charset=utf-8')]
    start_response(status, headers)    

    message += "<table width='40%' border='0'>"
    message += "<tbody>"
    message += "<tr bgcolor='#CEF6F5'>"
    #--------------------------------------- BOOT TIME
    boot_time = datetime.datetime.fromtimestamp(psutil.boot_time()).strftime("%m-%d-%Y %H:%M:%S")

    print("\nBOOT TIME:", boot_time)
    
    message += "<td>BOOT TIME</td>"
    message += "<td>" + boot_time + "</td></tr>"
    
    #--------------------------------------- CPU
    cpu_util = psutil.cpu_percent(interval=1, percpu=True)

    i=1
    print("\nCPU UTILIZATION:")
    message += "<tr><td>CPU UTILIZATION</td>"
    message += "<td><table border='0' width='100%'><tbody>"
    for cpu in cpu_util:
        print("CPU {} : {}%".format(i, cpu))
        message += "<tr><td>CPU " + str(i) + " </td>"
        message += '<td bgcolor="#E2A9F3">' + str(cpu) + "%</td></tr>"
        i+=1

    message += "</tbody></table></td></tr>"
    
    #--------------------------------------- MEMORY
    mem = psutil.virtual_memory()
    THRESHOLD = 100 * 1024 * 1024  # 100MB
    print("\nAVAILABLE MEMORY:", mem.available)
    print("USED MEMORY:", mem.used)
    print("USED PERCENTAGE:", mem.percent)
    
    message += "<tr bgcolor='#CEF6F5'><td>AVAILABLE MEMORY</td>"
    message += "<td>" + str(mem.available) + "</td></tr>"
    message += "<tr><td>USED MEMORY</td>"
    message += "<td>" + str(mem.used) + "</td></tr>"
    message += "<tr bgcolor='#CEF6F5'><td>USED PERCENTAGE</td>"
    message += "<td>" + str(mem.percent) + "</td></tr>"
    
    #--------------------------------------- PROCESSES
    pids = psutil.pids()
    print("\n   PID PROCESS NAME")
    message += "<tr><td>PROCESS ID</td><td>PROCESS NAME</td>"
    for pid in pids:
        p = psutil.Process(pid)
        name = ''
        try:
            name = p.name()
        except:
            pass
        print(repr(pid).rjust(6) + " " + name)
        message += "<tr><td align='right'>" + str(pid) + "</td>"
        message += "<td>" + name + "</td></tr>"

    #--------------------------------------- NETWORK
    net = psutil.net_io_counters(pernic=True)
    netstat = psutil.net_if_stats()
    print("\n         NETWORK STATS            PACKETS R   PACKETS S    ERROR IN   ERROR OUT")
    message += "<tr bgcolor='#CEF6F5'><td>NETWORK STATS</td>"
    message += "<td><table border='0' width='100%'><tbody>"
    message += "<tr><td>CONNECTION</td><td>PACKETS R</td><td>PACKETS S</td><td>ERROR IN</td><td>ERROR OUT</td></tr>"
    for c in netstat:
        if netstat[c].isup:
            print(c.rjust(30) + " : " + repr(net[c].packets_recv).rjust(10) + "  " + repr(net[c].packets_sent).rjust(10) + "  " + repr(net[c].errin).rjust(10) + "  " + repr(net[c].errout).rjust(10)) 
            message += "<tr bgcolor='#FFFFFF'><td>" + c + "</td><td>" + str(net[c].packets_recv) + "</td><td>" + str(net[c].packets_sent) + "</td><td>" + str(net[c].errin) + "</td><td>" + str(net[c].errout) + "</td></tr>"
    message += "</tbody></table></td></tr>"
        
    message += "</tbody></table>"
    return[bytes(message,'utf-8')]

httpd = make_server('', 8000, server_status_app)
print("Serving on port 8000...")

httpd.serve_forever()
