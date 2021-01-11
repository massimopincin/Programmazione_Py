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
        for i in self.corso:
            print("Frequento il corso: ",i)

class Docente(Persona):

    def __init__(self,nome,cognome,corso):
        super().__init__("Docente UNITS",nome,cognome)
        self.corso=corso
    def bonjour(self):
        Persona.bonjour(self)
        for i in self.corso:
            print("Insegno il corso: ",i) 

obj_ProfRusso = Docente("Stefano Alberto", "Russo", ["Programmazione", "Laboratorio di Programmazione"])

obj_ProfManzoni= Docente("Luca","Manzoni",["Geometria","Analisi"])

obj_ProfDelSanto = Docente("Daniele","Del Santo",["Analisi"])

obj_Giulio=Studente("Giulio","Caravagna",["Programmazione","Laboratorio di Programmazione","Geometria","Analisi"])



def docente_copre_studente(docente,studente):
    print("Docente che esamino\n-~-~-o-~-~-o-~-~-")
    docente.bonjour()
    print("\nStudente che esamino\n-~-~-o-~-~-o-~-~-")
    studente.bonjour()
    print("\nRicerca in corso...\n-~-~-o-~-~-o-~-~-")
    s=0
    manca=[]
    for i in studente.corso:
        print("Corso",i,"->",i in docente.corso)
        if(i not in docente.corso):
            s=s+1
            manca.append(i)
    print("\nRicerca completata\n-~-~-o-~-~-o-~-~-")
    if(s==0):
        print("Tutti i corsi sono coperti.\n")
    else:
        print(len(manca), "corsi non sono coperti!\n")
    return manca
        
def copertura_totale(docenti,studente):
    m=studente.corso
    for i in docenti:
        print("\n\n\n\nRICERCA n.",(docenti.index(i)+1),"\n")
        l=docente_copre_studente(i,studente)
        n=[]
        for j in m:
            if j in l:
                n.append(j)
        m=n
        if m==[]:
            print("Tutti i corsi sono coperti!")
            break
        if m!=[]:
            print("Continuo il ciclo con",m)
            studente.corso=m

copertura_totale([obj_ProfRusso,obj_ProfDelSanto,obj_ProfManzoni],obj_Giulio)