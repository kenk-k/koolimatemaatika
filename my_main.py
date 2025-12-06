import tkinter as tk
from tkinter import ttk
from random import randint
import csv
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import funktsioonid as fun


def main():
    matplotlib.use('TkAgg')
    prog = Programm()
    prog.mainloop()


class Programm(tk.Tk):

    def __init__(self):
        super().__init__()
        self.kysimuse_counter = 1
        self.oiged = 0

        self.title('Matemaatika mäng')
        
        # Ekraani suuruse arvutamine
        self.ekraani_laius = self.winfo_screenwidth()
        self.ekraani_korgus = self.winfo_screenheight()
        self.geometry(f'{round(self.ekraani_laius/2.5)}x'
                      + f'{round(self.ekraani_korgus/1.8)}')
        
        # Tsentreerib akna ekraanil
        self.update_idletasks()
        x = (self.ekraani_laius - self.winfo_width()) // 2
        y = (self.ekraani_korgus - self.winfo_height()) // 2
        self.geometry(f'+{x}+{y}')
        
        # Seadista taustavärv
        self.configure(bg='#f0f4f8')
        
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        
        # Seadista stiilid
        self.setup_styles()
        
        self.tiitel()
        
    def setup_styles(self):
        """Seadistab kõik TTK stiilid"""
        style = ttk.Style()
        style.theme_use('clam')
        
        # Üldine raami stiil
        style.configure('Main.TFrame', background='#f0f4f8')
        style.configure('Card.TFrame', background='white', relief='flat')
        
        # Tiitli stiil
        style.configure('Title.TLabel',
                       background='#f0f4f8',
                       foreground='#2c3e50',
                       font=('Segoe UI', 48, 'bold'))
        
        # Subtitle stiil
        style.configure('Subtitle.TLabel',
                       background='#f0f4f8',
                       foreground='#7f8c8d',
                       font=('Segoe UI', 14))
        
        # Tiitelnuppude stiil
        style.configure('Play.TButton',
                       font=('Segoe UI', 18, 'bold'),
                       padding=20,
                       background='#27ae60',
                       foreground='white')
        style.map('Play.TButton',
                 background=[('active', '#2ecc71'), ('pressed', '#229954')])
        
        style.configure('Info.TButton',
                       font=('Segoe UI', 18, 'bold'),
                       padding=20,
                       background='#3498db',
                       foreground='white')
        style.map('Info.TButton',
                 background=[('active', '#5dade2'), ('pressed', '#2980b9')])
        
        style.configure('Danger.TButton',
                       font=('Segoe UI', 18, 'bold'),
                       padding=20,
                       background='#e74c3c',
                       foreground='white')
        style.map('Danger.TButton',
                 background=[('active', '#ec7063'), ('pressed', '#c0392b')])
        
        style.configure('Results.TButton',
                       font=('Segoe UI', 18, 'bold'),
                       padding=20,
                       background='#9b59b6',
                       foreground='white')
        style.map('Results.TButton',
                 background=[('active', '#af7ac5'), ('pressed', '#7d3c98')])
        
        # Tagasi nupu stiil
        style.configure('Back.TButton',
                       font=('Segoe UI', 14),
                       padding=10,
                       background='#95a5a6',
                       foreground='white')
        style.map('Back.TButton',
                 background=[('active', '#bdc3c7'), ('pressed', '#7f8c8d')])
        
        # Mängu nuppude stiil
        style.configure('Game.TButton',
                       font=('Segoe UI', 16, 'bold'),
                       padding=15)
        
        # Labeli stiilid
        style.configure('Score.TLabel',
                       background='#3498db',
                       foreground='white',
                       font=('Segoe UI', 18, 'bold'),
                       padding=15)
        
        style.configure('Counter.TLabel',
                       background='#f0f4f8',
                       foreground='#34495e',
                       font=('Segoe UI', 16))
        
        style.configure('Feedback.TLabel',
                       background='#f0f4f8',
                       font=('Segoe UI', 14, 'bold'))
        
        style.configure('Result.TLabel',
                       background='white',
                       foreground='#2c3e50',
                       font=('Segoe UI', 36, 'bold'))
        
        # Entry stiil
        style.configure('Game.TEntry',
                       fieldbackground='white',
                       font=('Segoe UI', 20))
    
    def tiitel(self):
        """Tiitli ekraan"""
        self.tiitel_raam = ttk.Frame(self, style='Main.TFrame')
        self.tiitel_raam.grid(column=0, row=0, sticky='nsew', padx=40, pady=40)
        
        self.tiitel_raam.rowconfigure(0, weight=2)
        self.tiitel_raam.rowconfigure(1, weight=1)
        self.tiitel_raam.rowconfigure(2, weight=3)
        self.tiitel_raam.columnconfigure(0, weight=1)

        # Tiitel kaardiga
        title_card = ttk.Frame(self.tiitel_raam, style='Card.TFrame', relief='raised', borderwidth=2)
        title_card.grid(column=0, row=0, sticky='ew', pady=(0, 30))
        
        self.tiitel_nimi = ttk.Label(title_card,
                                     text='🎓 Matemaatika mäng',
                                     style='Title.TLabel',
                                     anchor='center')
        self.tiitel_nimi.pack(pady=30)
        
        subtitle = ttk.Label(self.tiitel_raam,
                            text='Harjuta matemaatikat lõbusal viisil!',
                            style='Subtitle.TLabel',
                            anchor='center')
        subtitle.grid(column=0, row=1, sticky='ew', pady=(0, 40))

        # Nuppude konteiner
        buttons_frame = ttk.Frame(self.tiitel_raam, style='Main.TFrame')
        buttons_frame.grid(column=0, row=2, sticky='n')
        
        self.start_nupp = ttk.Button(buttons_frame,
                                     text='🎯 Mängima!',
                                     style='Play.TButton',
                                     width=25,
                                     command=self.mang)
        self.start_nupp.pack(pady=12)

        self.juhised_nupp = ttk.Button(buttons_frame,
                                       text='📚 Juhised',
                                       style='Info.TButton',
                                       width=25,
                                       command=self.juhised)
        self.juhised_nupp.pack(pady=12)
        
        self.tulemused2_nupp = ttk.Button(buttons_frame,
                                          text='📊 Tulemused',
                                          style='Results.TButton',
                                          width=25,
                                          command=self.tulemused)
        self.tulemused2_nupp.pack(pady=12)
        
        self.kinni_nupp = ttk.Button(buttons_frame,
                                     text='🚪 Sulge',
                                     style='Danger.TButton',
                                     width=25,
                                     command=self.destroy)
        self.kinni_nupp.pack(pady=12)

    def juhised(self):
        """Juhiste aken"""
        self.juhised_aken = tk.Toplevel(self)
        self.juhised_aken.configure(bg='#f0f4f8')
        self.juhised_aken.rowconfigure(0, weight=1)
        self.juhised_aken.columnconfigure(0, weight=1)
        self.juhised_aken.title('Sisestuse juhised')
        self.juhised_aken.geometry(f'{round(self.ekraani_laius/2)}x'
                                   + f'{round(self.ekraani_korgus/2)}')
        
        # Tsentreeri aken
        self.juhised_aken.update_idletasks()
        x = (self.ekraani_laius - self.juhised_aken.winfo_width()) // 2
        y = (self.ekraani_korgus - self.juhised_aken.winfo_height()) // 2
        self.juhised_aken.geometry(f'+{x}+{y}')

        self.juhiste_raam = ttk.Frame(self.juhised_aken, style='Main.TFrame')
        self.juhiste_raam.grid(column=0, row=0, sticky='nsew', padx=30, pady=30)
        
        self.juhiste_raam.rowconfigure(0, weight=1)
        self.juhiste_raam.rowconfigure(1, weight=0)
        self.juhiste_raam.columnconfigure(0, weight=1)

        # Juhiste kaart
        content_card = ttk.Frame(self.juhiste_raam, style='Card.TFrame', relief='raised', borderwidth=2)
        content_card.grid(column=0, row=0, sticky='nsew', pady=(0, 20))
        content_card.rowconfigure(0, weight=0)
        content_card.rowconfigure(1, weight=1)
        content_card.columnconfigure(0, weight=1)
        
        self.juhised_tiitel = ttk.Label(content_card,
                                        text='📚 Sisestuse juhised',
                                        font=('Segoe UI', 32, 'bold'),
                                        background='white',
                                        foreground='#2c3e50')
        self.juhised_tiitel.grid(column=0, row=0, pady=(30, 20))

        try:
            with open('juhised.txt', encoding='utf-8') as f:
                juhiste_sisu = f.read()
        except:
            juhiste_sisu = """Kuidas mängida:

1. Vajuta "Mängima!" nuppu
2. Lahenda kuvatud matemaatilised võrrandid
3. Sisesta vastus täisarvuna
4. Vajuta Enter või "Kontrolli"
5. Saad tagasisidet oma vastuse kohta
6. Mäng kestab 20 küsimust

Vastuste sisestamine:
- Lineaar-, eksponentsiaal-, logaritm- ja tuletisülesannete korral sisesta üks täisarv
- Ruutvõrrandi korral sisesta mõlemad lahendused kujul: x1, x2
- Trigonomeetriliste võrrandite korral sisesta nurk kraadides

Edu mängus! 🎯"""

        # Scrollitav tekst
        text_frame = ttk.Frame(content_card, style='Card.TFrame')
        text_frame.grid(column=0, row=1, sticky='nsew', padx=30, pady=(0, 30))
        
        scrollbar = ttk.Scrollbar(text_frame)
        scrollbar.pack(side='right', fill='y')
        
        self.juhised_text = tk.Text(text_frame,
                                    wrap='word',
                                    font=('Segoe UI', 12),
                                    bg='white',
                                    fg='#2c3e50',
                                    relief='flat',
                                    yscrollcommand=scrollbar.set,
                                    padx=10,
                                    pady=10)
        self.juhised_text.pack(side='left', fill='both', expand=True)
        self.juhised_text.insert('1.0', juhiste_sisu)
        self.juhised_text.config(state='disabled')
        
        scrollbar.config(command=self.juhised_text.yview)

        self.juhised_kinni_nupp = ttk.Button(self.juhiste_raam,
                                             text='← Tagasi',
                                             style='Back.TButton',
                                             command=self.juhised_aken.destroy)
        self.juhised_kinni_nupp.grid(column=0, row=1)

    def mang(self):
        """Mängu ekraan"""
        self.tiitel_raam.destroy()

        self.mangu_raam = ttk.Frame(self, style='Main.TFrame')
        self.mangu_raam.grid(column=0, row=0, sticky='nsew', padx=40, pady=40)
        
        self.mangu_raam.columnconfigure(0, weight=1)
        self.mangu_raam.rowconfigure(0, weight=0)  # Skoor
        self.mangu_raam.rowconfigure(1, weight=2)  # Võrrand
        self.mangu_raam.rowconfigure(2, weight=0)  # Sisestus
        self.mangu_raam.rowconfigure(3, weight=0)  # Nupp
        self.mangu_raam.rowconfigure(4, weight=0)  # Loendur
        self.mangu_raam.rowconfigure(5, weight=0)  # Tagasiside

        # Skoor (ülemine lint)
        score_frame = ttk.Frame(self.mangu_raam, style='Card.TFrame', relief='raised', borderwidth=2)
        score_frame.grid(column=0, row=0, sticky='ew', pady=(0, 20))
        
        self.score_label = ttk.Label(score_frame,
                                     text=f'Skoor: {self.oiged}/{self.kysimuse_counter - 1}',
                                     style='Score.TLabel',
                                     anchor='center')
        self.score_label.pack(fill='x')

        # Võrrandi kaart
        self.uus_funktsioon()
        
        equation_card = ttk.Frame(self.mangu_raam, style='Card.TFrame', relief='raised', borderwidth=2)
        equation_card.grid(column=0, row=1, sticky='nsew', pady=(0, 20))
        equation_card.rowconfigure(0, weight=1)
        equation_card.columnconfigure(0, weight=1)

        self.funktsioon = ttk.Frame(equation_card, style='Card.TFrame')
        self.funktsioon.grid(column=0, row=0, sticky='nsew', padx=20, pady=20)

        self.figuur = matplotlib.figure.Figure(figsize=(8, 3), dpi=100)
        self.figuur.patch.set_facecolor('white')
        self.latex = FigureCanvasTkAgg(self.figuur, master=self.funktsioon)
        self.latex.get_tk_widget().pack(fill='both', expand=True)
    
        self.figuur.text(0.5, 0.5, self.vorrand,
                         horizontalalignment='center',
                         verticalalignment='center',
                         fontsize=24)
        self.latex.draw()
        
        # Vastuse sisestus
        self.sisestus = tk.StringVar()
        self.vastuse_kast = ttk.Entry(self.mangu_raam,
                                      font=('Segoe UI', 20),
                                      textvariable=self.sisestus,
                                      justify='center')
        self.vastuse_kast.grid(column=0, row=2, sticky='ew', pady=(0, 15))
        self.vastuse_kast.focus()

        # Nuppude raam
        button_frame = ttk.Frame(self.mangu_raam, style='Main.TFrame')
        button_frame.grid(column=0, row=3, pady=(0, 15))
        
        self.vastamis_nupp = ttk.Button(button_frame,
                                        text='✓ Kontrolli',
                                        style='Game.TButton',
                                        command=self.kontrolli)
        self.vastamis_nupp.pack(side='left', padx=5)
        
        self.lopp_nupp = ttk.Button(button_frame,
                                    text='Lõpeta mäng',
                                    style='Back.TButton',
                                    command=self.lopp)
        self.lopp_nupp.pack(side='left', padx=5)
        
        # Loendur
        self.loendur = ttk.Label(self.mangu_raam,
                                 text=f'Küsimus {self.kysimuse_counter}/20',
                                 style='Counter.TLabel',
                                 anchor='center')
        self.loendur.grid(column=0, row=4, pady=(0, 10))

        # Tagasiside
        self.sisestuse_info = ttk.Label(self.mangu_raam,
                                        text='',
                                        style='Feedback.TLabel',
                                        anchor='center')
        self.sisestuse_info.grid(column=0, row=5)

        self.bind('<Return>', self.kontrolli)

    def uus_funktsioon(self):
        """Vali suvaline võrrand"""
        self.vorrandi_number = randint(1, 6)
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
        """Kontrolli vastust"""
        self.vastus = self.sisestus.get()
        
        if self.vorrandi_number == 2:
            vastused = self.vastus.split(', ')
            if (str(self.lahendus1) in self.vastus and
                str(self.lahendus2) in vastused):
                vastused.pop(vastused.index(str(self.lahendus1)))
                vastused.pop(vastused.index(str(self.lahendus2)))
                if vastused == []:
                    self.oiged += 1
                    self.sisestuse_info.configure(
                        text='✓ Õige vastus!',
                        foreground='#27ae60')
                else:
                    self.sisestuse_info.configure(
                        text='✗ Vale vastus!',
                        foreground='#e74c3c')
            else:
                self.sisestuse_info.configure(
                    text='✗ Vale vastus!',
                    foreground='#e74c3c')
        else:
            try:
                self.vastuse_number = int(self.vastus)
            except ValueError:
                self.sisestuse_info.configure(
                    text='⚠ Sisesta vastus täisarvuna',
                    foreground='#f39c12')
                return None
            
            if isinstance(self.lahendus, list):
                if int(self.vastus) in self.lahendus:
                    self.oiged += 1
                    self.sisestuse_info.configure(
                        text='✓ Õige vastus!',
                        foreground='#27ae60')
                else:
                    self.sisestuse_info.configure(
                        text='✗ Vale vastus!',
                        foreground='#e74c3c')
            else:
                if int(self.vastus) == self.lahendus:
                    self.oiged += 1
                    self.sisestuse_info.configure(
                        text='✓ Õige vastus!',
                        foreground='#27ae60')
                else:
                    self.sisestuse_info.configure(
                        text='✗ Vale vastus!',
                        foreground='#e74c3c')

        self.uus_funktsioon()
        self.kysimuse_counter += 1
        
        if self.kysimuse_counter > 20:
            self.lopp()
        else:
            # Uuenda skoori
            self.score_label.configure(text=f'Skoor: {self.oiged}/{self.kysimuse_counter - 1}')
            
            # Uuenda võrrandit
            self.figuur.clear()
            self.figuur.text(0.5, 0.5, self.vorrand,
                             horizontalalignment='center',
                             verticalalignment='center',
                             fontsize=24)
            self.latex.draw()
            
            self.loendur.configure(text=f'Küsimus {self.kysimuse_counter}/20')
            self.vastuse_kast.delete(0, 'end')
            self.vastuse_kast.focus()

    def lopp(self):
        """Lõpuekraan"""
        self.unbind('<Return>')
        self.mangu_raam.destroy()
        
        self.lopp_raam = ttk.Frame(self, style='Main.TFrame')
        self.lopp_raam.grid(column=0, row=0, sticky='nsew', padx=40, pady=40)
        
        self.lopp_raam.columnconfigure(0, weight=1)
        self.lopp_raam.rowconfigure(0, weight=2)
        self.lopp_raam.rowconfigure(1, weight=1)

        # Tulemuse kaart
        result_card = ttk.Frame(self.lopp_raam, style='Card.TFrame', relief='raised', borderwidth=2)
        result_card.grid(column=0, row=0, sticky='nsew', pady=(0, 30))
        
        # Emoji ja tulemus
        protsent = (self.oiged / 20) * 100
        if protsent >= 90:
            emoji = '🎉'
            tekst = 'Suurepärane!'
        elif protsent >= 70:
            emoji = '🌟'
            tekst = 'Hästi tehtud!'
        elif protsent >= 50:
            emoji = '👍'
            tekst = 'Hea töö!'
        else:
            emoji = '💪'
            tekst = 'Harjuta edasi!'
        
        emoji_label = ttk.Label(result_card,
                               text=emoji,
                               font=('Segoe UI', 72),
                               background='white',
                               anchor='center')
        emoji_label.pack(pady=(40, 10))
        
        feedback_label = ttk.Label(result_card,
                                   text=tekst,
                                   font=('Segoe UI', 28, 'bold'),
                                   background='white',
                                   foreground='#2c3e50',
                                   anchor='center')
        feedback_label.pack(pady=(0, 20))
        
        self.tulemus = ttk.Label(result_card,
                                 text=f'Sinu tulemus: {self.oiged}/20',
                                 style='Result.TLabel',
                                 anchor='center')
        self.tulemus.pack(pady=(0, 40))

        # Nupud
        buttons_frame = ttk.Frame(self.lopp_raam, style='Main.TFrame')
        buttons_frame.grid(column=0, row=1, sticky='n')
        
        self.uuesti_nupp = ttk.Button(buttons_frame,
                                      text='🔄 Mängi uuesti',
                                      style='Play.TButton',
                                      width=25,
                                      command=self.uuesti)
        self.uuesti_nupp.pack(pady=12)
        
        self.tulemuste_nupp = ttk.Button(buttons_frame,
                                         text='📊 Tulemused',
                                         style='Results.TButton',
                                         width=25,
                                         command=self.tulemused)
        self.tulemuste_nupp.pack(pady=12)
        
        self.sulgemis_nupp_lopp = ttk.Button(buttons_frame,
                                             text='🚪 Sulge',
                                             style='Danger.TButton',
                                             width=25,
                                             command=self.destroy)
        self.sulgemis_nupp_lopp.pack(pady=12)

    def uuesti(self):
        """Alusta uuesti"""
        self.kysimuse_counter = 1
        self.oiged = 0
        self.lopp_raam.destroy()
        self.tiitel()
    
    def tulemused(self):
        """Tulemuste aken"""
        self.tulemuste_aken = tk.Toplevel(self)
        self.tulemuste_aken.configure(bg='#f0f4f8')
        self.tulemuste_aken.geometry(f'{round(self.ekraani_laius/2)}x'
                                     + f'{round(self.ekraani_korgus/2)}')
        
        # Tsentreeri aken
        self.tulemuste_aken.update_idletasks()
        x = (self.ekraani_laius - self.tulemuste_aken.winfo_width()) // 2
        y = (self.ekraani_korgus - self.tulemuste_aken.winfo_height()) // 2
        self.tulemuste_aken.geometry(f'+{x}+{y}')
        
        self.tulemuste_aken.rowconfigure(0, weight=1)
        self.tulemuste_aken.columnconfigure(0, weight=1)
        self.tulemuste_aken.title('Tulemused')
        
        self.tulemuste_raam = ttk.Frame(self.tulemuste_aken, style='Main.TFrame')
        self.tulemuste_raam.grid(column=0, row=0, sticky='nsew', padx=30, pady=30)
        
        self.tulemuste_raam.rowconfigure(0, weight=0)
        self.tulemuste_raam.rowconfigure(1, weight=1)
        self.tulemuste_raam.rowconfigure(2, weight=0)
        self.tulemuste_raam.columnconfigure(0, weight=1)

        # Pealkiri
        title_label = ttk.Label(self.tulemuste_raam,
                               text='📊 Tulemused',
                               font=('Segoe UI', 32, 'bold'),
                               background='#f0f4f8',
                               foreground='#2c3e50')
        title_label.grid(column=0, row=0, pady=(0, 20))

        # Tulemuste sisu
        content_card = ttk.Frame(self.tulemuste_raam, style='Card.TFrame', relief='raised', borderwidth=2)
        content_card.grid(column=0, row=1, sticky='nsew', pady=(0, 20))
        
        info_label = ttk.Label(content_card,
                              text='Tulemuste salvestamine tuleb varsti...',
                              font=('Segoe UI', 14),
                              background='white',
                              foreground='#7f8c8d')
        info_label.pack(expand=True)

        # Tagasi nupp
        self.tagasi_nupp = ttk.Button(self.tulemuste_raam,
                                      text='← Tagasi',
                                      style='Back.TButton',
                                      command=self.tulemuste_aken.destroy)
        self.tagasi_nupp.grid(column=0, row=2)


if __name__ == '__main__':
    main()