#🐍 Grimorio de Programación Orientada a Objetos en Python — Edición Anime

#🌟 Nivel 1: Invoca tu Clase
class Guerrero:
    pass  # Técnica aún no revelada

    class Nombre:
        #→ define una clase, el molde
        #pass → técnica aún no disponible, pero la clase ya existe

#🧬 Nivel 2: Constructor y Atributos de Instancia
        class Guerrero:
          def __init__(self, nombre, poder):
              self.nombre = nombre            # Atributo de instancia (parametrizado)
              self.poder = poder              # Atributo de instancia (parametrizado)
              self.nivel = 100                # Atributo de instancia interno / no parametrizado

# ⚔️ Atributo de clase vs Atributo de instancia (modo tabla épica)
# 🔮 Elemento	                     🧬 Atributo de instancia	                                  🧙‍♀️ Atributo de clase
# 📍 ¿Dónde se define?	                Dentro de __init__() con self.	                              Fuera de métodos, directo en la clase
# 👥 ¿A quién pertenece?	            Al objeto individual	                                      A la clase (compartido por todas las instancias)
# 📦 ¿Cómo se accede?	                self.atributo	                                              Clase.atributo o self.atributo
# 🧪 ¿Se hereda?	                    Sí	                                                          Sí
# 🔄 ¿Se puede modificar?	            Cada objeto puede tener su propio valor	                      Si se modifica en una instancia, se oculta la versión de clase
# 💡 ¿Cuándo usarlo?	                Cuando cada objeto tiene propiedades distintas	              Cuando el valor es fijo y común para todos
# 📊 Ejemplo	                        self.nombre = nombre	                                      letters = "TRWAGMYFPDXBNJZSQVHLCKE"              

# # 🧾 Tipos de atributos de instancia
# Tipo de atributo	¿Dónde se define?	Ejemplo
# Parametrizado	Recibido como argumento	self.nombre = nombre
# Interno / No parametrizado	Definido directamente	self.nivel = 100
# De clase (compartido por todos)	Fuera de __init__	nivel_maximo = 999
# 📌 Los atributos definidos en __init__() con self. pertenecen a cada objeto individual.

# ⚔️ Nivel 3: Métodos del Personaje (Técnicas activables)
def atacar(self):
    print(f"{self.nombre} lanza un ataque de {self.poder} puntos!")
# Los métodos son las técnicas que el personaje puede usar
# El primer parámetro es siempre self, para acceder al estado del objeto


# 🔮 Nivel 4: Herencia (Legado ancestral)
class Mago(Guerrero):
    def __init__(self, nombre, poder, elemento):
        super().__init__(nombre, poder)
        self.elemento = elemento  # Nuevo atributo para Mago
# class SubClase(SuperClase):
# super() invoca el constructor de la clase padre
# Puedes añadir atributos únicos o modificar técnicas        

# 🌀 Nivel 5: Polimorfismo (Técnicas con el mismo nombre)
class Sanador(Guerrero):
    def atacar(self):
        print(f"{self.nombre} lanza una curación de {self.poder} puntos.")
# Puedes redefinir métodos con el mismo nombre en distintas clases
# Python decide qué método ejecutar según el tipo de objeto

# 🛡️ Nivel 6: Encapsulamiento (Protección de datos secretos)
self._energia = 100       # Atributo protegido
self.__secreto = "Runas"  # Atributo muy privado
# Convención	¿Para qué sirve?	Ejemplo
# _atributo	Señal de uso interno / protegido	self._energia
# __atributo	Oculta más profundamente	self.__runas_secretas
# ⚠️ No es seguridad real, pero sí una convención importante en equipos y proyectos.


# 🧠 Tabla de referencia rápida
# Concepto	         Descripción breve
# -------------------------------------------------------------------------------------------------
# Clase              Molde para crear objetos
# Objeto	           Instancia de una clase
# Atributo	         Propiedad de cada objeto (self.nombre)
# Método	           Acción que puede ejecutar (def atacar)
# Constructor  	     __init__, inicializa atributos
# Herencia	         Hereda atributos y métodos de otra clase
# Polimorfismo	     Métodos con comportamiento distinto según la clase
# Encapsulamiento	   Protege detalles internos con convenciones


# 🔠 Convenciones de nomenclatura en Python (modo anime)
# ------------------------------------------------------------------------------------------------------------
# Elemento	            Convención	                                 Ejemplo

# Clase                	CamelCase	class                              GuerreroMagico

# Variable              snake_case	                                 guerrero_magico = GuerreroMagico()
# / instancia

# Método                snake_case	                                 def lanzar_hechizo()
# / función	

# Constante	            MAYÚSCULAS_CON_GUIONES	                     PODER_MAXIMO = 9999

# Módulo                minúsculas_con_guiones	                     guerrero_magico.py
# / archivo	


# 💥 Error	                                   ⚔️ Solución práctica
#--------------------------------------------------------------------------------------------------------
# Olvidar self en métodos	                     Siempre usa self para acceder a los atributos

# No usar super() correctamente	               Puedes perder atributos del padre. ¡Invócalo bien!

# Usar = en vez de ==	                         = asigna, == compara. ¡No lo confundas en if!

# Definir atributos sin self.	                 No se guardan en el objeto. Siempre usa self.

# Nombres vagos o sin contexto	               Usa nombres descriptivos: atacar(), curar(), etc.

# No documentar con """Docstring"""	           Tu código necesita guía como una historia de anime 🗺️





