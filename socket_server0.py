# -*- coding: utf-8 -*-
#2020/5/12/21:58 laptop
import socket
import time
import socket_app

HOST = '172.16.0.4'
PORT = 9999

class User:
        empCount = 0
        def __init__(self, time, name, speed, intensity, angle):
                self.time = time
                self.name = name
                self.trainSpeed = speed
                self.trainIntensity = intensity
                self.trainAngle = angle
                User.empCount += 1

        def displayUser(self):
                print('>>>>>>>Current training data:<<<<<<<')
                print('Training time:', self.time, '\nUser name:', self.name, '\nTraining speed:', self.trainSpeed, '\nTraining intensity:', self.trainIntensity, '\nTraining angle:', self.trainAngle)

def socket_conn():
    print('Connection being established...')
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
    sock.bind((HOST, PORT))
    sock.listen(5)
    conn, addr = sock.accept()
    s = conn.recv(1024).decode()
    if s:
        print('Message from raspi:', s)
    return conn

def socket_data():
    conn = socket_conn()
    conn.send('START'.encode())       #启动信号
    time.sleep(0.2)
    data_json = socket_app.data()
    print('Training data acquired.')
    startFlag = data_json[16:17]      #将字符串中的内容逐个解析出来
    DOFlag = data_json[37:41]
    speed = data_json[56:64]          #speed intensity angle是随便取名字的属性，就是把几个挡位信息存了进去，具体传入还需要转换格式，以刘禹锋为准
    CEFlag = data_json[76:80]
    intensity = data_json[95:103]
    UPFlag = data_json[115:119]
    angle = data_json[134:142]
    print('Data analysis completed')
    while startFlag != '1':          #原地等待开始命令
        data_json
    print('Sending data to Rasbpi...')
    name = 'xuziyitest'
    Time = time.asctime(time.localtime(time.time()))
    print(data_json)
    time.sleep(1)
    print("test")
    conn.send("test".encode())
    print("quit")
    time.sleep(1)
    conn.send("quit".encode())
    if DOFlag:
        conn.send(speed.encode())
        print(DOFlag)
    time.sleep(0.5)
    if CEFlag:
       	conn.send(intensity.encode())
        print(CEFlag)
    time.sleep(0.5)
    if UPFlag == 'True':
        conn.send(angle.encode())     #单次训练参数传送完毕

    user1 = User(Time, name, speed, intensity, angle)   #估计莫得必要
    user1.displayUser()                #display本无用，调试的多了，也便有了用
    while True:
        time.sleep(0.2)
        s = input('>>:')   #等待停止信号，具体实现方式有待考虑
        if s:
            conn.send(s.encode())
        if s == 'quit':
            time.sleep(0.2)     #树莓派端略慢，防止数据误读
            conn.send(s.encode())
            time.sleep(0.1)
            break;
    conn.close;
    print("end")
    #sock.close;

def main():
    socket_data()

if __name__ == '__main__':
    main()
