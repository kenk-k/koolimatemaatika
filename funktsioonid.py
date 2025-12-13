"""
Autorid: Kaur Kenk, Nansen Palo
Teema: Koolimatemaatika mäng

Antud fail on koolimatemaatika mängu põhifailile lisafail,
kus on defineeritud latexi formaadis suvaliste võrrandite
ja nende lahenduste genereerimine.
"""

import random
from math import log
from fractions import Fraction

def format_term(kordaja, valem, mode='latex', esimene=False):
    """
    - eemaldab kordaja 1 ja -1
    - 1x -> x
    - lisab LaTeX-is \\cdot siis, kui vaja
    """

    if kordaja == 0:
        return ""

    # --- lihtsustab 1x -> x ---
    if valem.startswith("1x"):
        valem = valem[1:]

    murd = Fraction(kordaja).limit_denominator()
    abs_murd = abs(murd)
    on_negatiivne = murd < 0

    # --- koef LaTeX / Python kujul ---
    def koef_str():
        if abs_murd.denominator == 1:
            return str(abs_murd.numerator)
        if mode == "latex":
            return rf"\frac{{{abs_murd.numerator}}}{{{abs_murd.denominator}}}"
        return f"{abs_murd.numerator}/{abs_murd.denominator}"

    # --- keha (ilma märgita) ---
    if not valem or valem == "":
        # keha puudumisel on kordaja ise keha
        keha = koef_str()
    elif abs_murd == 1:
        # kui kordaja on 1 või -1
        keha = valem
    else:
        # kui kordaja on midagi muud
        k = koef_str()
        if mode == "latex":
            keha = f"{k}{valem}"
        else:
            keha = f"{k}*{valem}"

    # --- esimene liige ---
    if esimene:
        return f"-{keha}" if on_negatiivne else keha

    # --- järgmised liikmed ---
    märk = "-" if on_negatiivne else "+"
    return f" {märk} {keha}"


def lineaar():
    lahendus = random.randint(-20, 21)
    a = random.choice([i for i in range(-20, 21) if i != 0])
    b = random.randint(-20, 21)
    c = a * lahendus + b

    vasak = format_term(a, "x", esimene=True)
    if b != 0:
        vasak += format_term(b, "", mode='latex')
    
    return f"${vasak} = {c}$", lahendus


def ruut():
    lahendus1 = random.randint(-20, 21)
    lahendus2 = random.randint(-20, 21)
    a = random.choice([i for i in range(-4, 5) if i != 0])

    b = -a * (lahendus1 + lahendus2)
    c = a * lahendus1 * lahendus2

    vasak = format_term(a, "x^2", esimene=True)
    if b != 0:
        vasak += format_term(b, "x")
    if c != 0:
        vasak += format_term(c, "")

    return f"${vasak} = 0$", lahendus1, lahendus2


def eksponentsiaal():
    baas = random.choice([2, 3])
    kordaja = random.choice([i for i in range(-5, 6) if i != 0])
    aste = random.randint(1, 5)

    parem_pool = baas ** aste
    lahendus = log(parem_pool, baas)

    # kasuta \cdot eksponentsiaalvõrrandis, et eraldada kordaja ja baas
    murd = Fraction(kordaja).limit_denominator()
    abs_murd = abs(murd)
    
    if abs_murd == 1:
        vasak = f"{baas}^x" if kordaja > 0 else f"-{baas}^x"
    else:
        if abs_murd.denominator == 1:
            koef = str(abs_murd.numerator)
        else:
            koef = rf"\frac{{{abs_murd.numerator}}}{{{abs_murd.denominator}}}"
        
        vasak = f"{koef} \\cdot {baas}^x" if kordaja > 0 else f"-{koef} \\cdot {baas}^x"
    
    return f"${vasak} = {kordaja * parem_pool}$", lahendus


def logaritm():
    baas = random.choice([2, 3, 5, 10])
    kordaja = random.choice([i for i in range(-5, 6) if i != 0])
    aste = random.randint(1, 4)

    lahendus = baas ** aste
    parem_pool = kordaja * aste

    vasak = format_term(kordaja, rf"\log_{{{baas}}}(x)", esimene=True)
    return f"${vasak} = {parem_pool}$", lahendus


def trigonomeetriline():
    voimalikud_lahendused = [
        30, 45, 60, 90, 120, 135, 150,
        180, 210, 225, 240, 270, 300, 315, 330
    ]

    lahendus_ = random.choice(voimalikud_lahendused)

    sin_map = {
        30:(r'\frac{1}{2}',1,2,''), 45:(r'\frac{\sqrt{2}}{2}',1,2,'sqrt(2)'),
        60:(r'\frac{\sqrt{3}}{2}',1,2,'sqrt(3)'), 90:(r'1',1,1,''),
        120:(r'\frac{\sqrt{3}}{2}',1,2,'sqrt(3)'), 135:(r'\frac{\sqrt{2}}{2}',1,2,'sqrt(2)'),
        150:(r'\frac{1}{2}',1,2,''), 180:(r'0',0,1,''),
        210:(r'-\frac{1}{2}',-1,2,''), 225:(r'-\frac{\sqrt{2}}{2}',-1,2,'sqrt(2)'),
        240:(r'-\frac{\sqrt{3}}{2}',-1,2,'sqrt(3)'), 270:(r'-1',-1,1,''),
        300:(r'-\frac{\sqrt{3}}{2}',-1,2,'sqrt(3)'), 315:(r'-\frac{\sqrt{2}}{2}',-1,2,'sqrt(2)'),
        330:(r'-\frac{1}{2}',-1,2,'')
    }

    cos_map = {
        30:(r'\frac{\sqrt{3}}{2}',1,2,'sqrt(3)'), 45:(r'\frac{\sqrt{2}}{2}',1,2,'sqrt(2)'),
        60:(r'\frac{1}{2}',1,2,''), 90:(r'0',0,1,''),
        120:(r'-\frac{1}{2}',-1,2,''), 135:(r'-\frac{\sqrt{2}}{2}',-1,2,'sqrt(2)'),
        150:(r'-\frac{\sqrt{3}}{2}',-1,2,'sqrt(3)'), 180:(r'-1',-1,1,''),
        210:(r'-\frac{\sqrt{3}}{2}',-1,2,'sqrt(3)'), 225:(r'-\frac{\sqrt{2}}{2}',-1,2,'sqrt(2)'),
        240:(r'-\frac{1}{2}',-1,2,''), 270:(r'0',0,1,''),
        300:(r'\frac{1}{2}',1,2,''), 315:(r'\frac{\sqrt{2}}{2}',1,2,'sqrt(2)'),
        330:(r'\frac{\sqrt{3}}{2}',1,2,'sqrt(3)')
    }

    kordaja = random.choice([
        1, 2, -1, -2, 3, -3,
        1/2, -1/2, 3/2, -3/2,
        4/3, -4/3, 1/3, -1/3,
        1/4, -1/4
    ])

    trig_func = random.choice(["sin", "cos"])
    trig_map = sin_map if trig_func == "sin" else cos_map
    trig_latex = r'\sin(x)' if trig_func == "sin" else r'\cos(x)'

    trig_latex_val, lugeja, nimetaja, irr = trig_map[lahendus_]

    vasak = format_term(kordaja, trig_latex, esimene=True)
    vorrand = f"${vasak} = {trig_latex_val}$"

    lahendus = [
        nurk for nurk in voimalikud_lahendused
        if trig_map[nurk][1:] == (lugeja, nimetaja, irr)
    ]

    return vorrand, lahendus


def tuletis():
    funktsiooni_tuup = random.choice(["polünoom", "exp", "ln", "trig"])

    if funktsiooni_tuup == "polünoom":
        a = random.choice([i for i in range(-5, 6) if i != 0])
        b = random.choice([i for i in range(-5, 6) if i != 0])
        c = random.randint(-5, 5)

        vorrand = "$f(x) = " + format_term(a, "x^2", esimene=True)
        if b != 0:
            vorrand += format_term(b, "x")
        if c != 0:
            vorrand += format_term(c, "")
        vorrand += "$"

        lahendus = format_term(2 * a, "x", mode="python", esimene=True)
        if b != 0:
            lahendus += format_term(b, "", mode="python")

        return vorrand, lahendus.strip()

    if funktsiooni_tuup == "exp":
        a = random.choice([i for i in range(-5, 6) if i != 0])
        k = random.choice([i for i in range(-5, 6) if i != 0])

        murd = Fraction(a).limit_denominator()
        abs_murd = abs(murd)
        
        #  1x -> x
        exp_part = f"e^{{{k}x}}" if abs(k) != 1 else (f"e^x" if k == 1 else f"e^{{-x}}")
        
        if abs_murd == 1:
            exp_str = exp_part if a > 0 else f"-{exp_part}"
        else:
            if abs_murd.denominator == 1:
                koef = str(abs_murd.numerator)
            else:
                koef = rf"\frac{{{abs_murd.numerator}}}{{{abs_murd.denominator}}}"
            exp_str = f"{koef} \\cdot {exp_part}" if a > 0 else f"-{koef} \\cdot {exp_part}"
        
        vorrand = f"$f(x) = {exp_str}$"
        return vorrand, f"{a*k}*e**({k}*x)"

    if funktsiooni_tuup == "ln":
        a = random.choice([i for i in range(-5, 6) if i != 0])
        return f"$f(x) = {format_term(a, r'\ln(x)', esimene=True)}$", f"{a}/x"

    if funktsiooni_tuup == "trig":
        a = random.choice([i for i in range(-5, 6) if i != 0])
        k = random.choice([1, 2, 3, 4])
        trig = random.choice(["sin", "cos"])

        # 1x -> x
        arg = "x" if k == 1 else f"{k}x"

        if trig == "sin":
            return (
                f"$f(x) = {format_term(a, f'\\sin({arg})', esimene=True)}$",
                f"{a*k}*cos({k}*x)"
            )

        return (
            f"$f(x) = {format_term(a, f'\\cos({arg})', esimene=True)}$",
            f"-{a*k}*sin({k}*x)"
        )