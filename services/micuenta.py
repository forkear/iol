
import requests
import config 

from models.auth import AuthModel
from models.cuenta import Cuenta
from models.portafolio import PortafolioModel

class MiCuentaService():
    
    @classmethod
    def estadocuentas(cls, auth):
        cuentas = []
        url = f"{config.API_URL}/api/v2/estadocuenta"

        r = requests.get(url, headers=auth.get_headers())

        if r.status_code != 200:
            raise Exception(f"No podemos obtener el estado de la cuenta | {r.status_code}")

        data = r.json()
        for cuenta in data['cuentas']:
            cuentas.append( Cuenta(cuenta) )

        
        return cuentas

    @classmethod
    def portafolio(cls, auth, pais):

        if not pais in config.PAISES:
            raise Exception('Pais no valido')
        
        url = f"{config.API_URL}/api/v2/portafolio/{pais}/"

        r = requests.get(url, headers=auth.get_headers())

        if r.status_code != 200:
            raise Exception(f"No podemos obtener el portafolio del pais: {pais}")
        
        data = r.json()
        portafolio = PortafolioModel.fromJson(data)
        
        return portafolio





        



