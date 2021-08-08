

class PortafolioModel(object):

    @classmethod
    def fromJson(cls, obj):
        p = PortafolioModel()
        p.pais = obj['pais']
        p.activos = [ PosicionModel.fromJson(a) for a in obj['activos'] ] 
        return p
    
    def __str__(self):
        activos_str = ""
        for a in self.activos:
            activos_str += f"\n - {a}"
        return f"Portafolio: {self.pais}:\nactivos: {activos_str}"
    

class TituloModel(object):

    @classmethod
    def fromJson(cls, obj):
        t = TituloModel()
        t.simbolo = obj['simbolo']
        t.descripcion = obj['descripcion']
        t.pais = obj['pais']
        t.mercado = obj['mercado']
        t.tipo = obj['tipo']
        t.plazo = obj['plazo'] 
        t.moneda = obj['moneda']
        return t
    
    def __str__(self):
        return f"Titulo: simbolo: {self.simbolo} | descripcion: {self.descripcion}"


class ParkinModel(object):

    @classmethod
    def fromJson(cls, obj):
        p = ParkinModel()
        p.disponibleInmediato = obj['disponibleInmediato']
        return p

    
    def __str__(self):
        return f"{self.disponibleInmediato}"
        

class PosicionModel(object):

    @classmethod
    def fromJson(cls, obj):
        p = PosicionModel()

        p.cantidad = obj['cantidad']
        p.comprometido = obj['comprometido']
        p.variacionDiaria = obj['variacionDiaria']
        p.puntosVariacion = obj['puntosVariacion']
        p.ultimoPrecio = obj['ultimoPrecio']
        p.ppc = obj['ppc']
        p.gananciaPorcentaje = obj['gananciaPorcentaje']
        p.gananciaDinero = obj['gananciaDinero']
        p.valorizado = obj['valorizado']  
        p.titulo = TituloModel.fromJson(obj['titulo'])
        if obj['parking']:
            p.parking = ParkinModel.fromJson(obj['parking'])
        else:
            p.parking = "SIN PARKING"
        return p
    
    def __str__(self):
        return f"Posicion: \n\tcantidad: {self.cantidad}\
            \n\tcomprometido: {self.comprometido}\
            \n\tpuntos Variacion: {self.puntosVariacion}\
            \n\tvariacionDiaria: {self.variacionDiaria}\
            \n\tultimo precion: {self.ultimoPrecio}\
            \n\tppc: {self.ppc}\
            \n\tganacia porcentaje: {self.gananciaPorcentaje}\
            \n\tgananciaDinero: {self.gananciaDinero}\
            \n\tvalorizado: {self.valorizado}\
            \n\t{self.titulo}\
            \n\tparkin: {self.parking}"
        
    
