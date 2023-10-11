from flask import Flask, jsonify
import os
import base64

app = Flask(__name__)

from data import data

@app.route('/data', methods=['GET'])
def getData():
    return jsonify(data)

CARPETA_IMAGENES = r'C:\Users\lets\OneDrive - Facultad de Ingeniería de la Universidad de San Carlos de Guatemala\Documentos\GitHub\MIA_201807389\HT4_201807389\CARPETA_IMAGENES'

def obtener_imagenes_info():
    imagenes_info = []
    
    for nombre_archivo in os.listdir(CARPETA_IMAGENES):
        if nombre_archivo.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
            ruta_completa = os.path.join(CARPETA_IMAGENES, nombre_archivo)
            with open(ruta_completa, 'rb') as imagen_archivo:
                imagen_base64 = base64.b64encode(imagen_archivo.read()).decode('utf-8')
                tamaño_imagen = os.path.getsize(ruta_completa)
                imagenes_info.append({'Nombre de la imagen': nombre_archivo, 'base64': imagen_base64, 'Tamanio bytes': tamaño_imagen })
    
    return imagenes_info

@app.route('/getPics', methods=['GET'])
def obtener_imagenes():
    imagenes = obtener_imagenes_info()
    return jsonify(imagenes)

if __name__ == '__main__':
    app.run(debug=True, port=4000)