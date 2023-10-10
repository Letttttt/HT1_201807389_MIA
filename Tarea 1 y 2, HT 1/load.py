import pickle

def Aescritura_desplazado(archivo,desplazamiento,data):
   archivo.seek(desplazamiento)
   data_serizada = pickle.dumps(data)
   #print(f"Tamaño de la data: {len(data_serizada)}")
   archivo.write(data_serizada)

def Alectura_desplazado(archivo,desplazamiento,data):
   archivo.seek(desplazamiento)
   data_serializada = archivo.read()
   try:
      return pickle.loads(data_serializada)
   except Exception as e:
      return data
   
def Winit_size(file,size_mb):
    #mb to bytes -> mb * 1024kb/1mb * 1024b/1kb -> mb * 1024 * 1024
    buffer = b'\0'*1024
    times_to_write =  size_mb  * 1024 
    print(f"Expected File Size: {len(buffer)*times_to_write} bytes")

    for i in range(times_to_write):
        file.write(buffer)

    print("¡Size apply successfully!")