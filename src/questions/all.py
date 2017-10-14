#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
all.py

Created on 2017-10-13
by Mike Zawitkowski
mike@acornanalytics.io
"""
from __future__ import division, print_function
import logging as log
import subprocess
import os
from datetime import datetime
import sys


def start_and_end_times(func):
    "Decorator that prints start, end, and total elapsed time values."
    def timer_function(*args, **kwargs):
        time1 = datetime.utcnow()
        msg = "Started timer at %s"
        log.info(msg % time1.replace(microsecond=0).isoformat())
        sys.stdout.flush()

        result = func(*args, **kwargs)

        time2 = datetime.utcnow()
        timed = time2 - time1
        msg = "Script completed at %s; Total time: %s"
        log.info(msg % (time2.replace(microsecond=0).isoformat(), timed))
        return result
    return timer_function


@start_and_end_times
def main():
    scripts = os.listdir(os.getcwd())
    for scriptname in scripts:
        if '.py' not in scriptname:
            continue
        if 'wrong' in scriptname:
            continue
        if scriptname == 'all.py':
            continue
        if 'question' not in scriptname:
            continue

        script = './' + scriptname
        log.info('running script %s' % script)
        subprocess.check_call([script])

    log.info('main script completed.')


if __name__ == "__main__":
    log.basicConfig(level=log.INFO,
                    format='%(asctime)s %(message)s',
                    datefmt="%b %d %H:%M:%S %Z")
    main()
