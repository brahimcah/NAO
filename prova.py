#-*- coding: utf-8 -*-

import socket
import os
import threading

import urllib.parse
import ctypes
import datetime


local_ip = '172.16.252.96' # Configure la IP local vinculada al servidor de socket
local_port = 4321 # Configure el puerto local vinculado al servidor de socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((local_ip, local_port))
server.listen(5)

 # Solo responda a tareas de computadoras en la lista blanca
 # clave () de admin_filter
admin_filter = {}
admin_filter['172.19.1.30'] = {'exe'}
admin_filter['127.0.0.1'] = {'exe'}


print('White list:' + str(admin_filter))
print('Server bind on %s:%s' % (local_ip, str(local_port)))
print('-----------------Server starting success-----------------')


def exe_prog(msg):
         # La ruta consta de espacios y comillas muy bien -_- !!!!!
    #os.system(u"\"C:\Program Files (x86)\TTPlayer\TTPlayer.exe\"".encode("gbk"))
    os.system(msg)
    # os.system("C:\ProgramData\Anaconda3\envs\py2\python.exe F:\\source_files\\quant\\remote_pc_control\\exe_calc.py")

while 1:
    conn, addr = server.accept()
    msg = urllib.parse.unquote(conn.recv(1024).decode('utf-8'))
    
    peer_name = conn.getpeername()
    sock_name = conn.getsockname()

         # peer_name es una tupla, peer_name [0] es la ip y peer_name [1] es el número de puerto
    now_dt = str(datetime.datetime.now())
    print(u'%s, visitor: %s:%s'%(now_dt, peer_name[0],peer_name[1])) # , sock_name
         # Llamada lista blanca, verificación de permisos de administrador
    if peer_name[0] in admin_filter.keys():
        print(msg)
        if '"quit"' == msg: # puede ser 'quit' puede ser '"quit"' ... verifíquelo usted mismo
            conn.close()
            exit(0)
        t = threading.Thread(target=exe_prog,args=(msg,))
        t.start()

    #conn.send('server: I received '+msg)