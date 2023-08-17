import ctypes
import struct

from Utilities import coding_str

const = 'q 20s I'

class Disco(ctypes.Structure):

    _fields_ = [
        ('mbr_tamano', ctypes.c_longlong),
        ('mbr_fecha_creacion', ctypes.c_char * 20),
        ('mbr_dsk_signature', ctypes.c_int )
    ]

    def __init__(self):
        self.mbr_t = 0
        self.mbr_f = b'\0'*20
        self.mbr_d = 0

    def set_infomation(self, mbr_t, mbr_f, mbr_d):
        self.mbr_t=mbr_t
        self.mbr_f=mbr_f
        self.mbr_d=mbr_d

    def doSerialize(self):
        return struct.pack(
            const,
            self.mbr_t,
            self.mbr_f,
            self.mbr_d
        )
    
    def display_info(self):
        print(f"Tamaño del disco: {self.mbr_t}")
        print(f"Fecha de creacion: {self.mbr_f}")
        print(f"Asignacion de disco: {self.mbr_d}")
