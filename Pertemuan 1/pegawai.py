from manusia import Manusia



class Pegawai(Manusia): #Membuat class child turunan manusia 
    def __init__(self, name,gender,year,nip):
        self.nip = nip
        Manusia.__init__(self, name,gender,year,nip)


    def getNip(self):
        return self.nip
            
