"""
Autorid: Kaur Kenk, Nansen Palo

Teema: Koolimatemaatika mäng

Vajalik programmi tööks: matplotlib, pythoni versioon vähemalt 3.10

Käivitamise juhend: installida kas läbi pipi või thonny matplotlib
ja tkinter, seejärel kas terminalis või läbi koodiredaktori
käivitada __main__.py.

Inspiratsioon: Programm on kergelt inspireeritud pranglimisest.
latexi displaymisega aitas: 
https://www.tutorialspoint.com/how-to-display-latex-
in-real-time-in-a-text-box-in-tkinter
Samuti on kasutatud matplotlibi dokumentatsiooni,
tkdocs.com veebilehte.

"""
import tkinter as tk
from tkinter import ttk

from random import randint

import matplotlib
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

import funktsioonid as fun


def main():


    #Programm kasutab võrrandite printimiseks TkAgg backendi
    matplotlib.use('TkAgg')
    prog = Programm()
    prog.mainloop()


class Programm(tk.Tk):


    def __init__(self):

        """Tekitab uue tkinteri akna, sätib paika õige akna suuruse
        ning sätib kysimuse_counter ja oiged muutujad paika.
        """
        #Teeb läbi tk.Tk init funktsiooni
        super().__init__()
        self.kysimuse_counter = 1
        self.oiged = 0

        self.title('Matemaatika mäng')
        #Võtab ekraani suuruse arvesse, et mängu aken oleks sama suur
        #nii madala kui kõrge resolutsiooniga monitoridel.
        self.ekraani_laius = self.winfo_screenwidth()
        self.ekraani_korgus = self.winfo_screenheight()
        self.geometry(f'{round(self.ekraani_laius/3.2)}x'
                      + f'{round(self.ekraani_korgus/2.6)}')
        #Raamid suurendavad end automaatselt akent suurendades
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.tiitel()
        
    def tiitel(self):

        """Teeb tiitli raami ja selle sees olevad aknad."""
        self.tiitel_raam = ttk.Frame(self)
        #Raamis on 2 rida ja 3 veergu.
        self.tiitel_raam.rowconfigure(0, weight=2)
        self.tiitel_raam.rowconfigure(1, weight=1)
        self.tiitel_raam.columnconfigure(1, weight=1)
        self.tiitel_raam.columnconfigure(2, weight=1)
        self.tiitel_raam.columnconfigure(3, weight=1)
        self.tiitel_raam.grid(column = 0, row = 0,
                              sticky = 'nsew')

        self.tiitel_nimi = ttk.Label(self.tiitel_raam,
                                     anchor='center',
                                     font=('Arial', 40),
                                     text = 'Matemaatika mäng')
        self.tiitel_nimi.grid(column = 1, row = 0, columnspan=3,
                              sticky = 'nsew')

        #Sätib tiitellehe nuppude fondi ja suuruse.
        self.tiitelnupp_stiil = ttk.Style()
        self.tiitelnupp_stiil.configure('Tiitel.TButton',font=('Arial',25))
        self.start_nupp = ttk.Button(self.tiitel_raam, text='Mängima!',
                                     style='Tiitel.TButton',
                                     command=self.mang)
        self.start_nupp.grid(column = 1, row = 1, sticky = 'n')

        self.juhised_nupp = ttk.Button(self.tiitel_raam,
                                       text = 'Juhised',
                                       style='Tiitel.TButton',
                                       command=self.juhised)
        self.juhised_nupp.grid(column = 2, row = 1, sticky = 'n')
        
        self.kinni_nupp = ttk.Button(self.tiitel_raam,
                                     text='Sulge',
                                     style='Tiitel.TButton',
                                     command=self.destroy)
        self.kinni_nupp.grid(column=3, row=1, sticky = 'n')

    def juhised(self):

        """Teeb uue toplevel akna, kus on juhised.txt failist võetud
        sisestuse juhised.
        """
        
        self.juhised = tk.Toplevel(self)
        #akna suurendamisel suureneb juhiste_raam
        self.juhised.rowconfigure(0, weight = 1)
        self.juhised.columnconfigure(0, weight = 1)
        self.juhised.title('Sisestuse juhised')
        #vt. init
        self.juhised.geometry(f'{round(self.ekraani_laius/2)}x'
                              + f'{round(self.ekraani_korgus/2)}')

        self.juhiste_raam = ttk.Frame(self.juhised)
        self.juhiste_raam.grid(column = 0, row = 0,
                               sticky = 'nsew')
        #Teksti rida on 3 korda suurem kui tagasinupu rida                       
        self.juhiste_raam.rowconfigure(0, weight = 3)
        self.juhiste_raam.rowconfigure(1, weight = 1)

        self.juhiste_raam.columnconfigure(0, weight=1)

        self.juhised_tiitel = ttk.Label(self.juhiste_raam,
                                        text = 'Sisestuse juhised',
                                        width = 50, font = 44)
        self.juhised_tiitel.grid(column = 0, row = 0)

        #Juhiste tekst tuleb failist juhised.txt, kuna siia kirjutamine
        #võtab liiga palju ruumi
        self.juhisetekstifail = open('juhised.txt', encoding='utf-8')
        self.juhised_text = ttk.Label(self.juhiste_raam, justify='center',
                                      text = self.juhisetekstifail.read(),
                                      font=('Arial', 16))
        self.juhised_text.grid(column = 0, row = 0, sticky= 'ns')
        self.juhisetekstifail.close()

        self.juhiste_nupp_stiil = ttk.Style()
        self.juhiste_nupp_stiil.configure('Juhised.TButton',
                                          font=('Arial', 20)) 
        self.juhised_kinni_nupp = ttk.Button(self.juhiste_raam, text = 'Sulge',
                                             style='Juhised.TButton',
                                             command = self.juhised.destroy)
        self.juhised_kinni_nupp.grid(column = 0, row = 1)
        
    def mang(self):

        """Teeb raami, kus sees küsitlus toimub
        ja selle raami sees olevad aknad."""
        self.tiitel_raam.destroy()

        self.mangu_raam = ttk.Frame(self)
        self.mangu_raam.grid(column = 0, row = 0,
                             sticky = 'nsew')
        #mängul on 1 veerg ja 5 rida, võrrandi rida on teistest
        #2 korda suurem.
        self.mangu_raam.columnconfigure(0, weight=1)
        self.mangu_raam.rowconfigure(0, weight = 2)
        self.mangu_raam.rowconfigure(1, weight = 1)
        self.mangu_raam.rowconfigure(2, weight = 1)
        self.mangu_raam.rowconfigure(3, weight = 1)
        self.mangu_raam.rowconfigure(4, weight = 1)

        #Genereeritakse lahendatav võrrand ja sellele vastav lahendus.
        self.uus_funktsioon()

        self.funktsioon = ttk.Label(self.mangu_raam)
        self.funktsioon.grid(column = 0, row = 0, sticky= 'ns')

        #Tehakse uus matplotlibi figuur ja pannakse see self.funktsioon
        #labeli sisse.
        self.figuur = matplotlib.figure.Figure(figsize = (10, 3), dpi = 100)
        self.latex = FigureCanvasTkAgg(self.figuur, master = self.funktsioon)
        self.latex.get_tk_widget().grid(column = 0, row = 0, sticky='ns')
    
        #Võrrand prinditakse matplotlibi figuuri sisse
        self.figuur.text(0.5, 0.5, self.vorrand,
                         horizontalalignment = 'center',
                         verticalalignment = 'center', fontsize = 40)
        self.latex.draw()
        
        #Vastuse kasti tegemine
        self.sisestus = tk.StringVar()
        self.vastuse_kast = ttk.Entry(self.mangu_raam,
                                      font = ('Arial', 20),
                                      textvariable = self.sisestus)
        self.vastuse_kast.grid(column = 0, row = 1, sticky = 'ns')

        #Kontrollimise nupp
        self.vastamis_nupp = ttk.Button(self.mangu_raam, text = 'Kontrolli',
                                        command = self.kontrolli)
        self.vastamis_nupp.grid(column = 0, row = 2)
        
        #Näitab, mitmenda küsimuse peal kasutaja on
        self.loendur = ttk.Label(self.mangu_raam,
                                 text = f'{self.kysimuse_counter}/20')
        self.loendur.grid(column = 0, row = 3)

        #Näitab, kui kasutaja on sisestanud midagi valesti, näitab
        #ka, kas vastus oli õige/vale
        self.sisestuse_info = ttk.Label(self.mangu_raam)
        self.sisestuse_info.grid(column = 0, row = 4)

        #Enter nupp binditud kontrollimiseks, et ei
        #peaks iga kord kontrollimise nuppu vajutama
        self.bind('<Return>', self.kontrolli)

    def uus_funktsioon(self):
        """valib suvaliselt ühte tüüpi võrrandi ja
           salvestab võrrandi latexi sõne ja vastused
           mängu jaoks muutujatesse"""
        #TODO: rohkem võrrandeid mängu
        self.vorrandi_number = randint(1,4)
        #self.vorrandi_number = 2
        match self.vorrandi_number:
            case 1:
                self.vorrand, self.lahendus = fun.lineaar()
            case 2:
                self.vorrand, self.lahendus1, self.lahendus2 = fun.ruut()
            case 3:
                self.vorrand, self.lahendus = fun.eksponentsiaal()
            case 4:
                self.vorrand, self.lahendus = fun.logaritm()
    
    def kontrolli(self, event=None):
        """Kontrollib vastust, mis kasutaja sisestas ja 
           uuendab mängu raamil väärtusi. Kui on vastatud
           piisavatele küsimustele, lõpetab mängu"""

        self.vastus = self.sisestus.get()
        #vaatab, kas võrrand on ruutfunktsioon,
        #sest sellel on kaks vastust
        if self.vorrandi_number == 2:
            #teeb vastused listiks, vaatab, kas vastused on sees
            #või mitte ja siis kustutab listist.
            vastused = self.vastus.split(', ')
            if (str(self.lahendus1) in self.vastus and
                str(self.lahendus2) in vastused):
                vastused.pop(vastused.index(str(self.lahendus1)))
                vastused.pop(vastused.index(str(self.lahendus2)))
                #kui oli täpselt kaks vastust ja need olid õiged,
                #tuleb õige vastus
                if vastused == []:
                    self.oiged += 1
                    self.sisestuse_info.configure(text='Õige vastus!')
                else:
                    self.sisestuse_info.configure(text='Vale vastus!')
            else:
                self.sisestuse_info.configure(text='Vale vastus!')
        else:
            #kui kasutaja sisestas midagi muud peale täisarvu,
            #ütleb programmis sellest kasutajale
            try:
                self.vastuse_number = int(self.vastus)
            except ValueError:
                self.sisestuse_info.configure(text='Sisesta vastus täisarvuna')
                return None
            if int(self.vastus) == self.lahendus:
                self.oiged += 1
                self.sisestuse_info.configure(text='Õige vastus!')
            else:
                self.sisestuse_info.configure(text='Vale vastus!')

        #genereerib uuesti suvalise võrrandi ja sellele
        #vastava lahenduse
        self.uus_funktsioon()
        
        self.kysimuse_counter += 1
        #Lõpetab mängu, kui 20 küsimust on vastatud
        if self.kysimuse_counter == 20:
            self.lopp()
        else:
            #Puhastab figuuri ja kirjutab uue võrrandi figuurile
            self.figuur.clear()
            self.figuur.text(0.5, 0.5, self.vorrand,
                             horizontalalignment = 'center',
                             verticalalignment = 'center',
                             fontsize = 30)
            self.latex.draw()
            #uuendab loendurit
            self.loendur.configure(text = f'{self.kysimuse_counter}/20')
            #kustutab kasutaja eelmise sisestuse
            self.vastuse_kast.delete(0, 'end')

    def lopp(self):

        """Teeb lõpuekraani raami ja näitab tulemust.
        Saab minna tiitellehele"""
        #TODO: teha lõpuekraan valmis
        #Teeb nii, et Enterit vajutades enam ei kutsutaks kontrolli()
        #funktsiooni
        self.unbind('<Return>')
        #Hävitab mängu raami ja loob lõpuekraani raami, kus on kasutaja
        #tulemus 20-st ja kaks nuppu
        self.mangu_raam.destroy()
        self.lopp_raam = ttk.Frame(self)
        self.lopp_raam.grid(column = 0, row = 0, sticky = 'nsew')
        self.lopp_raam.columnconfigure(0, weight = 1)
        self.lopp_raam.columnconfigure(1, weight = 1)
        self.lopp_raam.rowconfigure(0, weight = 3)
        self.lopp_raam.rowconfigure(1, weight = 1)
        self.tulemus = ttk.Label(self.lopp_raam,
                                 text = f'Sinu tulemus on {self.oiged}/20.',
                                 font = ('Arial', 30))
        self.tulemus.grid(column = 0, row = 0, columnspan = 2)
        #Nupp, millega saab minna tiitellehele ja mängu uuesti alustada
        self.uuesti_nupp = ttk.Button(self.lopp_raam,
                                      text = 'Tagasi tiitelehele',
                                      command = self.uuesti)
        self.uuesti_nupp.grid(column = 0, row = 1)
        
        self.sulgemis_nupp_lopp = ttk.Button(self.lopp_raam,
                                             text = 'Sulge',
                                             command = self.destroy)
        self.sulgemis_nupp_lopp.grid(column = 1, row = 1)

    def uuesti(self):

        """Taastab muutujate kysimuse_counter ja oiged algsed väärtused
        ning läheb tagasi tiitellehele."""
        self.kysimuse_counter = 1
        self.oiged = 0
        #Hävitab lõpuekraani raami ja läheb tagasi tiitellehe raamile
        self.lopp_raam.destroy()
        self.tiitel()
        
if __name__ == '__main__':
    main()
