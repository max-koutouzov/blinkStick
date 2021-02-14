#!/usr/bin/env python3


import socket
from blinkstick import blinkstick


"""
Checking internet connection using Blinkstick.

Usage:
python3 checkConnection.py
"""


class InternetCheck:
    """

    """
    def __new__(cls, host="1.1.1.1", port=853):
        try:
            socket.setdefaulttimeout(1)
            socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, port))
            return True
        except Exception as ex:
            print(ex)

        return False


class BlinkStick:
    def __new__(cls, *args, **kwargs):
        led = blinkstick.find_first()
        if InternetCheck() is True:
            print("Internet is up!")
            led.set_color(name="green")
        elif InternetCheck() is False:
            print("Internet is down")
            led.set_color("red")


if __name__ == '__main__':
    BlinkStick()
