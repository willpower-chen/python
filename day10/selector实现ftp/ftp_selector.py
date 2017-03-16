import selectors
import socket
import os,json


def put(self, *args):
    '''接收客户端文件'''
    cmd_dic = args[0]
    filename = cmd_dic["filename"]
    filesize = cmd_dic["size"]
    if os.path.isfile(filename):
        f = open(filename + ".new", "wb")
    else:
        f = open(filename, "wb")

    self.send(b"200 ok")
    received_size = 0
    while received_size < filesize:
        data = self.request.recv(1024)
        f.write(data)
        received_size += len(data)
    else:
        print("file [%s] has uploaded..." % filename)


def accept(sock, mask):
    conn, addr = sock.accept()  # Should be ready
    # print('accepted', conn, 'from', addr,mask)
    conn.setblocking(False)
    sel.register(conn, selectors.EVENT_READ, read) #新连接注册read回调函数


def read(conn, mask):
    try:
        data = conn.recv(1024).strip()  # Should be ready
        cmd_dic = json.loads(data.decode())
        action = cmd_dic["action"]
        if hasattr( conn,action):
            func = getattr( conn,action)
            func(cmd_dic)
        if data:
            # print('echoing', repr(data), 'to', conn)
            conn.send(data)  # Hope it won't block
        else:
            print('closing', conn)
            sel.unregister(conn)
            conn.close()
    except ConnectionResetError as e:
        print("err", e)




sel = selectors.DefaultSelector()
sock = socket.socket()
sock.bind(('localhost', 9999))
sock.listen(1000)
sock.setblocking(False)
sel.register(sock, selectors.EVENT_READ, accept)

while True:
    events = sel.select() #默认阻塞，有活动连接就返回活动的连接列表
    for key, mask in events:
        callback = key.data #accept
        callback(key.fileobj, mask) #key.fileobj=  文件句柄