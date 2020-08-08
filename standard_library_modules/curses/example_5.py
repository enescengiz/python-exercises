#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import curses
import time

ekran = curses.initscr()
curses.start_color()
curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
curses.init_pair(2, curses.COLOR_CYAN, curses.COLOR_BLACK)
curses.init_pair(3, curses.COLOR_RED, curses.COLOR_BLACK)
curses.noecho()
boyutlar = ekran.getmaxyx()
ekran.nodelay(1)
g = 1
q = -1
x, y = 0, 0
while q != ord("q"):
    ekran.clear()
    ekran.addstr(y, x, "hello world!", curses.color_pair(g))
    ekran.move(boyutlar[0] - 1, boyutlar[1] - 1)
    ekran.refresh()
    q = ekran.getch()
    if q in range(49, 52):
        g = int(chr(q))
    if q == ord("w") and y > 0:
        y -= 1
    elif q == ord("s") and y < boyutlar[0] - 1:
        if y == boyutlar[0] - 2 and x == boyutlar[1] - \
                len("hello world!"):
            pass
        else:
            y += 1
    elif q == ord("a") and x > 0:
        x -= 1
    elif q == ord("d") and x < boyutlar[1] - len("hello world!"):
        if y == boyutlar[0] - 1 and x == boyutlar[1] - \
                len("hello world!") - 1:
            pass
        else:
            x += 1
    time.sleep(0.05)
curses.endwin()