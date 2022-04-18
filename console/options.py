#!/usr/bin/python3

import sys

from getopt import getopt, GetoptError
from collections import defaultdict

# Local
from console.term import options_usage, os_usage, exception_usage
from exceptions import LFIexceptBadOptions, LFIsyntaxError, LFIsyntaxError


# Options

short_args = 'hcv:o:u:w:d:H:A:C:O:'
long_args  = ['help', 'colors','output=', 'url=', 'wordlist=', 'data=', 'header=', 'user-agent=', 'cookie=', 'os=']
print(__name__)

class Parser:

    # Esta clase analiza los parametros argumentos obtenidos

    def __init__(
        self, argv,
        short_args      = short_args,
        long_args       = long_args,
        options_usage   = options_usage,
        os_usage        = os_usage,
        exception_usage = exception_usage
    ):

        self.argv            = argv
        self.short_args      = short_args
        self.long_args       = long_args
        self.options_usage   = options_usage
        self.os_usage        = os_usage
        self.exception_usage = exception_usage

    def ShowUsage(self):
        sys.tracebacklimit=0
        print(self.options_usage)

    def ShowException(self):
        sys.tracebacklimit=0
        print(self.exception_usage)

    def ShowOs(self):
        sys.tracebacklimit=0
        print(self.os_usage)

    def ArgsControl(self):
        try:
            # Opciones
            opts, args = getopt(sys.argv[1:], short_args, long_args)
            params     = defaultdict(list)
            payload    = ''


            # El usuario no digito opciones

            if not args and not params:
                self.ShowException()
                sys.exit(1)


            # Si se digita un argumento (attributo sin parametro) este se toma como url
            # Si hay mas de un argumento lanza error de 'malas opciones'

            url = None
            if len(args) == 1:
                url = args[0]
            elif len(args) > 1:
                raise LFIexceptBadOptions("Too many arguments.")



        except GetoptError as err:
            self.ShowExeption()
            raise LFIsyntaxError('%s\r\n\n' % err) from None

Parser(short_args).ArgsControl()
