# Lista de exceptiones para el manejo de errores

class LFIexception(Exception):
    pass

class LFIsyntaxError(LFIexception):
    pass

class LFIexceptBadOptions(LFIexception):
    pass
