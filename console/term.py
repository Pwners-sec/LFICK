#!/usr/bin/python3

# Programa para definir el Panel de ayuda y el manejo de la salida
# Uso:
# from console.term import ACSII
# from console.term import header_usage
# Ejemplo:
# print('%s%s%s%s' % (ACSII.bgCyan, ACSII.fgBlack, header_usage, ACSII.reset))

header_usage = """\nUsage:\tlfick [options] -u <url>\r\n"""

# No se si vamos a usar asterisco..
# You can enter a Asterisk (*) where you want to apply the inclusion attack.
# Example: -u http://127.0.0.1/home/contact*


exception_usage = """%s\nType lfick -h for more information\n""" % header_usage

os_usage = """
(!) Operating system recognition has failed. Please specify this

 Usage: [command] -O, --os windows
                           linux
                           mac
"""

options_usage = """%s
Options:
    -h, --help                  Shows this help
    -v, -vv, -vvv               Verbosity level
    -c, --colors                Output with colors
    -o, --output <file>         Send the output to file

    Target:
        -u <url>                Target URL (Example: -u http://127.0.0.1/home/dashboard?id=1)

    Wordlists:
        -w, --wordlist          If you wish to use one of your wordlists

    Request:
        -d, --data <data>       HTTP POST data (Example: "id=1")
        -H, --header <header>   Extra header (e.g. "X-Forwarded-For: 127.0.0.1")
        -A, --user-agent <name> HTTP User-Agent header value
        -C, --cookie <cookie>   HTTP Cookie header value (Example: "PHPSESSID=6e573a0..")

    Operating System:
        -O, --os win, windows   Specify the operating system to penetrate,
                 lin, linux     by default the program recognizes the OS,
                 mac            if it does not, this field will be required.

""" % header_usage


# Declaracion de colores y funciones que los requieran

class ACSII:

    reset = "\x1b[0m"
    bright = "\x1b[1m"
    dim = "\x1b[2m"
    underscore = "\x1b[4m"
    blink = "\x1b[5m"
    reverse = "\x1b[7m"
    hidden = "\x1b[8m"

    delete = "\x1b[0K"
    oneup = "\033[1A"

    fgBlack = "\x1b[30m"
    fgRed = "\x1b[31m"
    fgGreen = "\x1b[32m"
    fgYellow = "\x1b[33m"
    fgBlue = "\x1b[34m"
    fgMagenta = "\x1b[35m"
    fgCyan = "\x1b[36m"
    fgWhite = "\x1b[37m"

    bgBlack = "\x1b[40m"
    bgRed = "\x1b[41m"
    bgGreen = "\x1b[42m"
    bgYellow = "\x1b[43m"
    bgBlue = "\x1b[44m"
    bgMagenta = "\x1b[45m"
    bgCyan = "\x1b[46m"
    bgWhite = "\x1b[47m"

    noColour = ""

