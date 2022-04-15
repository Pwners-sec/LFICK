#!/usr/bin/python3

import sys
from argparse import ArgumentParser
from argparse import ArgumentError
from console.term import header_usage

def ArgsControl(argv=None):

    # Esta funcion analiza los parametros argumentos obtenidos

    if not argv:
        argv = sys.argv

    parser = ArgumentParser(usage=header_usage)
    try:
        # Options
        parser.add_argument('-h', '--help',        dest='opt_help')
        parser.add_argument('-v',                  dest='opt_verbose')
        parser.add_argument('-o', '--output',      dest='opt_output')
        parser.add_argument('-c', '--colors',      dest='opt_colors')

        # Target
        parser.add_argument('-u', '--url',         dest='target')

        # Request
        parser.add_argument('-d', '--data',        dest='request_data')
        parser.add_argument('-H', '--header',      dest='request_header')
        parser.add_argument('-A', '--user-agent',  dest='request_agent')
        parser.add_argument('-C', '--cookie',      dest='request_cookie')

        # Operating system
        parser.add_argument('-O', '--os',          dest='os')

        # ! Aqui faltaria codigo para controlar el flujo del parser
        # comparando los argumentos del parser con la entrada del sys.argv
        # esto es para solucionar todos los errores de tipeo, por parte del usuario

    except (argparse.ArgumentError, TypeError) as ex:
        parser.error(ex)

    return argv

