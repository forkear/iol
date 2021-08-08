
from .auth import AuthModel
from services.micuenta import MiCuentaService

class Iol(object):

    def __init__(self, username, password):
        self.auth = AuthModel(username, password)

    def estadocuentas(self):
        self.cuentas =  MiCuentaService.estadocuentas(self.auth)
        return self.cuentas

    @property
    def token(self):
        return self.auth.token
        