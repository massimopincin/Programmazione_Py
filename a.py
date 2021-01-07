class Persona:

    def __init__(self,ruolo,nome,cognome):
        self.ruolo=ruolo
        self.nome=nome
        self.cognome=cognome

    def bonjour(self):
        print(self.ruolo,":",self.nome, self.cognome)

class Studente(Persona):

    def __init__(self,nome,cognome,corso):
        super().__init__("Studente UNITS",nome,cognome)
        self.corso=corso
    def bonjour(self):
        Persona.bonjour(self)
        print("Studente del corso: ",self.corso)

class Docente(Persona):

    def __init__(self,nome,cognome,corso):
        super().__init__("Docente UNITS",nome,cognome)
        self.corso=corso
    def bonjour(self):
        Persona.bonjour(self)
        print("Docente del corso: ",self.corso)   

tecnico=TecnicoAmministrativo("Elvis","Pozzecco","Buje")

tecnico.bonjour()