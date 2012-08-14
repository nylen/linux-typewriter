#!/usr/bin/env python
## A tiny,  nifty script for playing musical notes on each keypress.
##
##  Copyright Sayan "Riju" Chakrabarti (sayanriju) 2009
##  me[at]sayanriju[dot]co[dot]cc ##
##    Released under WTFPL Version 2
## (DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE)
##  Copy of license text can be found online at ##    http://sam.zoy.org/wtfpl/COPYING
## http://rants.sayanriju.co.cc/script-to-make-tick-tick-sound-on-keypress

from Xlib.display import Display
import os
import time


def main():
    disp = Display()  # connect to display
    last_keymap = [0] * 32
    sound_filename = os.path.join(
            os.path.dirname(os.path.realpath(__file__)),
            'sounds/click.wav')

    while 1:  # event loop
        keymap = disp.query_keymap()
        time.sleep(0.02)
        if any(keymap[i] & ~last_keymap[i] for i in xrange(32)):
            os.system('aplay "%s" &' % sound_filename)
        last_keymap = keymap


if __name__ == '__main__':
    main()
