#!/usr/bin/python3

import sys
from console.parser import CliParser

# Funcion principal del programa

def main():

    CliParser(sys.argv).ArgsControl()

main()
