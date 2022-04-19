#!/usr/bin/python3

import sys

from getopt import getopt, GetoptError
from collections import defaultdict

# Local
from console.term import options_usage, os_usage, exception_usage
from exceptions import LFIexceptBadOptions, LFIexception


# Options

short_args = 'hcv:o:u:w:d:H:A:C:O:'
long_args  = ['help', 'colors','output=', 'url=', 'wordlist=', 'data=', 'header=', 'user-agent=', 'cookie=', 'os=']

class CliParser:

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
            opts_cli   = defaultdict(list)


            for a, b in opts:
                opts_cli[a].append(b)


            # El usuario no digito opciones

            if not args and not opts_cli:
                self.ShowException()
                sys.exit(1)


            self.HelpPanel(opts_cli)


            # Revisa si las opciones fueron bien ingresadas por el usuario

            self.CheckOptions(opts_cli, args)


        except LFIexception as msgErr:
            self.ShowException()
            raise msgErr

        except ValueError:
            self.ShowException()
            raise LFIexceptBadOptions(
                'Incorrect options, please check help.'
            )

        except GetoptError as err:
            self.ShowException()
            raise LFIexceptBadOptions('%s.\r\n' % err) from None


    # Muestra panel de ayuda

    def HelpPanel(self, opts_cli):
        if '-h' in opts_cli:
            self.ShowUsage()


    def CheckOptions(self, opts_cli, args):

        # Si se digita un argumento (attributo sin parametro) este se toma como url
        # Si hay mas de un argumento lanza error de 'malas opciones'

        url = None

        if len(args) == 1:
            url = args[0]

        elif len(args) > 1:
            sys.tracebacklimit=0
            raise LFIexceptBadOptions("Too many arguments.")


        # Control del target ingresado por el usuario

        cli_url = None

        if "-u" in opts_cli:

            if url is not None or url == opts_cli['-u'][0]:
                raise LFIexceptBadOptions(
                    'Specify the URL either with -u or last argument.'
                )

            cli_url = opts_cli['-u'][0]

        if cli_url:
            url = cli_url


        # Revision de datos repetidos

        opt_repeat = [i for i in opts_cli if not i == '-w' and len(opts_cli[i]) > 1]
        if opt_repeat:
            raise LFIexceptBadOptions(
                'Bad Usage: Only one %s option could be specified at the same time.'
                % ' '.join(opt_repeat)
            )
