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
import math
from fractions import Fraction

def lineaar():

  """Genereerib täisarvulise vastuse ja
     sellele vastava lineaarvõrrandi."""
  
  lahendus = random.randint(-20, 21)
  a = random.choice([i for i in range(-20, 21) if i != 0])
  b = random.randint(-20, 21)
  #Arvutab välja, mis võrrandi parem pool peaks olema.
  c = a*lahendus + b
    
  # Vasak pool
  if a == 1:
    vasak = 'x'
  elif a == -1:
    vasak = '-x'
  else:
    vasak = f'{a}x'
  
  # b lisamine
  if b >= 0:
    vorrand = f'${vasak} + {b} = {c}$'
  else:
    vorrand = f'${vasak} - {-b} = {c}$'
  
  return vorrand, lahendus

def ruut():

  """Genereerib 2 täisarvulist vastust ja
     nendele vastava ruutvõrrandi Viete'i teoreemi abillatexis"""
  lahendus1 = random.randint(-20, 21)
  lahendus2 = random.randint(-20, 21)
  vorrandi_kordaja = random.choice([i for i in range(-4,5) if i != 0])
  vabaliige1 = lahendus1*lahendus2
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

def trigonomeetriline():
    """Genereerib lihtsustatud trigonomeetrilise võrrandi LaTeX-is.
       Kujul: a*sin(x) = constant või a*cos(x) = constant
       Tagab, et lahendus (kraadides) on täisarv.
       Tagastab (vorrand, lahendus)"""

    voimalikud_lahendused = [30, 45, 60, 90, 120, 135, 150, 180, 210, 225, 240, 270, 300, 315, 330]
    lahendus_ = random.choice(voimalikud_lahendused)

    # väärtused kraadide jaoks (latex, lugeja, nimetaja, irrationaalarv)
    # irratsionaalarv on kas '', 'sqrt(2)', 'sqrt(3)' jne
    sin_map = {
        30:(r'\frac{1}{2}', 1, 2, ''), 45:(r'\frac{\sqrt{2}}{2}', 1, 2, 'sqrt(2)'),
        60:(r'\frac{\sqrt{3}}{2}', 1, 2, 'sqrt(3)'), 90:(r'1', 1, 1, ''),
        120:(r'\frac{\sqrt{3}}{2}', 1, 2, 'sqrt(3)'), 135:(r'\frac{\sqrt{2}}{2}', 1, 2, 'sqrt(2)'),
        150:(r'\frac{1}{2}', 1, 2, ''), 180:(r'0', 0, 1, ''),
        210:(r'-\frac{1}{2}', -1, 2, ''), 225:(r'-\frac{\sqrt{2}}{2}', -1, 2, 'sqrt(2)'),
        240:(r'-\frac{\sqrt{3}}{2}', -1, 2, 'sqrt(3)'), 270:(r'-1', -1, 1, ''),
        300:(r'-\frac{\sqrt{3}}{2}', -1, 2, 'sqrt(3)'), 315:(r'-\frac{\sqrt{2}}{2}', -1, 2, 'sqrt(2)'),
        330:(r'-\frac{1}{2}', -1, 2, '')
    }

    cos_map = {
        30:(r'\frac{\sqrt{3}}{2}', 1, 2, 'sqrt(3)'), 45:(r'\frac{\sqrt{2}}{2}', 1, 2, 'sqrt(2)'),
        60:(r'\frac{1}{2}', 1, 2, ''), 90:(r'0', 0, 1, ''),
        120:(r'-\frac{1}{2}', -1, 2, ''), 135:(r'-\frac{\sqrt{2}}{2}', -1, 2, 'sqrt(2)'),
        150:(r'-\frac{\sqrt{3}}{2}', -1, 2, 'sqrt(3)'), 180:(r'-1', -1, 1, ''),
        210:(r'-\frac{\sqrt{3}}{2}', -1, 2, 'sqrt(3)'), 225:(r'-\frac{\sqrt{2}}{2}', -1, 2, 'sqrt(2)'),
        240:(r'-\frac{1}{2}', -1, 2, ''), 270:(r'0', 0, 1, ''),
        300:(r'\frac{1}{2}', 1, 2, ''), 315:(r'\frac{\sqrt{2}}{2}', 1, 2, 'sqrt(2)'),
        330:(r'\frac{\sqrt{3}}{2}', 1, 2, 'sqrt(3)')
    }

    #juhuslik kordaja
    kordaja = random.choice([1, 2, -1, -2, 3, -3, 1/2, -1/2, 3/2, -3/2, 4/3, -4/3, 1/3, -1/3, 1/4, -1/4])
    
    #juhuslik funktsioon
    trig_func = random.choice(["sin", "cos"])
    
    if trig_func == "sin":
        trig_latex_val, num, denom, irrational = sin_map[lahendus_]
        trig_latex = r'\sin(x)'
    else:
        trig_latex_val, num, denom, irrational = cos_map[lahendus_]
        trig_latex = r'\cos(x)'
    
    # Teisendab kordaja LaTeX formaati koos trig funktsiooniga vasakul
    def kordaja_latexiks(kordaja, trig):
        murd = Fraction(kordaja).limit_denominator(100)
        
        if murd.denominator == 1:
            koef = int(murd.numerator)
            if koef == 1:
                return trig
            elif koef == -1:
                return f"-{trig}"
            else:
                return f"{koef}{trig}"
        else:
            if murd.numerator < 0:
                return rf"-\frac{{{-murd.numerator}}}{{{murd.denominator}}}{trig}"
            else:
                return rf"\frac{{{murd.numerator}}}{{{murd.denominator}}}{trig}"
    
    # Korrutab kordaja ja trig väärtuse ning genereerib LaTeX kuju
    def korda_ja_latexiks(kordaja, num, denom, irratsionaalarv):
        kord_murd = Fraction(kordaja).limit_denominator(100)
        
        # Arvutab uue lugeja ja nimetaja
        uus_lugeja = kord_murd.numerator * num
        uus_nimetaja = kord_murd.denominator * denom
        
        # Lihtsutab murru
        sük = math.gcd(abs(uus_lugeja), abs(uus_nimetaja))
        uus_lugeja //= sük
        uus_nimetaja //= sük
        
        # Genereeri LaTeX
        if uus_nimetaja == 1:
            if irratsionaalarv == '':
                return str(uus_lugeja)
            else:
                sqrt_num = irratsionaalarv.split('sqrt(')[1].split(')')[0]
                if uus_lugeja == 1:
                    return f"\\sqrt{{{sqrt_num}}}"
                elif uus_lugeja == -1:
                    return f"-\\sqrt{{{sqrt_num}}}"
                else:
                    return f"{uus_lugeja}\\sqrt{{{sqrt_num}}}"
        else:
            if irratsionaalarv == '':
                if uus_lugeja < 0:
                    return rf"-\frac{{{-uus_lugeja}}}{{{uus_nimetaja}}}"
                else:
                    return rf"\frac{{{uus_lugeja}}}{{{uus_nimetaja}}}"
            else:
                sqrt_num = irratsionaalarv.split('sqrt(')[1].split(')')[0]
                if uus_lugeja == 1:
                    return rf"\frac{{\sqrt{{{sqrt_num}}}}}{{{uus_nimetaja}}}"
                elif uus_lugeja == -1:
                    return rf"-\frac{{\sqrt{{{sqrt_num}}}}}{{{uus_nimetaja}}}"
                else:
                    if uus_lugeja < 0:
                        return rf"-\frac{{{-uus_lugeja}\sqrt{{{sqrt_num}}}}}{{{uus_nimetaja}}}"
                    else:
                        return rf"\frac{{{uus_lugeja}\sqrt{{{sqrt_num}}}}}{{{uus_nimetaja}}}"
    
    # Võrrandi koostamine
    vasak_pool = kordaja_latexiks(kordaja, trig_latex)
    parem_pool_tex = korda_ja_latexiks(kordaja, num, denom, irrational)
    
    vorrand = f"${vasak_pool} = {parem_pool_tex}$"
    
    # Leiab kõik lahendused voimalikud_lahendused hulgast
    lahendus = []
    
    # Arvutab numbrilise väärtuse kontrollimiseks
    if trig_func == "sin":
        for nurk in voimalikud_lahendused:
            _, test_num, test_denom, test_irr = sin_map[nurk]
            if irrational == test_irr and num == test_num and denom == test_denom:
                lahendus.append(nurk)
    else:
        for nurk in voimalikud_lahendused:
            _, test_num, test_denom, test_irr = cos_map[nurk]
            if irrational == test_irr and num == test_num and denom == test_denom:
                lahendus.append(nurk)
    
    return vorrand, lahendus