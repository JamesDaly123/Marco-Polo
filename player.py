#PLAYER
from microbit import *
import radio
import music                                 #importing everything we will need.
radio.on()                                   #turning on the radio.

while True:                                  #establishing loop.
    msg = radio.receive_full()               #receiving radio messages and signal strength (Booth, 2018).
    if msg:                                  #checking if a radio message is recived.
        if 'marco' in msg[0]:                #checking if correct message is received.
            signal_s = int(msg[1])           #gives signal strength.
            print(signal_s)
            display.clear()
            sleep(100)

            if signal_s <= -100:             #checking what signal strength is received.
                img = Image('11111:11111:11111:11111:11111')
                display.show(img)            #displaying lights, depending on the signal strength the light will be dimmer of brighter.
                music.play('B9:3')           #playing music, depending on the signal strength the pitch will be higher or lower.
                sleep(10)

            elif signal_s <= -90:
                img2 = Image('33333:33333:33333:33333:33333')
                display.show(img2)
                music.play('B9:3')
                sleep(10)

            elif signal_s <= -80:
                img3 = Image('44444:44444:44444:44444:44444')
                display.show(img3)
                music.play('B8:3')
                sleep(10)

            elif signal_s <= -70:
                img4 = Image('55555:55555:55555:55555:55555')
                display.show(img4)
                music.play('B7:3')
                sleep(10)

            elif signal_s <= -60:
                img5 = Image('66666:66666:66666:66666:66666')
                display.show(img5)
                music.play('B5:3')
                radio.send('winning')              #sending winning message- tells endpoint someboy is in range.
                sleep(10)

            elif signal_s <= -50:
                img6 = Image('77777:77777:77777:77777:77777')
                display.show(img6)
                music.play('B3:3')
                radio.send('winning')              #sending winning message- tells endpoint someboy is in range.
                sleep(10)

            elif signal_s <= -40:
                img7 = Image('99999:99999:99999:99999:99999')
                display.show(img7)
                music.play('B1:3')
                radio.send('winning')              #sending winning message- tells endpoint someboy is in range.
                sleep(10)

        if 'win' in msg[0]:                        #checking if player has won the game
            if signal_s <= -60:                    #checking if player won or lost, <= -60 means they lost.
                display.show(Image.SAD)            #shows a sad face to display that they lost.
                music.play(music.WAWAWAWAA)        #plays sad/ depressing music.
            if signal_s > -60:                     #checking if player won or lost, > -60 means they won.
                display.show(Image.HAPPY)          #shows a happy face to display that they won.
                music.play(music.ENTERTAINER)

        if button_b.is_pressed():                  #checking if reset button is pressed.
            radio.send('reset')                    #telling endpoint microbit that the reset button was pressed.
            display.clear()
            music.stop()