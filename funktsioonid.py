"""
Autorid: Kaur Kenk, Nansen Palo
Teema: Koolimatemaatika mäng

Antud fail on koolimatemaatika mängu põhifailile lisafail,
kus on defineeritud latexi formaadis suvaliste võrrandite
ja nende lahenduste genereerimine.
"""

import random
from math import log
import numpy as np

def lineaar():

  """Genereerib täisarvulise vastuse ja
     sellele vastava lineaarvõrrandi."""
  
  lahendus = random.randint(-20, 21)
  a = random.choice([i for i in range(-20, 21) if i != 0])
  b = random.randint(-20, 21)
  #Arvutab välja, mis võrrandi parem pool peaks olema.
  c = a*lahendus + b
  vorrand = f'${a}x + {b} = {c}$'
  return vorrand, lahendus

def ruut():

  """Genereerib 2 täisarvulist vastust ja
     nendele vastava ruutvõrrandi Viete'i teoreemi abillatexis"""
  lahendus1 = random.randint(-20, 21)
  lahendus2 = random.randint(-20, 21)
  vorrandi_kordaja = random.choice([i for i in range(-4,5) if i != 0])
  #TODO: teha nii, et vabaliige saab olla ka paremal pool nii, et
  #numbrid oleksid täisarvud
  #vabaliikmete_suhe = random.randint(-4, 5)
  #while vabaliikmete_suhe == 0:
  #  vabaliikmete_suhe = random.randint(-4, 5)
  #vabaliige1 = (lahendus1*lahendus2*(1-(1/vabaliikmete_suhe)))
  vabaliige1 = lahendus1*lahendus2
  #vabaliige2 = (-lahendus1*lahendus2/vabaliikmete_suhe)
  vabaliige2 = 0
  lineaar_kordaja = -(lahendus1 + lahendus2)
  # järgnev if-elif-else plokk on selle jaoks, et negatiivsete
  #kordajate puhul ei oleks latexi formaadis miinuse ees plussi
  if (vorrandi_kordaja*lineaar_kordaja < 0 and
      vorrandi_kordaja*vabaliige1 < 0):
    vorrand = ('$' + str(vorrandi_kordaja) + 'x^{2}'
               + str(vorrandi_kordaja*lineaar_kordaja) + 'x' 
               + str(vorrandi_kordaja*vabaliige1) + ' ='
               + str(vorrandi_kordaja*vabaliige2) +'$')
  elif vorrandi_kordaja*lineaar_kordaja < 0:
    vorrand = ('$' + str(vorrandi_kordaja) + 'x^{2}'
               + str(vorrandi_kordaja*lineaar_kordaja) + 'x +' 
               + str(vorrandi_kordaja*vabaliige1) + ' ='
               + str(vorrandi_kordaja*vabaliige2) +'$')
  elif vorrandi_kordaja*vabaliige1 < 0:
    vorrand = ('$' + str(vorrandi_kordaja) + 'x^{2} + '
               + str(vorrandi_kordaja*lineaar_kordaja) + 'x' 
               + str(vorrandi_kordaja*vabaliige1) + ' ='
               + str(vorrandi_kordaja*vabaliige2) +'$')
  else:
    vorrand = ('$' + str(vorrandi_kordaja) + 'x^{2} + '
               + str(vorrandi_kordaja*lineaar_kordaja) + 'x + ' 
               + str(vorrandi_kordaja*vabaliige1) + ' ='
               + str(vorrandi_kordaja*vabaliige2) +'$')
  #võtab x^2 eest 1-e ära, kui võrrandi kordaja on 1 või -1
  if vorrandi_kordaja == 1:
    vorrand = vorrand[0:1] + vorrand[2:]
  elif vorrandi_kordaja == -1:
    vorrand = vorrand[0:2] + vorrand[3:]
  return vorrand, lahendus1, lahendus2

def eksponentsiaal():

  """Genereerib latexis eksponentsiaalvõrrandi sõne ja
     vastava täisarvulise vastuse"""
  baas = random.choice([i for i in range(2, 4)])
  
  kordaja = random.choice([i for i in range(-5, 6) if i != 0])
  
  #Võrrandi parem pool on baas astmes mingi positiivne täisarv,
  #sellest ja baasist saab välja arvutada lahenduse
  parem_pool = baas**random.randint(1,5)
  lahendus = log(parem_pool, baas)
  vorrand = f"${kordaja} \\cdot {baas}^{'x'} = {parem_pool*kordaja}$"
  return vorrand, lahendus

def logaritm():

  """Genereerib latexi formaadis logaritmvõrrandi sõne ja 
     vastava täisarvulise vastuse"""
  baas = random.choice([2,3,5,10])
  #valib suvaliselt kordaja -5st 5ni nii, et kordaja ei oleks 0
  kordaja = random.choice([i for i in range(-5, 6) if i != 0])
  #lahendus on baas astmes suvaline täisarv, täisarvuliste baaside
  #korral on see täisarv.
  #TODO: mõelda välja, kuidas saada tööle murdude korral
  lahendus = baas**random.randint(1,4)
  parem_pool = round(kordaja*log(lahendus, baas))
  vorrand = ('$'+ str(kordaja)+ '\\log_{'
             + str(baas) + '}x = ' + str(parem_pool) + '$')
  return vorrand, lahendus

#TODO: lisada ln-ile funktsioon

def trigonomeetriline():
  """Genererib LaTeX-formaadis trigonomeetrilise võrrandi ja täiskraadilise lahenduse.
     Tagastab (vorrand, lahendus), kus vorrand on LaTeX-string nagu
     '$\\sin(x) = \\frac{\\sqrt{3}}{2}$' ning lahendus on kraadides."""
  angles = [0,30,45,60,90,120,135,150,180,210,225,240,270,300,315,330]
  lahendus = random.choice(angles)
  trig = random.choice(['sin', 'cos'])

  sin_map = {
    0: r'0', 30: r'\frac{1}{2}', 45: r'\frac{\sqrt{2}}{2}', 60: r'\frac{\sqrt{3}}{2}', 90: r'1',
    120: r'\frac{\sqrt{3}}{2}', 135: r'\frac{\sqrt{2}}{2}', 150: r'\frac{1}{2}', 180: r'0',
    210: r'-\frac{1}{2}', 225: r'-\frac{\sqrt{2}}{2}', 240: r'-\frac{\sqrt{3}}{2}', 270: r'-1',
    300: r'-\frac{\sqrt{3}}{2}', 315: r'-\frac{\sqrt{2}}{2}', 330: r'-\frac{1}{2}'
  }

  cos_map = {
    0: r'1', 30: r'\frac{\sqrt{3}}{2}', 45: r'\frac{\sqrt{2}}{2}', 60: r'\frac{1}{2}', 90: r'0',
    120: r'-\frac{1}{2}', 135: r'-\frac{\sqrt{2}}{2}', 150: r'-\frac{\sqrt{3}}{2}', 180: r'-1',
    210: r'-\frac{\sqrt{3}}{2}', 225: r'-\frac{\sqrt{2}}{2}', 240: r'-\frac{1}{2}', 270: r'0',
    300: r'\frac{1}{2}', 315: r'\frac{\sqrt{2}}{2}', 330: r'\frac{\sqrt{3}}{2}'
  }

  if trig == 'sin':
    val = sin_map[lahendus]
    trig_tex = r'\sin'
  else:
    val = cos_map[lahendus]
    trig_tex = r'\cos'

  vorrand = f'${trig_tex}(x) = {val}$'
  return vorrand, lahendus