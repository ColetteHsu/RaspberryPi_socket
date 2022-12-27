import RPi.GPIO as GPIO
import time
  
def Setup(GPIOnum , OUT_IN) :
    GPIO.setmode(GPIO.BCM)
    
    if OUT_IN == "OUT":
        GPIO.setup(GPIOnum, GPIO.OUT)
    else:
        GPIO.setup(GPIOnum, GPIO.IN)
        
def TurnOnLED(GPIOnum) :
    GPIO.output(GPIOnum,True)

def TurnOffLED (GPIOnum):
    GPIO.output(GPIOnum,False)
    
def GetGPIOStatus(GPIOnum):
    GPIO_State = GPIO.input(GPIOnum)
    return GPIO_State

if __name__ == "__main__":
    try:
        Setup(2, "OUT")
        Setup(3, "OUT")
        Setup(4, "OUT")
        while True:
            TurnOnLED(2) #亮綠燈
            time.sleep(1) #亮1秒
            TurnOffLED(2) #關綠燈
            time.sleep(1) #關1秒
            
            for i in range(0,5): #建立for跑五次的迴圈
                if i<5:          
                    TurnOnLED(3) #亮黃燈
                    time.sleep(0.2) #亮0.2秒
                    TurnOffLED(3) #關黃燈
                    time.sleep(1) #關1秒
            
            TurnOnLED(4) #亮紅燈
            time.sleep(2) #亮2秒
            TurnOffLED(4) #關紅燈
            time.sleep(1) #關1秒
    except KeyboardInterrupt:
            GPIO.cleanup()
    