from collections import UserDict
from collections import defaultdict


# Configuracion para el LFI

class LFIsession(UserDict):

    def __init__(self, **kwargs):
        self.data = self.Defaults()


    # Datos por defecto

    def Defaults(self):
        return dict(
            url         = '',
            verbose     = False,
            verbose_lvl = 0,
            colors      = False,
            output      = None,
            payload     = None,
            wordlist    = False
            data        = [],
            header      = [],
            agent       = [],
            cookie      = [],
            OS          = False,
        )


    # Reemplazar las variable con las opciones ingresadas

    def UpdateDict(self, options):
        self.data.update(options)


    # Validacion y control de errores

    def Errors(self):
        if self.data['verbose'] and self.data['verbose_lvl'] > 3:
            raise LFIexceptBadOptions(
                'Bad usage: Verbose level permitted (-v, -vv, -vvv)'
            )

        if not self.data['url']:
            raise LFIexceptBadOptions(
                'Bad usage: You must specify a url'
            )

