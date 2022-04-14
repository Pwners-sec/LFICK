#!/usr/bin/python3

import sys
from argparse import ArgumentParser
from argparse import ArgumentError

def ArgsControl(argv=None):

    # Esta funcion analiza los parametros argumentos obtenidos

    if not argv:
        argv = sys.argv

    parser = ArgumentParser(usage='python lfick.py [options] -u TARGET')

    try:
        parser.add_argument('-v', dest='verbose', help='Verbosity level: use -vv or more for greater effect')

        # options = parser.add_argument('-u', '--url', dest='URL', type=str,
                            # help='Target URL (Example: http://127.0.0.1/home/dashboard)')

    except (argparse.ArgumentError, TypeError) as ex:
        parser.error(ex)

    return argv

def HelpPanel():
    parser.print_help()
