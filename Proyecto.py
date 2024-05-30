import os
os.system ("cls")

class Usuario:
    def __init__(self, nombre, email, pais) -> None:#self, atributos
        self.nombre = nombre
        self.email = email
        self.pais = pais
class Emprendedor (Usuario):
    def __init__(self, nombre, email, pais,rubro, estado_inversion, instancia, valuacion) -> None:
        self.rubro= rubro
        self.estado_inversion=estado_inversion
        self.instancia=instancia
        self.valuacion=valuacion
        super().__init__(nombre, email, pais)
class Inversor (Usuario):
    def __init__(self, nombre, email, pais, tipo_inversor, perfil_inversor, rubros_preferencias) -> None:
        self.tipo_inversor=tipo_inversor
        self.perfil_inversor=perfil_inversor
        self.rubros_preferencias=rubros_preferencias
        super().__init__(nombre, email, pais)

emprendedor_1=Emprendedor("Matias","mati@gmail.com", "Argentina", "Agro", "Estado", "Maduro",2000000)
inversor_1=Inversor("Feli","felirodriguez@gmail.com", "Argentina","Inversor angel", "Conservador","Agro")
print (emprendedor_1)

