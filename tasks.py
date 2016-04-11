import time
from pymouse import PyMouse
from pykeyboard import PyKeyboard
import random
from celery import Celery


app = Celery(broker='amqp://rabbit_user:password@localhost:5672//app_rabbit')


@app.task()
def quiamouse(qtime, username, password, link, gametype):
        name = 'quia'
        m = PyMouse()
        k = PyKeyboard()
        jstartx = 72
        jstarty = 616
        namechecker = 0
        numoftimes = 1
        seccount = 0
        cardcount = 0

        def randomword(length):
            alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                     'u', 'v', 'w', 'x', 'y', 'z', ]
            for w in range(length):
                return ''.join(random.choice(alpha))

        k.press_key(k.control_l_key)
        time.sleep(2)
        k.tap_key('t')
        k.release_key(k.control_l_key)
        time.sleep(2)
        k.tap_key(k.function_keys[6])
        time.sleep(.5)
        k.tap_key(k.backspace_key)
        time.sleep(.5)
        k.type_string(link)
        time.sleep(.5)
        k.tap_key(k.enter_key)
        time.sleep(3)
        if gametype == 'c':
            m.click(246, 464, n=2)
            k.tap_key(k.backspace_key)
            time.sleep(.5)
            k.type_string(username)
            time.sleep(.5)
            m.click(246, 490, n=2)
            time.sleep(.5)
            k.tap_key(k.backspace_key)
            time.sleep(.5)
            k.type_string(password)
            time.sleep(.5)
            m.click(337, 490)
            time.sleep(3)
            m.click(295, 320)

            for b in range(int(qtime)):
                m.click(534, 530, n=2)
                time.sleep(.50)
                if namechecker == 0:
                    k.type_string(name)
                    namechecker = 1
                elif namechecker == 1:
                    k.tap_key(k.backspace_key, n=6)
                    numoftimes += 1
                    k.type_string(name + str(numoftimes))
                time.sleep(.50)
                m.click(196, 764)
                time.sleep(.50)
                for i in range(5):
                    for a in range(5):
                        m.click(jstartx, jstarty)
                        jstarty += 25
                        time.sleep(.50)
                        k.type_string(randomword(10))
                        time.sleep(.50)
                        k.tap_key(k.enter_key)
                        time.sleep(.50)
                        k.tap_key(k.enter_key)
                    jstarty -= 125
                    jstartx += 125
                    m.click(jstartx, 616)
                    time.sleep(.50)
                jstartx = 72
                jstarty = 616
                m.click(570, 837)
        elif gametype == 'j':
            m.click(103, 326)
            time.sleep(.5)
            k.tap_key(k.tab_key, n=14)
            k.tap_key(k.backspace_key)
            time.sleep(.5)
            k.type_string(username)
            time.sleep(.5)
            m.click(246, 490, n=2)
            time.sleep(.5)
            k.tap_key(k.backspace_key)
            time.sleep(.5)
            k.type_string(password)
            time.sleep(.5)
            m.click(296, 490)
            time.sleep(.5)
            for i in range(int(qtime)):
                for e in range(50):
                    m.click(534, 481)
                    time.sleep(1.1904761)


