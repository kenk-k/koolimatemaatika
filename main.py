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
                                     command=self.valikud)
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
        
        self.tulemused2_nupp = ttk.Button(self.tiitel_raam,
                                          text='Tulemused',
                                          style='Tiitel.TButton',
                                          command=self.tulemused)
        self.tulemused2_nupp.grid(column=0, row = 2, sticky = 'n')

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
        
    def valikud(self):
        self.tiitel_raam.destroy()
        self.valikute_raam = ttk.Frame(self)
        self.valikute_raam.rowconfigure(0, weight = 1)
        self.valikute_raam.rowconfigure(1, weight=1)
        self.valikute_raam.rowconfigure(2, weight=1)
        self.valikute_raam.rowconfigure(3, weight=1)
        self.valikute_raam.rowconfigure(4, weight=1)
        self.valikute_raam.columnconfigure(0, weight=1)
        self.valikute_raam.grid(column=0, row=0, sticky='nsew')

        self.info_label = ttk.Label(self.valikute_raam,
                                    text='Tee mängurežiimi valik!',
                                    font=20)
        self.info_label.grid(row=0,column=0)

        self.valik = tk.StringVar()
        self.valik.set('20')
        self.mang20st = ttk.Radiobutton(self.valikute_raam,
                                        text='Mäng 20 küsimusega',
                                        variable=self.valik,
                                        value='20')
        self.mangzen = ttk.Radiobutton(self.valikute_raam,
                                       text='zen', variable=self.valik,
                                       value='zen')
        self.mangaeg = ttk.Radiobutton(self.valikute_raam,
                                       text='aja peale', variable=self.valik,
                                       value='aeg')
        self.mang20st.grid(row=1,column=0)
        self.mangzen.grid(row=2,column=0)
        self.mangaeg.grid(row=3, column=0)

        self.mangunupp = ttk.Button(self.valikute_raam, text='Mängima!',
                                    command=self.mang)
        self.mangunupp.grid(row = 4, column = 0)
        
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
        self.figuur = matplotlib.figure.Figure(figsize = (6, 2), dpi = 100)
        self.latex = FigureCanvasTkAgg(self.figuur, master = self.funktsioon)
        self.latex.get_tk_widget().grid(column = 0, row = 0, sticky='ns')
    
        #Võrrand prinditakse matplotlibi figuuri sisse
        self.figuur.text(0.5, 0.5, self.vorrand,
                         horizontalalignment = 'center',
                         verticalalignment = 'center', fontsize = 20)
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
        if self.valik.get() == '20':
            self.loendur = ttk.Label(self.mangu_raam,
                                    text = f'{self.kysimuse_counter}/20')
            self.loendur.grid(column = 0, row = 3)
        elif self.valik.get() == 'aeg':
            pass

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
            # Tuletisfunktsiooni puhul peab lubama python fromaadis valemit
            if self.vorrandi_number == 6:
                # konverdib ^ -> **
                user_expr = self.vastus.strip().replace('^', '**')
                expected_expr = self.lahendus  # fun.tuletis() tagastatud valem

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
                        if not (isinstance(ev_expected, (int, float)) and isinstance(ev_user, (int, float))):
                            correct = False
                            break
                        if math.isfinite(ev_expected) and math.isfinite(ev_user):
                            if abs(ev_expected - ev_user) > tol:
                                correct = False
                                break
                        else:
                            correct = False
                            break
                except Exception:
                    self.sisestuse_info.configure(
                        text='Vigane funktsioon. Kasuta Python-süntaksit (nt 2*x, sin(x), e**(x)).'
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
                    self.sisestuse_info.configure(text='Sisesta vastus täisarvuna')
                    return None
                
                # Kontrollib, kas lahendus on list (trigonomeetriline) või üksik väärtus
                if isinstance(self.lahendus, list):
                    # Trigonomeetrilise võrrandi puhul peab vastus olema üks lahendustest
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
            pass
        

    def lopp(self):

        """Teeb lõpuekraani raami ja näitab tulemust.
        Saab minna tiitellehele"""
        #TODO: teha lõpuekraan valmis
        #Teeb nii, et Enterit vajutades enam ei kutsutaks kontrolli()
        #funktsiooni
        self.unbind('<Return>')
        #Hävitab mängu raami ja loob lõpuekraani raami, kus on kasutaja
        #tulemus 20-st ja kolm nuppu
        self.mangu_raam.destroy()
        self.lopp_raam = ttk.Frame(self)
        self.lopp_raam.grid(column = 0, row = 0, sticky = 'nsew')
        self.lopp_raam.columnconfigure(0, weight = 1)
        self.lopp_raam.columnconfigure(1, weight = 1)
        self.lopp_raam.columnconfigure(2, weight = 1)
        self.lopp_raam.rowconfigure(0, weight = 3)
        self.lopp_raam.rowconfigure(1, weight = 1)
        if self.valik.get() == '20':
            self.tulemus = ttk.Label(self.lopp_raam,
                                    text = f'Sinu tulemus on {self.oiged}/20.',
                                    font = ('Arial', 30))
        else:
            self.tulemus = ttk.Label(self.lopp_raam,
                                     text=f'Vastasid {self.oiged} küsimust õigesti.',
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
        self.tulemuste_nupp = ttk.Button(self.lopp_raam,
                                         text='Tulemused',
                                         command = self.tulemused)
        self.tulemuste_nupp.grid(column = 2, row = 1)

    def uuesti(self):

        """Taastab muutujate kysimuse_counter ja oiged algsed väärtused
        ning läheb tagasi tiitellehele."""
        self.kysimuse_counter = 1
        self.oiged = 0
        #Hävitab lõpuekraani raami ja läheb tagasi tiitellehe raamile
        self.lopp_raam.destroy()
        self.tiitel()
    
    def tulemused(self):
        """Tekitab tulemuste akna ja kuvab tulemused """
        self.tulemuste_aken = tk.Toplevel(self)
        self.tulemuste_aken.geometry(f'{round(self.ekraani_laius/2)}x'
                              + f'{round(self.ekraani_korgus/2)}')
        stiil = ttk.Style()
        stiil.configure('Raam.TFrame', background='red')
        self.tulemuste_aken.rowconfigure(0, weight = 1)
        self.tulemuste_aken.columnconfigure(0, weight = 1)
        self.tulemuste_aken.title('Tulemused')
        self.tulemuste_raam = ttk.Frame(self.tulemuste_aken,
                                        style='Raam.TFrame')
        self.tulemuste_raam.grid(column=0, row=0, sticky='nsew')
        self.tulemuste_raam.rowconfigure(0, weight = 2)
        self.tulemuste_raam.rowconfigure(1, weight=1)
        self.tulemuste_raam.columnconfigure(0, weight=1)
        self.tulemuste_raam.columnconfigure(1, weight=1)


        self.tulemuste_notebook = ttk.Notebook(self.tulemuste_raam)
        self.tulemuste_notebook.grid(column=0, row=0, columnspan=2,
                                     sticky='nsew')
        self.tulemused_20st = ttk.Frame(self.tulemuste_notebook)
        self.tulemused_20st.grid(row=0, column=0, sticky='nsew')
        self.tulemused_20st.rowconfigure(0, weight=1)
        self.tulemused_20st.columnconfigure(0, weight=1)
        self.tulemuste_notebook.add(self.tulemused_20st, text='20-st')
        self.tulemused_zen = ttk.Frame(self.tulemuste_notebook)
        self.tulemused_zen.grid(row=0, column=0, sticky='nsew')
        self.tulemused_zen.rowconfigure(0, weight=1)
        self.tulemused_zen.columnconfigure(0, weight=1)
        self.tulemuste_notebook.add(self.tulemused_zen, text='zen')
        self.tulemuste_tekst = tk.StringVar()
        self.tulemused_zen_tekst = tk.StringVar()
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
        with open('tulemused/tulemused-20st.csv', encoding='utf-8') as t_fail:
            csv_lugeja = csv.reader(t_fail)
            for rida in csv_lugeja:
                rida_oige = ' - '.join(rida)
                self.tulemuste_tekst.set(self.tulemuste_tekst.get() +
                                         rida_oige + '/20-st\n')
        if self.tulemuste_tekst != '':
            self.tulemuste_label = ttk.Label(self.tulemused_20st,
                                            text = self.tulemuste_tekst.get(),
                                            anchor='center')
        else:
            self.tulemuste_label = ttk.Label(self.tulemused_20st,
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
                                                 text=self.tulemused_zen_tekst.get(),
                                                 anchor='center')
        else:
            self.tulemused_zen_label = ttk.Label(self.tulemused_zen,
                                                 text='Tulemusi veel pole',
                                                 anchor='center')
        self.tulemused_zen_label.grid(row=0, column=0, sticky='nsew')
        if self.tiitel_raam.winfo_exists() == 1:
            self.tagasi_nupp = ttk.Button(self.tulemuste_raam, text='Tagasi', 
                                        command=self.tulemuste_aken.destroy)
            self.tagasi_nupp.grid(column = 0, row = 1, columnspan=2)
        else:
            self.tagasi_nupp = ttk.Button(self.tulemuste_raam, text='Tagasi', 
                                        command=self.tulemuste_aken.destroy)
            self.tagasi_nupp.grid(column = 0, row = 1)
            self.uus_tulemus_nupp = ttk.Button(self.tulemuste_raam,
                                            text='Uus tulemus',
                                            command=self.uus_tulemus)
            self.uus_tulemus_nupp.grid(column=1, row=1)

    def uus_tulemus(self):
        self.lisamise_aken = tk.Toplevel(self.tulemuste_aken)
        self.lisamise_aken.rowconfigure(0)
        self.lisamise_aken.columnconfigure(0)
        self.lisamise_raam = ttk.Frame(self.lisamise_aken)
        self.lisamise_raam.grid(row=0, column=0)
        self.lisamise_raam.rowconfigure(0, weight=1)
        self.lisamise_raam.rowconfigure(1, weight=1)
        self.lisamise_raam.rowconfigure(2, weight=1)
        self.lisamise_raam.columnconfigure(0, weight=1)

        self.nime_text = ttk.Label(self.lisamise_raam,
                                    text='Sisesta oma nimi:')
        self.nime_text.grid(row = 0, column = 0)
        
        self.nimi = tk.StringVar()
        self.nime_kast = ttk.Entry(self.lisamise_raam,
                                    textvariable=self.nimi)
        self.nime_kast.grid(row = 1, column = 0)

        self.sisestus_nupp = ttk.Button(self.lisamise_raam,
                                        text='Sisesta tulemus',
                                        command=self.lisa_tulemus)
        self.sisestus_nupp.grid(row=0,column=1)
        self.tagasi_nupp_tulemus = ttk.Button(self.lisamise_raam,
                                              text='Tagasi',
                                              command=self.lisamise_aken.destroy)
        self.tagasi_nupp_tulemus.grid(row=1,column=1)
    def lisa_tulemus(self):
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
        self.tulemuste_aken.destroy()
        self.tulemused()

if __name__ == '__main__':
    main()
