class Manusia:

    def __init__(self, name, gender, year,berat = 10, tinggi = 3):
        self.name = name
        self.gender = gender
        self.year = year    
        self.berat = berat
        self.tinggi = tinggi


    def getName(self):
        return self.name