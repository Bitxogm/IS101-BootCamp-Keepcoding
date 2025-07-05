"""
Estructura

Nº de DNI
Nombre
Apellidos
Domicilio
Fecha de nacimiento
"""

"""
Fecha

Dia
Mes
Año
"""

class Day:

    def __init__(self, day: int, month: int, year: int):
        self.day = day
        self.month = month
        self.year = year
        self.validate_day()
        # self.leap_year()
        self.show()

    def validate_day(self):
        if self.day > 31 or self.day < 1:
            raise ValueError(f"dia {self.day} inválido")
        if self.month > 12 or self.month < 1:
            raise ValueError(f"mes {self.month} inválido")
        if self.year < 1:
            raise ValueError(f"Año {self.year} debe ser mayor de 0")
        self.validate_february()

    def validate_february(self):
        if self.month == 2 and self.day  > 28  and not self.leap_year():
            raise ValueError(f'Fecha invalida  este año  {self.year}  no es bisiesto , el mes {self.month} tiene  28 dias')
        elif self.month == 2 and self.day >29 and self.leap_year():
            raise ValueError(f'Numero  de dias de mes {self.month}  en {self.year} año bisiesto es 29')
        
    def leap_year(self):
        return self.year % 400 == 0 and self.year %100 != 0 or self.year % 4 == 0 

    def show(self):
        return f"{self.day:02d}/{self.month:02d}/{self.year:04d}"
    
my_day = Day(31,  12, 1999)
print(my_day.show())

no_leap_year = Day(31 , 2, 1999)
# no_leap_year1 = Day(31 , 2, 2000)
print(no_leap_year.show())
# print(no_leap_year1.show())

    
        










        

        