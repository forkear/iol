
class Saldo(object):

    def __init__(self, obj):

        self.comprometido = obj['comprometido']
        self.disponible = obj['disponible']
        self.disponibleOperar = obj['disponibleOperar']
        self.liquidacion  = obj['liquidacion']
        self.saldo = obj['saldo']

class Cuenta(object):

    def __init__(self, obj):
        self.saldos = []
        self.comprometido = obj['comprometido']
        self.disponible = obj['disponible']
        self.estado = obj['estado']
        self.margenDescubierto = obj['margenDescubierto']
        self.moneda = obj['moneda']
        self.saldo = obj['saldo']
        self.tipo = obj['tipo']
        self.titulosValorizados = obj['titulosValorizados']
        self.total = obj['total']

        for s in obj['saldos']:
            self.saldos.append(Saldo(s))
        

       