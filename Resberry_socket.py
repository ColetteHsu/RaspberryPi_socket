import socket
import RPi.GPIO as GPIO
import LED

bind_ip="172.20.10.3" #resberrypi ip addr.
bind_port=8888

server=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind(bind_ip, bind_port)
server.listen(5)
print("Listening on %s:%d"%(bind_ip, bind_port))

LED.Setup(2, "OUT")
LED.Setup(3, "OUT")
LED.Setup(4, "OUT")

try:
    client, addr=server.accept() #client端輸入resberrypi addr. and connect
    print("Acepted connection from: &s:%d" % (addr[0],addr[1]))
    
    LED.TrunOffLED(2) #待連線後先將所有燈關閉
    LED.TrunOffLED(3)
    LED.TrunOffLED(4)
    
    while True:

        data=client.recv(1024)
        print(data)
        if data ==b'ron':
            LED.TurnOnLED(2)
        
        elif data==b'yon':
            LED.TurnOnLED(3)

        elif data==b'gon':
            LED.TurnOnLED(4)
        
        elif data==b'allon':
            LED.TurnOnLED(2)
            LED.TurnOnLED(3)
            LED.TurnOnLED(4)
            
        elif data==b'roff':
            LED.TurnOffLED(2)

        elif data==b'yoff':
            LED.TurnOffLED(3)

        elif data==b'goff':
            LED.TurnOffLED(4)
        
        elif data==b'alloff':
            LED.TurnOffLED(2)
            LED.TurnOffLED(3)
            LED.TurnOffLED(4)
            
except KeyboardInterrupt:
    client_socket.close()
    GPIO.cleanup()

