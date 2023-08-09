class Estudiante:
   def __init__(self):
      self.tipo = "~" * 1
      self.id = -1 # numero 4 bytes total = 19 bytes
      self.cui = -1
      self.nombre = "~" * 15 # 15 caracteres -> 15 bytes
      self.carnet = -1

   def set_tipo(self, tipo):
      self.tipo = tipo[:1].ljust(2, ' ')

   def set_id(self, id):
      if id > 0:
         self.id = id

   def set_cui(self, cui):
      if cui > 0:
         self.cui = cui

   def set_nombre(self, nombre):
      self.nombre = nombre[:15].ljust(16, ' ')

   def set_carnet(self, carnet):
      if carnet > 0:
         self.carnet = carnet

   def imprimir_info(self):
      print("Tipo: ", self.tipo)
      print("Id Estudiante: ", self.id)
      print("CUI: ", self.cui)
      print("Nombre: ", self.nombre)
      print("Carnet: ", self.carnet)