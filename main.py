"""
Autorid: Kaur Kenk, Nansen Palo

Teema: Koolimatemaatika mäng

Vajalik programmi tööks: matplotlib, pythoni versioon vähemalt 3.10

Käivitamise juhend: installida kas läbi pipi või thonny matplotlib
ja tkinter, seejärel kas terminalis või läbi koodiredaktori
käivitada main.py.

Inspiratsioon: Programm on kergelt inspireeritud pranglimisest.
taimeri implementatsiooniga aitas:
https://discuss.python.org/t/using-countdown-and-input-
at-the-same-time/52577/3
latexi displaymisega aitas: 
https://www.tutorialspoint.com/how-to-display-latex-
in-real-time-in-a-text-box-in-tkinter
Samuti on kasutatud matplotlibi dokumentatsiooni,
tkdocs.com veebilehte.

"""
import tkinter as tk
from tkinter import ttk

from random import randint

import csv
import os.path
import os
import math
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

        self.taustavarv = '#fafafa'
        self.taustavarv2 = '#ffffff'
        self.border_varv = '#e0e0e0'
        self.tekst1 = '#1a1a1a'
        self.tekst2 = '#666666'
        self.tume = '#2a2a2a'
        self.oige = '#f5f5f5'

        self.configure(bg=self.taustavarv)

        self.title('Matemaatika treener')
        #Võtab ekraani suuruse arvesse, et mängu aken oleks sama suur
        #nii madala kui kõrge resolutsiooniga monitoridel.
        self.ekraani_laius = self.winfo_screenwidth()
        self.ekraani_korgus = self.winfo_screenheight()
        self.geometry(f'{round(self.ekraani_laius/3.2)}x'
                      + f'{round(self.ekraani_korgus/2.6)}')
        #Raamid suurendavad end automaatselt akent suurendades
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.stiil()
        self.tiitel()

    def stiil(self):
        self.stiil = ttk.Style()
        self.stiil.theme_use('clam')

        self.stiil.configure('Main.TFrame', bg=self.taustavarv)

        self.stiil.configure('Tiitel.TLabel',
                             #background=self.taustavarv,
                             foreground=self.tekst1,
                             font=('Verdana', 42))
        
        self.stiil.configure('Lugeja.TLabel',
                             #background=self.taustavarv,
                             foreground=self.tekst2,
                             font=('Verdana', 13))
        
        self.stiil.configure('Tulemus.TLabel',
                             #background=self.taustavarv,
                             foreground=self.tekst2,
                             font=('Verdana', 14))
        
        self.stiil.configure('Nupp1.TButton',
                       background=self.tume,
                       foreground='white',
                       font=('Verdana', 14),
                       borderwidth=0,
                       focuscolor='none',
                       padding=(20, 12))
        self.stiil.configure('Raadio.TRadiobutton',
                             font=('Verdana', 16))
        
        self.stiil.map('Nupp1.TButton',
                 background=[('active', '#3a3a3a'),
                            ('pressed', '#1a1a1a')])
        
        self.stiil.configure('Nupp2.TButton',
                       background=self.taustavarv,
                       foreground=self.tekst1,
                       font=('Verdana', 14),
                       borderwidth=1,
                       focuscolor='none',
                       padding=(20, 12))
        
        self.stiil.map('Nupp2.TButton',
                 background=[('active', '#f5f5f5')],
                 bordercolor=[('active', '#d0d0d0')])

        

    def tiitel(self):

        """Teeb tiitli raami ja selle sees olevad aknad."""
        self.tiitel_raam = ttk.Frame(self, style='Main.TFrame')
        #Raamis on 1 rida ja 4 veergu.
        self.tiitel_raam.rowconfigure(0, weight=3)
        for i in range(1,5):
            self.tiitel_raam.rowconfigure(i, weight=1)
        self.tiitel_raam.columnconfigure(1, weight=1)
        self.tiitel_raam.grid(column = 0, row = 0,
                              sticky = 'nsew')

        self.tiitel_nimi = ttk.Label(self.tiitel_raam,
                                     style='Tiitel.TLabel',
                                     text='Matemaatika treener',
                                     anchor='center')
        self.tiitel_nimi.grid(column = 1, row = 0, sticky = 'nsew')

        self.start_nupp = ttk.Button(self.tiitel_raam, text='Mängima!',
                                     style='Nupp1.TButton',
                                     command=self.valikud)
        self.start_nupp.grid(column = 1, row = 1, padx = 240, sticky = 'we')

        self.juhised_nupp = ttk.Button(self.tiitel_raam,
                                       text = 'Juhised',
                                       style='Nupp1.TButton',
                                       command=self.juhised)
        self.juhised_nupp.grid(column = 1, row = 2, padx = 240, sticky = 'we')
        
        self.kinni_nupp = ttk.Button(self.tiitel_raam,
                                     text='Sulge',
                                     style='Nupp1.TButton',
                                     command=self.destroy)
        self.kinni_nupp.grid(column=1, row=4, padx = 240, sticky = 'we')
        
        self.tulemused2_nupp = ttk.Button(self.tiitel_raam,
                                          text='Tulemused',
                                          style='Nupp1.TButton',
                                          command=self.tulemused)
        self.tulemused2_nupp.grid(column=1, row = 3, padx = 240, sticky = 'we')

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

        self.juhiste_raam = ttk.Frame(self.juhised, style='Main.TFrame')
        self.juhiste_raam.grid(column = 0, row = 0,
                               sticky = 'nsew')
        #Teksti rida on 3 korda suurem kui tagasinupu rida                       
        self.juhiste_raam.rowconfigure(0, weight = 1)
        self.juhiste_raam.rowconfigure(1, weight=3)
        self.juhiste_raam.rowconfigure(2, weight = 1)

        self.juhiste_raam.columnconfigure(0, weight=1)

        self.juhised_tiitel = ttk.Label(self.juhiste_raam,
                                        text = 'Sisestuse juhised',
                                        style='Tiitel.TLabel')
        self.juhised_tiitel.grid(column = 0, row = 0)

        #Juhiste tekst tuleb failist juhised.txt, kuna siia kirjutamine
        #võtab liiga palju ruumi
        with open('juhised.txt', encoding='utf-8') as juhised_fail:
            self.juhised_text = ttk.Label(self.juhiste_raam, justify='center',
                                        text = juhised_fail.read(),
                                        style='Tulemus.TLabel',
                                        anchor='center')
        self.juhised_text.grid(column = 0, row = 1, sticky= 'nsew')

        self.juhised_kinni_nupp = ttk.Button(self.juhiste_raam, text = 'Sulge',
                                             style='Nupp1.TButton',
                                             command = self.juhised.destroy)
        self.juhised_kinni_nupp.grid(column = 0, row = 2)
        
    def valikud(self):
        self.tiitel_raam.destroy()
        self.valikute_raam = ttk.Frame(self)
        self.valikute_raam.rowconfigure(0, weight = 2)
        self.valikute_raam.rowconfigure(1, weight=1)
        self.valikute_raam.rowconfigure(2, weight=1)
        self.valikute_raam.rowconfigure(3, weight=1)
        self.valikute_raam.rowconfigure(4, weight=2)
        self.valikute_raam.columnconfigure(0, weight=1)
        self.valikute_raam.grid(column=0, row=0, sticky='nsew')

        self.info_label = ttk.Label(self.valikute_raam,
                                    text='Mängurežiimi valik',
                                    style='Tiitel.TLabel',
                                    anchor='center')
        self.info_label.grid(row=0,column=0, sticky='nsew')

        self.valik = tk.StringVar()
        self.valik.set('20')
        self.mang20st = ttk.Radiobutton(
            self.valikute_raam,
            text='Mäng 20 küsimusega',
            variable=self.valik,
            value='20', style='Raadio.TRadiobutton'
            )
        self.mangzen = ttk.Radiobutton(
            self.valikute_raam,
            text='Mäng eksimiseni', variable=self.valik,
            value='zen', style='Raadio.TRadiobutton'
            )
        self.mangaeg = ttk.Radiobutton(
            self.valikute_raam,
            text='Mäng aja peale', variable=self.valik,
            value='aeg', style='Raadio.TRadiobutton'
            )
        self.mang20st.grid(row=1,column=0, sticky='s')
        self.mangzen.grid(row=2,column=0)
        self.mangaeg.grid(row=3, column=0, sticky='n')

        self.mangunupp = ttk.Button(self.valikute_raam, text='Mängima!',
                                    style='Nupp1.TButton',
                                    command=self.mang)
        self.mangunupp.grid(row = 4, column = 0)
        
    def mang(self):

        """Teeb raami, kus sees küsitlus toimub
        ja selle raami sees olevad aknad."""
        self.tiitel_raam.destroy()

        self.mangu_raam = ttk.Frame(self, style='Main.TFrame')
        self.mangu_raam.grid(column = 0, row = 0,
                             sticky = 'nsew')
        #mängul on 1 veerg ja 5 rida, võrrandi rida on teistest
        #2 korda suurem.
        self.mangu_raam.columnconfigure(0, weight=1)
        self.mangu_raam.rowconfigure(0, weight = 2)
        for i in range(1,5):
            self.mangu_raam.rowconfigure(i, weight = 1)

        #paneb taimeri käima, kui on valitud aja peale
        if self.valik.get() == 'aeg':
            self.aeg = 120
            self.minutid = self.aeg//60
            self.sekundid = self.aeg-(self.aeg//60)*60
            if self.sekundid < 10:
                self.sekundid = '0' + str(self.sekundid)
            self.ajalabel = ttk.Label(self.mangu_raam,
                                      text=f'{self.minutid}:{self.sekundid}',
                                      style='Lugeja.TLabel')
            self.ajalabel.grid(column=0, row=3)
            self.taimer()

        #Genereeritakse lahendatav võrrand ja sellele vastav lahendus.
        self.uus_funktsioon()

        self.funktsioon = ttk.Label(self.mangu_raam)
        self.funktsioon.grid(column = 0, row = 0, sticky= 'n')

        #Tehakse uus matplotlibi figuur ja pannakse see self.funktsioon
        #labeli sisse.
        self.figuur = matplotlib.figure.Figure(figsize = (10, 2.5), dpi = 100,
                                               facecolor='#ffffff')
        self.latex = FigureCanvasTkAgg(self.figuur, master = self.funktsioon)
        self.latex.get_tk_widget().grid(column = 0, row = 0, sticky='n')
    
        #Võrrand prinditakse matplotlibi figuuri sisse
        self.figuur.text(0.5, 0.5, self.vorrand,
                         horizontalalignment = 'center',
                         verticalalignment = 'center', fontsize = 20)
        self.latex.draw()
        
        #Vastuse kasti tegemine
        self.sisestus = tk.StringVar()
        self.vastuse_kast = ttk.Entry(self.mangu_raam,
                                      background=self.taustavarv,
                                      font = ('Verdana', 20),
                                      textvariable = self.sisestus)
        self.vastuse_kast.grid(column = 0, row = 1, sticky = 'ew')

        #Kontrollimise nupp
        self.vastamis_nupp = ttk.Button(self.mangu_raam, text = 'Kontrolli',
                                        style='Nupp1.TButton',
                                        command = self.kontrolli)
        self.vastamis_nupp.grid(column = 0, row = 2)
        
        #Näitab, mitmenda küsimuse peal kasutaja on või palju aega
        if self.valik.get() == '20':
            self.loendur = ttk.Label(self.mangu_raam,
                                    style='Lugeja.TLabel',
                                    text = f'{self.kysimuse_counter}/20')
            self.loendur.grid(column = 0, row = 3)

        #Näitab, kui kasutaja on sisestanud midagi valesti, näitab
        #ka, kas vastus oli õige/vale
        self.sisestuse_info = ttk.Label(self.mangu_raam,
                                        style='Tulemus.TLabel')
        self.sisestuse_info.grid(column = 0, row = 4)

        #Enter nupp binditud kontrollimiseks, et ei
        #peaks iga kord kontrollimise nuppu vajutama
        self.bind('<Return>', self.kontrolli)
        self.vastuse_kast.focus()

    def uus_funktsioon(self):
        """valib suvaliselt ühte tüüpi võrrandi ja
           salvestab võrrandi latexi sõne ja vastused
           mängu jaoks muutujatesse"""
        self.vorrandi_number = randint(1,6)
        match self.vorrandi_number:
            case 1:
                self.vorrand, self.lahendus = fun.lineaar()
            case 2:
                self.vorrand, self.lahendus1, self.lahendus2 = fun.ruut()
            case 3:
                self.vorrand, self.lahendus = fun.eksponentsiaal()
            case 4:
                self.vorrand, self.lahendus = fun.logaritm()
            case 5:
                self.vorrand, self.lahendus = fun.trigonomeetriline()
            case 6: 
                self.vorrand, self.lahendus = fun.tuletis()
    
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
            # Tuletisfunktsiooni puhul peab lubama python
            # fromaadis valemit
            if self.vorrandi_number == 6:
                # konverdib ^ -> **
                user_expr = self.vastus.strip().replace('^', '**')
                # fun.tuletis() tagastatud valem
                expected_expr = self.lahendus

                #eval funktsioon
                safe_globals = {
                    '__builtins__': None,
                    'sin': math.sin,
                    'cos': math.cos,
                    'tan': math.tan,
                    'sqrt': math.sqrt,
                    'pi': math.pi,
                    'e': math.e,
                    'exp': math.exp,
                    'log': math.log,
                    'abs': abs,
                    'pow': pow
                }

                def safe_eval(expr, x):
                    # Eval funktsioon, mis hindab valemit
                    return eval(expr, safe_globals, {'x': x})

                # Kontrollib valemit mitme erineva x väärtusega
                sample_x = [0.3, 0.7, 1.3, 2.5, -1.2]
                tol = 1e-6
                try:
                    correct = True
                    for xv in sample_x:
                        ev_expected = safe_eval(expected_expr, xv)
                        ev_user = safe_eval(user_expr, xv)
                        #mittetäisarvuliste väärtuste kontroll
                        if not (isinstance(ev_expected, (int, float)) and
                                isinstance(ev_user, (int, float))):
                            correct = False
                            break
                        if (math.isfinite(ev_expected) and
                            math.isfinite(ev_user)):
                            if abs(ev_expected - ev_user) > tol:
                                correct = False
                                break
                        else:
                            correct = False
                            break
                except Exception:
                    self.sisestuse_info.configure(
                        text='Vigane funktsioon. Kasuta Python-süntaksit '\
                        '(nt 2*x, sin(x), e**(x)).'
                    )
                    return None

                if correct:
                    self.oiged += 1
                    self.sisestuse_info.configure(text='Õige vastus!')
                else:
                    self.sisestuse_info.configure(text='Vale vastus!')
            else:
                #kui kasutaja sisestas midagi muud peale täisarvu,
                #ütleb programmis sellest kasutajale
                try:
                    self.vastuse_number = int(self.vastus)
                except ValueError:
                    self.sisestuse_info.configure(
                        text='Sisesta vastus täisarvuna'
                        )
                    return None
                
                # Kontrollib, kas lahendus on list (trigonomeetriline) 
                # või üksik väärtus
                if isinstance(self.lahendus, list):
                    # Trigonomeetrilise võrrandi puhul peab 
                    # vastus olema üks lahendustest
                    if int(self.vastus) in self.lahendus:
                        self.oiged += 1
                        self.sisestuse_info.configure(text='Õige vastus!')
                    else:
                        self.sisestuse_info.configure(text='Vale vastus!')
                else:
                    # Teiste võrrandite puhul on tavaline võrdlus
                    if int(self.vastus) == self.lahendus:
                        self.oiged += 1
                        self.sisestuse_info.configure(text='Õige vastus!')
                    else:
                        self.sisestuse_info.configure(text='Vale vastus!')

        #genereerib uuesti suvalise võrrandi ja sellele
        #vastava lahenduse
        self.uus_funktsioon()
        
        #Lõpetab mängu, kui 20 küsimust on vastatud
        if self.valik.get() == '20':
            if self.kysimuse_counter == 20:
                self.lopp()
            else:
                self.kysimuse_counter += 1
                #Puhastab figuuri ja kirjutab uue võrrandi figuurile
                self.figuur.clear()
                self.figuur.text(0.5, 0.5, self.vorrand,
                                horizontalalignment = 'center',
                                verticalalignment = 'center',
                                fontsize = 20)
                self.latex.draw()
                #uuendab loendurit
                self.loendur.configure(text = f'{self.kysimuse_counter}/20')
                #kustutab kasutaja eelmise sisestuse
                self.vastuse_kast.delete(0, 'end')
        elif self.valik.get() == 'zen':
            if self.oiged != self.kysimuse_counter:
                self.lopp()
            else:
                self.kysimuse_counter += 1
                #Puhastab figuuri ja kirjutab uue võrrandi figuurile
                self.figuur.clear()
                self.figuur.text(0.5, 0.5, self.vorrand,
                                horizontalalignment = 'center',
                                verticalalignment = 'center',
                                fontsize = 20)
                self.latex.draw()
                #kustutab kasutaja eelmise sisestuse
                self.vastuse_kast.delete(0, 'end')
        else:
            self.kysimuse_counter += 1
            #Puhastab figuuri ja kirjutab uue võrrandi figuurile
            self.figuur.clear()
            self.figuur.text(0.5, 0.5, self.vorrand,
                            horizontalalignment = 'center',
                            verticalalignment = 'center',
                            fontsize = 20)
            self.latex.draw()
            #kustutab kasutaja eelmise sisestuse
            self.vastuse_kast.delete(0, 'end')



    def taimer(self):
        """Kui valiti aja peale, tekitab taimeri"""
        
        if self.aeg == 0:
            self.lopp()
        else:
            self.aeg -= 1
            #teeb sekundid m:ss ajaks
            self.minutid = self.aeg//60
            self.sekundid = self.aeg-(self.aeg//60)*60
            if self.sekundid < 10:
                self.sekundid = '0' + str(self.sekundid)
            self.ajalabel.configure(text=f'{self.minutid}:{self.sekundid}')
            #ootab 1000ms ja uuendab taimerit
            self.after(1000, self.taimer)

        

    def lopp(self):

        """Teeb lõpuekraani raami ja näitab tulemust.
        Saab minna tiitellehele"""
        self.unbind('<Return>')
        #Hävitab mängu raami ja loob lõpuekraani raami, kus on kasutaja
        #tulemus 20-st ja kolm nuppu
        self.mangu_raam.destroy()
        self.lopp_raam = ttk.Frame(self, style='Main.TFrame')
        self.lopp_raam.grid(column = 0, row = 0, sticky = 'nsew')
        self.lopp_raam.columnconfigure(0, weight = 1)
        self.lopp_raam.rowconfigure(0, weight = 3)
        for i in range(1,4):
            self.lopp_raam.rowconfigure(i, weight = 1)
        #Tekitab vastavale mängurežiimile vastava tulemuse labeli
        if self.valik.get() == '20':
            self.tulemus = ttk.Label(self.lopp_raam,
                                    style='Tiitel.TLabel',
                                    text = f'Sinu tulemus on {self.oiged}/20.')
        else:
            self.tulemus = ttk.Label(
                self.lopp_raam,
                style='Tiitel.TLabel',
                text=f'Vastasid {self.oiged} küsimust õigesti.'
                )
        self.tulemus.grid(column = 0, row = 0, sticky='ns')
        #Nupp, millega saab minna tiitellehele ja mängu uuesti alustada
        self.uuesti_nupp = ttk.Button(self.lopp_raam,
                                      style='Nupp1.TButton',
                                      text = 'Tagasi tiitelehele',
                                      command = self.uuesti)
        self.uuesti_nupp.grid(column = 0, row = 1, padx=240, sticky='ew')
        
        self.sulgemis_nupp_lopp = ttk.Button(self.lopp_raam,
                                             style='Nupp1.TButton',
                                             text = 'Sulge',
                                             command = self.destroy)
        self.sulgemis_nupp_lopp.grid(column = 0, row = 2,
                                     padx=240, sticky='ew')
        self.tulemuste_nupp = ttk.Button(self.lopp_raam,
                                         style='Nupp1.TButton',
                                         text='Tulemused',
                                         command = self.tulemused)
        self.tulemuste_nupp.grid(column = 0, row = 3, padx = 240, sticky='ew')

    def uuesti(self):

        """Taastab muutujate kysimuse_counter ja oiged algsed väärtused
        ning läheb tagasi tiitellehele."""
        self.kysimuse_counter = 1
        self.oiged = 0
        #Hävitab lõpuekraani raami ja läheb tagasi tiitellehe raamile
        self.lopp_raam.destroy()
        self.tiitel()
    
    def tulemused(self):
        """Tekitab tulemuste akna ja kuvab tulemused notebooki"""
        self.tulemuste_aken = tk.Toplevel(self)
        self.tulemuste_aken.geometry(f'{round(self.ekraani_laius/2)}x'
                              + f'{round(self.ekraani_korgus/2)}')
        self.tulemuste_aken.rowconfigure(0, weight = 1)
        self.tulemuste_aken.columnconfigure(0, weight = 1)
        self.tulemuste_aken.title('Tulemused')
        self.tulemuste_raam = ttk.Frame(self.tulemuste_aken,
                                        style='Main.TFrame')
        self.tulemuste_raam.grid(column=0, row=0, sticky='nsew')
        self.tulemuste_raam.rowconfigure(0, weight = 2)
        self.tulemuste_raam.rowconfigure(1, weight=1)
        self.tulemuste_raam.columnconfigure(0, weight=1)
        self.tulemuste_raam.columnconfigure(1, weight=1)


        self.tulemuste_notebook = ttk.Notebook(self.tulemuste_raam)
        self.tulemuste_notebook.grid(column=0, row=0, columnspan=2,
                                     sticky='nsew')

        self.tulemused_20st = ttk.Frame(self.tulemuste_notebook, 
                                        style='Main.TFrame')
        self.tulemused_20st.grid(row=0, column=0, sticky='nsew')
        self.tulemused_20st.rowconfigure(0, weight=1)
        self.tulemused_20st.columnconfigure(0, weight=1)
        self.tulemuste_notebook.add(self.tulemused_20st, text='Mäng 20-st')

        self.tulemused_zen = ttk.Frame(self.tulemuste_notebook,
                                       style='Main.TFrame')
        self.tulemused_zen.grid(row=0, column=0, sticky='nsew')
        self.tulemused_zen.rowconfigure(0, weight=1)
        self.tulemused_zen.columnconfigure(0, weight=1)
        self.tulemuste_notebook.add(self.tulemused_zen, text='Eksimiseni')

        self.tulemused_aeg = ttk.Frame(self.tulemuste_notebook,
                                       style='Main.TFrame')
        self.tulemused_aeg.grid(row=0, column=0, sticky='nsew')
        self.tulemused_aeg.rowconfigure(0, weight=1)
        self.tulemused_aeg.columnconfigure(0, weight=1)
        self.tulemuste_notebook.add(self.tulemused_aeg, text='Mäng aja peale')

        self.tulemuste_tekst = tk.StringVar()
        self.tulemused_zen_tekst = tk.StringVar()
        self.tulemused_aeg_tekst = tk.StringVar()
        #kui tulemuste kaustasid pole, tekitab need
        if not os.path.exists('tulemused/'):
            os.makedirs('tulemused/')
        if not os.path.exists('tulemused/tulemused-20st.csv'):
            with open('tulemused/tulemused-20st.csv','w',
                      encoding='utf-8') as fail:
                pass
        if not os.path.exists('tulemused/tulemused-zen.csv'):
            with open('tulemused/tulemused-zen.csv', 'w',
                      encoding='utf-8') as fail:
                pass
        if not os.path.exists('tulemused/tulemused-aeg.csv'):
            with open('tulemused/tulemused-aeg.csv', 'w',
                      encoding='utf-8') as fail:
                pass 
        #kõik tulemused loetakse vastavasse notebooki alaaknasse
        with open('tulemused/tulemused-20st.csv', encoding='utf-8') as t_fail:
            csv_lugeja = csv.reader(t_fail)
            for rida in csv_lugeja:
                rida_oige = ' - '.join(rida)
                self.tulemuste_tekst.set(self.tulemuste_tekst.get() +
                                         rida_oige + '/20-st\n')
        if self.tulemuste_tekst != '':
            self.tulemuste_label = ttk.Label(self.tulemused_20st,
                                            style='Tulemus.TLabel',
                                            text = self.tulemuste_tekst.get(),
                                            anchor='center')
        else:
            self.tulemuste_label = ttk.Label(self.tulemused_20st,
                                            style='Tulemus.TLabel',
                                            text = 'Tulemusi veel pole',
                                            anchor='center')
        self.tulemuste_label.grid(row=0, column=0, sticky='nsew')

        with open('tulemused/tulemused-zen.csv', encoding='utf-8') as tz_fail:
            csv_lugeja = csv.reader(tz_fail)
            for rida in csv_lugeja:
                rida_oige = ' - '.join(rida)
                self.tulemused_zen_tekst.set(self.tulemused_zen_tekst.get() +
                                         rida_oige + ' õiget vastust\n')
        if self.tulemused_zen_tekst.get() != '':
            self.tulemused_zen_label = ttk.Label(self.tulemused_zen,
                                        style='Tulemus.TLabel', 
                                        text=self.tulemused_zen_tekst.get(),
                                        anchor='center')
        else:
            self.tulemused_zen_label = ttk.Label(self.tulemused_zen,
                                                 style='Tulemus.TLabel',
                                                 text='Tulemusi veel pole',
                                                 anchor='center')
        self.tulemused_zen_label.grid(row=0, column=0, sticky='nsew')

        with open('tulemused/tulemused-aeg.csv', encoding='utf-8') as ta_fail:
            csv_lugeja = csv.reader(ta_fail)
            for rida in csv_lugeja:
                rida_oige = ' - '.join(rida)
                self.tulemused_aeg_tekst.set(self.tulemused_aeg_tekst.get() +
                                         rida_oige + ' õiget vastust\n')
        if self.tulemused_aeg_tekst.get() != '':
            self.tulemused_aeg_label = ttk.Label(
                                        self.tulemused_aeg,
                                        style='Tulemus.TLabel',
                                        text=self.tulemused_aeg_tekst.get(),
                                        anchor='center')
        else:
            self.tulemused_aeg_label = ttk.Label(self.tulemused_aeg,
                                                 style='Tulemus.TLabel',
                                                 text='Tulemusi veel pole',
                                                 anchor='center')
        self.tulemused_aeg_label.grid(row=0, column=0, sticky='nsew')

        #kui tuldi tiitelraamilt, ei lase lisada uut tulemust
        if self.tiitel_raam.winfo_exists() == 1:
            self.tagasi_nupp = ttk.Button(self.tulemuste_raam, text='Tagasi', 
                                        style='Nupp1.TButton',
                                        command=self.tulemuste_aken.destroy)
            self.tagasi_nupp.grid(column = 0, row = 1, columnspan=2)
        else:
            self.tagasi_nupp = ttk.Button(self.tulemuste_raam, text='Tagasi',
                                        style='Nupp1.TButton',
                                        command=self.tulemuste_aken.destroy)
            self.tagasi_nupp.grid(column = 0, row = 1)
            self.uus_tulemus_nupp = ttk.Button(self.tulemuste_raam,
                                            style='Nupp1.TButton',
                                            text='Uus tulemus',
                                            command=self.uus_tulemus)
            self.uus_tulemus_nupp.grid(column=1, row=1)

    def uus_tulemus(self):
        """Tekitab lisamise akna koos tekstikasti ja nuppudega"""
        self.lisamise_aken = tk.Toplevel(self.tulemuste_aken)
        self.lisamise_aken.title = 'Tulemuse lisamine'
        self.lisamise_aken.rowconfigure(0)
        self.lisamise_aken.columnconfigure(0)
        self.lisamise_raam = ttk.Frame(self.lisamise_aken, style='Main.TFrame')
        self.lisamise_raam.grid(row=0, column=0)
        self.lisamise_raam.rowconfigure(0, weight=1)
        self.lisamise_raam.rowconfigure(1, weight=1)
        self.lisamise_raam.rowconfigure(2, weight=1)
        self.lisamise_raam.columnconfigure(0, weight=1)

        self.nime_text = ttk.Label(self.lisamise_raam,
                                    style='Tulemus.TLabel',
                                    text='Sisesta oma nimi:')
        self.nime_text.grid(row = 0, column = 0, columnspan=2)
        
        self.nimi = tk.StringVar()
        self.nime_kast = ttk.Entry(self.lisamise_raam,
                                    textvariable=self.nimi)
        self.nime_kast.grid(row = 1, column = 0, columnspan=2)

        self.sisestus_nupp = ttk.Button(self.lisamise_raam,
                                        style='Nupp1.TButton',
                                        text='Sisesta tulemus',
                                        command=self.lisa_tulemus)
        self.sisestus_nupp.grid(row=2,column=0,padx=15,pady=5)
        self.tagasi_nupp_tulemus = ttk.Button(self.lisamise_raam,
                                            style='Nupp1.TButton',
                                            text='Tagasi',
                                            command=self.lisamise_aken.destroy)
        self.tagasi_nupp_tulemus.grid(row=2,column=1,padx=15, pady=5)

    def lisa_tulemus(self):
        """Valib mängurežiimile vastava faili ja sisestab sinna tulemuse
        """
        if self.valik.get() == '20':
            with open('tulemused/tulemused-20st.csv', 'a',
                      encoding='utf-8') as t_fail:
                csv_kirjutaja = csv.writer(t_fail)
                csv_kirjutaja.writerow([self.nimi.get(), self.oiged])
        elif self.valik.get() == 'zen':
            with open('tulemused/tulemused-zen.csv', 'a',
                      encoding='utf-8') as tz_fail:
                csv_kirjutaja = csv.writer(tz_fail)
                csv_kirjutaja.writerow([self.nimi.get(), self.oiged])
        else:
            with open('tulemused/tulemused-aeg.csv', 'a',
                      encoding='utf-8') as ta_fail:
                csv_kirjutaja = csv.writer(ta_fail)
                csv_kirjutaja.writerow([self.nimi.get(), self.oiged])

        self.tulemuste_aken.destroy()
        self.tulemused()

if __name__ == '__main__':
    main()
