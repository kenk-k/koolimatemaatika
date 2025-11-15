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
    """Genereerib keerulisema trigonomeetrilise võrrandi LaTeX-is.
       Tagab, et lahendus (kraadides) on täisarv.
       Tagastab (vorrand, lahendus)"""

    voimalikud_lahendused = [30,45,60,90,120,135,150,180,210,225,240,270,300,315,330]
    lahendus_ = random.choice(voimalikud_lahendused)

    # väärtused kraadide jaoks (latex code, python value)
    sin_map = {
        30:(r'\frac{1}{2}', 1/2), 45:(r'\frac{\sqrt{2}}{2}', math.sqrt(2)/2),
        60:(r'\frac{\sqrt{3}}{2}', math.sqrt(3)/2), 90:(r'1', 1),
        120:(r'\frac{\sqrt{3}}{2}', math.sqrt(3)/2), 135:(r'\frac{\sqrt{2}}{2}', math.sqrt(2)/2),
        150:(r'\frac{1}{2}', 1/2), 180:(r'0', 0),
        210:(r'-\frac{1}{2}', -1/2), 225:(r'-\frac{\sqrt{2}}{2}', -math.sqrt(2)/2),
        240:(r'-\frac{\sqrt{3}}{2}', -math.sqrt(3)/2), 270:(r'-1', -1),
        300:(r'-\frac{\sqrt{3}}{2}', -math.sqrt(3)/2), 315:(r'-\frac{\sqrt{2}}{2}', -math.sqrt(2)/2),
        330:(r'-\frac{1}{2}', -1/2)
    }

    cos_map = {
        30:(r'\frac{\sqrt{3}}{2}', math.sqrt(3)/2), 45:(r'\frac{\sqrt{2}}{2}', math.sqrt(2)/2),
        60:(r'\frac{1}{2}', 1/2), 90:(r'0', 0),
        120:(r'-\frac{1}{2}', -1/2), 135:(r'-\frac{\sqrt{2}}{2}', -math.sqrt(2)/2),
        150:(r'-\frac{\sqrt{3}}{2}', -math.sqrt(3)/2), 180:(r'-1', -1),
        210:(r'-\frac{\sqrt{3}}{2}', -math.sqrt(3)/2), 225:(r'-\frac{\sqrt{2}}{2}', -math.sqrt(2)/2),
        240:(r'-\frac{1}{2}', -1/2), 270:(r'0', 0),
        300:(r'\frac{1}{2}', 1/2), 315:(r'\frac{\sqrt{2}}{2}', math.sqrt(2)/2),
        330:(r'\frac{\sqrt{3}}{2}', math.sqrt(3)/2)
    }

    kordaja = [1, 2, -1, -2, 3, -3, 1/2, -1/2]
    a = random.choice(kordaja)
    b = random.choice(kordaja)

    # votab python code vastavale vaartusele
    sin_val = sin_map[lahendus_][1]
    cos_val = cos_map[lahendus_][1]
  
   # teeb murrulise kordaja korral korrektse latex stringi
    def murd_tex(kordaja, sin_v_cos):
        if kordaja == 1: return sin_v_cos
        elif kordaja == -1: return f"-{sin_v_cos}"
        else:  # murd
            murd = Fraction(kordaja).limit_denominator()
            if murd.denominator == 1:
               return f"{murd.numerator}{sin_v_cos}"  
            else: # kontrollib kas lugeja on negatiivne
              if murd.numerator < 0:
                return rf"-\frac{{{-murd.numerator}}}{{{murd.denominator}}}{sin_v_cos}"
              else: 
                return rf"\frac{{{murd.numerator}}}{{{murd.denominator}}}{sin_v_cos}"
              
    # teisendab kraadid radiaanideks latex stringina
    def nurk_radiaanides(kraadid):
        if kraadid == 0:
            return "0"
        elif kraadid == 180:
            return r"\pi"
        else:
            murd = Fraction(kraadid, 180)
            if murd.numerator == 1:
                return rf"\frac{{\pi}}{{{murd.denominator}}}"
            else:
                return rf"\frac{{{murd.numerator}\pi}}{{{murd.denominator}}}"
    
    nurk_tex = nurk_radiaanides(lahendus_)

    # Vasaku poole loomine
    liikmed_vasakul = []
    if a != 0:
        liikmed_vasakul.append(murd_tex(a, r'\sin(x)'))
    if b != 0:
        t = murd_tex(b, r'\cos(x)')
        if t.startswith('-'):
            liikmed_vasakul.append(t)
        else:
            liikmed_vasakul.append(f"+{t}")
    
    vasak_pool = "".join(liikmed_vasakul)
    if vasak_pool.startswith('+'):
        vasak_pool = vasak_pool[1:] # + eemaldamine
    
    # Parema poole loomine
    liikmed_paremal = []
    if a != 0:
        liikmed_paremal.append(murd_tex(a, rf'\sin\left({nurk_tex}\right)'))
    if b != 0:
        t = murd_tex(b, rf'\cos\left({nurk_tex}\right)')
        if t.startswith('-'):
            liikmed_paremal.append(t)
        else:
            liikmed_paremal.append(f"+{t}")
    
    parem_pool = "".join(liikmed_paremal)
    if parem_pool.startswith('+'):
        parem_pool = parem_pool[1:]  # + eemaldamine
    

    vorrand = f"${vasak_pool} = {parem_pool}$"
    vaartus = a * sin_val + b * cos_val
    lahendus = []
    #testib koiki voimalikke lahendusi
    for nurk in voimalikud_lahendused:
        test_sin = sin_map[nurk][1]
        test_cos = cos_map[nurk][1]
        test_value = a * test_sin + b * test_cos
        
        if abs(test_value - vaartus) < 1e-10:
            lahendus.append(nurk)
            
    return vorrand, lahendus


def tuletis():
    """
    Genereerib juhusliku funktsiooni.
    Tagastab:
        (originaalfunktsioon(latex), lahendus(string))
    """

    funktsiooni_tuup = random.choice(["polünoom", "exp", "ln", "trig"])

    #Vajalik selleks, et tagastaks 4 - 5, mitte 4 + -5 (latex)
    def latex_term(kordaja, expr):
        if kordaja == 0:
            return ""
        if kordaja > 0:
            return f" + {kordaja}{expr}"
        else:
            return f" - {-kordaja}{expr}"

    #(python)
    def python_term(kordaja, expr):
        if kordaja == 0:
            return ""
        if kordaja > 0:
            return f" + {kordaja}*{expr}"
        else:
            return f" - {-kordaja}*{expr}"

   #Polunoomi lahendus
    if funktsiooni_tuup == "polünoom":
        a = random.choice([i for i in range(-5, 6) if i != 0])
        b = random.choice([i for i in range(-5, 6) if i != 0])
        c = random.randint(-5, 5)

        # LaTeX originaalfunktsioon
        vorrand = f"$f(x) = {a}x^2{latex_term(b,'x')}{latex_term(c,'')}$"

        # Python tuletisfunktsioon
        lahendus = f"{2*a}*x{python_term(b,'1')}".strip()

        return vorrand, lahendus

    #Exponentsiaali lahendus  a * e^{kx}
    if funktsiooni_tuup == "exp":
        a = random.choice([i for i in range(-5, 6) if i != 0])
        k = random.choice([i for i in range(-5, 6) if i != 0])

        vorrand = f"$f(x) = {a}e^{{{k}x}}$"
        lahendus = f"{a*k}*e**({k}*x)"

        return vorrand, lahendus

    #Logaritmi lahendus  a ln(x)
    if funktsiooni_tuup == "ln":
        a = random.choice([i for i in range(-5, 6) if i != 0])

        vorrand = f"$f(x) = {a}\\ln(x)$"
        lahendus = f"{a}/x"

        return vorrand, lahendus

    #Trigonomeetrilise lahendus  a*sin(kx) / a*cos(kx)
    if funktsiooni_tuup == "trig":
        a = random.choice([i for i in range(-5, 6) if i != 0])
        k = random.choice([1, 2, 3, 4])
        trig = random.choice(["sin", "cos"])

        if trig == "sin":
            vorrand = f"$f(x) = {a}\\sin({k}x)$"
            lahendus = f"{a*k}*cos({k}*x)"
        else:
            vorrand = f"$f(x) = {a}\\cos({k}x)$"
            lahendus = f"-{a*k}*sin({k}*x)"

        return vorrand, lahendus