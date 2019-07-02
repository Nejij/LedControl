import RPi.GPIO as GPIO
import time

redFront = 15
greenFront = 4
blueFront = 14
redBack = 18
greenBack = 17
blueBack = 27

fanPin = 10

#set pins to output mode
def setupPins():
    
    GPIO.setmode(GPIO.BCM)

    GPIO.setup(redFront, GPIO.OUT)
    GPIO.setup(greenFront, GPIO.OUT)
    GPIO.setup(blueFront, GPIO.OUT)
    GPIO.setup(redBack, GPIO.OUT)
    GPIO.setup(greenBack, GPIO.OUT)
    GPIO.setup(blueBack, GPIO.OUT)
    
    GPIO.setup(fanPin, GPIO.OUT)
    
    return;

#apply 3.3v to GPIO pin
def pinOn( pin ):
    
    GPIO.output(pin, GPIO.HIGH)
    
    return;

#removes voltage from pin
def pinOff( pin ):
    
    GPIO.output(pin, GPIO.LOW)
    
    return;

def setPrimaries( r, g, b, location = 'all' ):
    if location == 'front':
        if r:
            pinOn(redFront)
        else:
            pinOff(redFront)
        if g:
            pinOn(greenFront)
        else:
            pinOff(greenFront)
        if b:
            pinOn(blueFront)
        else:
            pinOff(blueFront)
    elif location == 'back':
        if r:
            pinOn(redBack)
        else:
            pinOff(redBack)
        if g:
            pinOn(greenBack)
        else:
            pinOff(greenBack)
        if b:
            pinOn(blueBack)
        else:
            pinOff(blueBack)
    elif location == 'all':
        if r:
            pinOn(redFront)
            pinOn(redBack)
        else:
            pinOff(redFront)
            pinOff(redBack)
        if g:
            pinOn(greenFront)
            pinOn(greenBack)
        else:
            pinOff(greenFront)
            pinOff(greenBack)
        if b:
            pinOn(blueFront)
            pinOn(blueBack)
        else:
            pinOff(blueFront)
            pinOff(blueBack)
    else:
        print('error, no lights in the specified location')
        
    return;

def lightsOff():
    
    setPrimaries( location = 'front', r = False, g = False, b = False)
    setPrimaries( location = 'back', r = False, g = False, b = False)
    
    return;
    
def lightsOn():
    
    setPrimaries( location = 'front', r = True, g = True, b = True)
    setPrimaries( location = 'back', r = True, g = True, b = True)
    
    return;
    
def setColour( colour, location = 'all' ):
    if location == 'all':
        if colour is "red":
            setPrimaries( r = True, g = False, b = False)
        if colour is "yellow":
            setPrimaries( r = True, g = True, b = False)
        if colour is "green":
            setPrimaries( r = False, g = True, b = False)
        if colour is "cyan":
            setPrimaries( r = False, g = True, b = True)
        if colour is "blue":
            setPrimaries( r = False, g = False, b = True)
        if colour is "purple":
            setPrimaries( r = True, g = False, b = True)
        if colour is "white":
            setPrimaries( r = True, g = True, b = True)
    elif location == 'front':
        if colour is "red":
            setPrimaries( location = 'front', r = True, g = False, b = False)
        if colour is "yellow":
            setPrimaries( location = 'front', r = True, g = True, b = False)
        if colour is "green":
            setPrimaries( location = 'front', r = False, g = True, b = False)
        if colour is "cyan":
            setPrimaries( location = 'front', r = False, g = True, b = True)
        if colour is "blue":
            setPrimaries( location = 'front', r = False, g = False, b = True)
        if colour is "purple":
            setPrimaries( location = 'front', r = True, g = False, b = True)
        if colour is "white":
            setPrimaries( location = 'front', r = True, g = True, b = True)
    elif location == 'back':
        if colour is "red":
            setPrimaries( location = 'back', r = True, g = False, b = False)
        if colour is "yellow":
            setPrimaries( location = 'back', r = True, g = True, b = False)
        if colour is "green":
            setPrimaries( location = 'back', r = False, g = True, b = False)
        if colour is "cyan":
            setPrimaries( location = 'back', r = False, g = True, b = True)
        if colour is "blue":
            setPrimaries( location = 'back', r = False, g = False, b = True)
        if colour is "purple":
            setPrimaries( location = 'back', r = True, g = False, b = True)
        if colour is "white":
            setPrimaries( location = 'back', r = True, g = True, b = True)
    else:
        print('error, no lights in the specified location')
            
    return;

def rainbow(onTime = 1.5):
    
    try:
        while True:
            setColour('red')
            time.sleep(onTime)
            setColour('yellow')
            time.sleep(onTime)
            setColour('green')
            time.sleep(onTime)
            setColour('cyan')
            time.sleep(onTime)
            setColour('blue')
            time.sleep(onTime)
            setColour('purple')
            time.sleep(onTime)
    except KeyboardInterrupt:
        lightsOff()
        GPIO.cleanup()
        
    return;

def ravebow(onTime = 1, offTime = 0.2):
    try:
        while True:
            setColour('red')
            time.sleep(onTime)
            lightsOff()
            time.sleep(offTime)
            setColour('yellow')
            time.sleep(onTime)
            lightsOff()
            time.sleep(offTime)
            setColour('green')
            time.sleep(onTime)
            lightsOff()
            time.sleep(offTime)
            setColour('cyan')
            time.sleep(onTime)
            lightsOff()
            time.sleep(offTime)
            setColour('blue')
            time.sleep(onTime)
            lightsOff()
            time.sleep(offTime)
            setColour('purple')
            time.sleep(onTime)
            lightsOff()
            time.sleep(offTime)
    except KeyboardInterrupt:
        lightsOff()
        GPIO.cleanup()
        
    return;

def translateMorse(code, dotLength = 0.2, colour = 'white'):
    
    for char in code:
        if char == '.':
            setColour(colour)
            time.sleep(dotLength)
            lightsOff()
            time.sleep(dotLength)
        elif char == '-':
            setColour(colour)
            time.sleep(dotLength * 3)
            lightsOff()
            time.sleep(dotLength)
        else:
            print('error unacceptable character in morse code: ' + char)
            lightsOff()
            GPIO.cleanup()
            break
    
    time.sleep(dotLength * 2)
    
    return;

def newWord(dotLength = 0.2, colour = 'white'):
    
    lightsOff()
    time.sleep(dotLength * 6)
    
    return;

def morseCode(inText, dotLength = 0.2, colour = 'white'):

    try:
        for char in inText:
            if char == ' ':
                newWord(dotLength = dotLength, colour = colour)
            elif char == 'e':
                translateMorse(code = '.')
            elif char == 't':
                translateMorse(code = '-')
            elif char == 'a':
                translateMorse(code = '.-')
            elif char == 'o':
                translateMorse(code = '---')
            elif char == 'i':
                translateMorse(code = '..')
            elif char == 'n':
                translateMorse(code = '-.')
            elif char == 's':
                translateMorse(code = '...')
            elif char == 'h':
                translateMorse(code = '....')
            elif char == 'r':
                translateMorse(code = '.-.')
            elif char == 'd':
                translateMorse(code = '-..')
            elif char == 'l':
                translateMorse(code = '.-..')
            elif char == 'c':
                translateMorse(code = '-.-.')
            elif char == 'u':
                translateMorse(code = '..-')
            elif char == 'm':
                translateMorse(code = '--')
            elif char == 'w':
                translateMorse(code = '.--')
            elif char == 'f':
                translateMorse(code = '..-.')
            elif char == 'g':
                translateMorse(code = '--.')
            elif char == 'y':
                translateMorse(code = '-.--')
            elif char == 'p':
                translateMorse(code = '.--.')
            elif char == 'b':
                translateMorse(code = '-...')
            elif char == 'v':
                translateMorse(code = '...-')
            elif char == 'k':
                translateMorse(code = '-.-')
            elif char == 'j':
                translateMorse(code = '.---')
            elif char == 'x':
                translateMorse(code = '-..-')
            elif char == 'q':
                translateMorse(code = '--.-')
            elif char == 'z':
                translateMorse(code = '--..')
            elif char == '1':
                translateMorse(code = '.----')
            elif char == '2':
                translateMorse(code = '..---')
            elif char == '3':
                translateMorse(code = '...--')
            elif char == '4':
                translateMorse(code = '....-')
            elif char == '5':
                translateMorse(code = '.....')
            elif char == '6':
                translateMorse(code = '-....')
            elif char == '7':
                translateMorse(code = '--...')
            elif char == '8':
                translateMorse(code = '---..')
            elif char == '9':
                translateMorse(code = '----.')
            elif char == '0':
                translateMorse(code = '-----')
            else:
                print('error unacceptable character: ' + char)
                lightsOff()
                GPIO.cleanup()
                break
            
    except KeyboardInterrupt:
        lightsOff()
        GPIO.cleanup()
        
    return;

setupPins()

while True:
    
    request = input('set lights:')
    print(request)
    if request == 'off' or request == 'o':
        lightsOff()
    elif request == 'red' or request == 'r':
        setColour(colour = 'red')
    elif request == 'redFront' or request == 'rf':
        setColour(location = 'front', colour = 'red')
    elif request == 'redBack' or request == 'rb':
        setColour(location = 'back', colour = 'red')
    elif request == 'yellow' or request == 'y':
        setColour(colour = 'yellow')
    elif request == 'yellowFront' or request == 'yf':
        setColour(location = 'front', colour = 'yellow')
    elif request == 'yellowBack' or request == 'yb':
        setColour(location = 'back', colour = 'yellow')
    elif request == 'green' or request == 'g':
        setColour(colour = 'green')
    elif request == 'greenFront' or request == 'gf':
        setColour(location = 'front', colour = 'green')
    elif request == 'greenBack' or request == 'gb':
        setColour(location = 'back', colour = 'green')
    elif request == 'cyan' or request == 'c':
        setColour(colour = 'cyan')
    elif request == 'cyanFront' or request == 'cf':
        setColour(location = 'front', colour = 'cyan')
    elif request == 'cyanBack' or request == 'cb':
        setColour(location = 'back', colour = 'cyan')
    elif request == 'blue' or request == 'b':
        setColour(colour = 'blue')
    elif request == 'blueFront' or request == 'bf':
        setColour(location = 'front', colour = 'blue')
    elif request == 'blueBack' or request == 'bb':
        setColour(location = 'back', colour = 'blue')
    elif request == 'purple' or request == 'p':
        setColour(colour = 'purple')
    elif request == 'purpleFront' or request == 'pf':
        setColour(location = 'front', colour = 'purple')
    elif request == 'purpleBack' or request == 'pb':
        setColour(location = 'back', colour = 'purple')
    elif request == 'white' or request == 'w':
        setColour(colour = 'white')
    elif request == 'whiteFront' or request == 'wf':
        setColour(location = 'front', colour = 'white')
    elif request == 'whiteBack' or request == 'wb':
        setColour(location = 'back', colour = 'white')
    elif request == 'fan':
        pinOn(fanPin)
    elif request == 'rainbow':
        rainbow()
    elif request == 'ravebow':
        ravebow()
    elif request[0:9] == 'morsecode':
        morseCode(inText = request[10:])
    elif request == 'exit':
        lightsOff()
        break
    else:
        print('command not acceptable')

GPIO.cleanup()
