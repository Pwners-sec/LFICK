#!/usr/bin/python3

# Programa para definir el Panel de ayuda y el manejo de la salida

header_usage = """\nUsage:\tlfick [options] -u <url>"""

exception_usage = """%s\n\nType lfick -h for more information""" % header_usage

os_usage = """
(!) Operating system recognition has failed. Please specify this

 Usage: [command] -O windows
                     linux
                     mac
"""

options_usage = """%s\n
Options:
    -h, --help                  Shows this help
    -v                          Verbosity level (use -vv or more for increment the verbose)
    -o, --output <file>         Send the output to file
    -c, --colors                Output with colors

    Target:
        -u <url>                Target URL (Example: -u http://127.0.0.1/home/dashboard?id=1)

    Request:
        -d, --data <data>       HTTP POST data (Example: "id=1")
        -H, --header <header>   Extra header (e.g. "X-Forwarded-For: 127.0.0.1")
        -A, --user-agent <name> HTTP User-Agent header value
        -C, --cookie <cookie>   HTTP Cookie header value (Example: "PHPSESSID=6e573a0..")

    Operating System:
        -O win, windows         Specify the operating system to penetrate,
           lin, linux           by default the program recognizes the OS,
           mac                  if it does not, this field will be required.
""" % header_usage

print('%s\n' % os_usage)
