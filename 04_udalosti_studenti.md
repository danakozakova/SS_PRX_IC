# PRX · Téma 04 — Udalosti a stav appky

**Cieľ:** naučiť appku **reagovať**. Doteraz sme len skladali a pozerali — tlačidlo síce bolo v okne, ale po kliknutí sa nič nestalo. Dnes mu dáme **prácu**: keď ho stlačím, niečo sa stane.

A druhá nová vec: appka si bude vedieť **niečo pamätať** (napr. koľkokrát som klikol). To voláme **stav appky**.

Pracujeme v `app.py`. Keď niečo nefunguje, prvé je **prečítať chybu v termináli**.

> Spustenie: v termináli VS Code (s aktívnym `.venv`) napíš `python app.py`.

> **Ako čítať pseudokód nižšie:** je to **recept**, nie hotový kód na skopírovanie. Hovorí, *čo* má appka spraviť a v akom poradí. Tvoja úloha je prepísať každý krok do skutočného Pythonu — na presné názvy, zátvorky a odsadenie prídeš sám (a práve to sa dnes učíš).

---

## Etuda 0 — Rozcvička: nadpis a tlačidlo pod sebou

Aby sme mali čo klikať a kam písať výsledok, poskladáme si z minula jednoduché okno: hore nápis, dole tlačidlo.

```text
Importuj: App, Label, Button, BoxLayout

Trieda MojaApp (je to App):
    build():
        koreň = zvislý BoxLayout
        do koreňa pridaj Label s textom "Zatiaľ nič"
        do koreňa pridaj Button s textom "Klikni ma"
        vráť koreň

Spusti MojaApp
```

**Otázka:** Klikni na tlačidlo. Čo sa stane? (Odpoveď: nič — a to dnes zmeníme.)

---

## Etuda 1 — Prvá reakcia: tlačidlo niečo spraví

Chceme, aby sa po stlačení tlačidla niečo stalo. Na to appke pridáme **vlastnú funkciu** — kúsok kódu, ktorý sa spustí **až vtedy, keď na tlačidlo klikneme**.

```text
Importuj: App, Button

Trieda MojaApp:
    build():
        tlacidlo = Button s textom "Klikni ma"
        naviaž tlačidlo: keď sa stlačí (on_press) → zavolaj funkciu klik
        vráť tlacidlo

    funkcia klik(self, instancia):
        vypíš do terminálu "Niekto ma klikol!"

Spusti MojaApp
```

Dve nové veci:
- **naviazanie (`bind`)** — povieme tlačidlu: *„keď ťa stlačia, spusti funkciu `klik`."* Pozor: píšeme **meno** funkcie, nevoláme ju (bez zátvoriek).
- **vlastná funkcia `klik`** — patrí appke, preto má `self`. `instancia` je to tlačidlo, ktoré nás zavolalo — zatiaľ ho nepotrebujeme, ale napísané tam byť musí.

Výsledok uvidíš **v termináli** (nie v okne). Klikaj viackrát.

**Otázka:** Čo sa vypíše do terminálu, keď klikneš trikrát?

---

## Etuda 2 — Appka mení nápis v okne

Vypisovať do terminálu je fajn na skúšku, ale chceme to vidieť **v okne**. Nápis (`Label`) si preto **odložíme do appky** (`self.vysledok`), aby sme ho vedeli neskôr zmeniť:

```text
Trieda MojaApp:
    build():
        koreň = zvislý BoxLayout
        self.vysledok = Label "Zatiaľ nič"     # nápis odlož do appky cez self.
        tlacidlo = Button "Klikni ma", naviaž on_press → klik
        do koreňa pridaj self.vysledok a tlacidlo
        vráť koreň

    funkcia klik(self, instancia):
        zmeň self.vysledok.text na "Klikol si!"
```

**Prečo `self.vysledok`?** Lebo nápis vyrobíme v `build`, ale meníme ho až vo funkcii `klik`. Keď si ho odložíme do appky (`self.`), vidia ho **obe** funkcie.

**Otázka:** Zmeň text tak, aby po kliknutí písalo tvoje meno.

---

## Etuda 3 — Počítadlo: appka si pamätá číslo ⭐

Teraz nech appka **počíta**, koľkokrát som klikol. Číslo si tiež odložíme do appky (`self.pocet`) — to je **stav appky**, vec, ktorú si pamätá medzi klikmi.

```text
Trieda MojaApp:
    build():
        koreň = zvislý BoxLayout
        self.pocet = 0                         # stav: zatiaľ 0 klikov
        self.vysledok = Label "Klikov: 0"
        tlacidlo = Button "Klikni ma", naviaž on_press → klik
        do koreňa pridaj self.vysledok a tlacidlo
        vráť koreň

    funkcia klik(self, instancia):
        zvýš self.pocet o 1
        prepíš self.vysledok.text na "Klikov: <pocet>"
```

**Ľudsky:** `self.pocet` je zásuvka, kam si appka odkladá číslo. Pri každom kliku ho zoberie, pripočíta 1 a nápis prepíše.

**Otázka:** Čo by si zmenil, aby počítadlo rátalo po dvoch (0, 2, 4, …)?

---

## Etuda 4 — `on_press` vs `on_release`

Tlačidlo vie ohlásiť dve chvíle:
- `on_press` — v momente, keď ho **stlačíš** (prst/myš idú dole),
- `on_release` — keď ho **pustíš** (prst/myš idú hore).

Skús v etude 3 pri naviazaní vymeniť `on_press` za `on_release`:

```text
naviaž tlačidlo: keď sa pustí (on_release) → zavolaj funkciu klik
```

**Otázka:** Stlač tlačidlo a **podrž**, potom pusti. Pri ktorom nastavení sa počítadlo zmení skôr — pri stlačení, alebo až pri pustení?

---

## Etuda 5 — Mini prevodník: z políčka → do nápisu

Konečne necháme appku **prečítať, čo užívateľ napísal**, a niečo s tým spraviť. Spravíme prevodník centimetrov na milimetre (1 cm = 10 mm).

Políčko (`TextInput`) si tiež odložíme do appky (`self.policko`), aby sme z neho vedeli prečítať text:

```text
Importuj navyše: TextInput

Trieda MojaApp:
    build():
        koreň = zvislý BoxLayout (spacing, padding)
        self.policko = TextInput (hint "Zadaj cm", jeden riadok)
        tlacidlo = Button "Preveď na mm", naviaž on_press → preved
        self.vysledok = Label "Výsledok: —"
        do koreňa pridaj políčko, tlačidlo, výsledok
        vráť koreň

    funkcia preved(self, instancia):
        text = prečítaj self.policko.text
        ak je text celé číslo (isdigit):
            cm = preveď text na číslo (int)
            self.vysledok.text = "<cm> cm = <cm·10> mm"
        inak:
            self.vysledok.text = "Napíš celé číslo."
```

Dve veci na všimnutie:
- `self.policko.text` — takto si prečítam, čo je v políčku. Je to **text** (napr. `"5"`), nie číslo.
- **overenie `isdigit`** — overí, že v políčku je naozaj (celé) číslo. **Prevod `int(...)`** ho potom premení z textu na číslo, s ktorým sa dá počítať.

**Otázka:** Čo sa stane, keď do políčka napíšeš `ahoj` a klikneš? A prečo tam potrebujeme ten prevod na číslo (`int`)?

---

### Na koniec hodiny — odpovedz si

- Na čo slúži naviazanie (`bind`)? Čo doň píšeme?
- Prečo si nápis/políčko odkladáme do appky cez `self.`?
- Čo znamená „stav appky"? Uveď príklad (z dnešnej hodiny).

---

## ⭐ Pre šikovnejších — oživená kalkulačka

V téme 03 sme postavili **vzhľad** kalkulačky (dve políčka a výsledok). Teraz jej pridáme **mozog** — nech naozaj sčíta dve čísla.

Poskladaj okno: hore nadpis, pod ním dve políčka (`self.cislo1`, `self.cislo2`), tlačidlo `=` a dole `Label` na výsledok (`self.vysledok`). Tlačidlo naviaž na funkciu `spocitaj`:

```text
funkcia spocitaj(self, instancia):
    a = prečítaj self.cislo1.text
    b = prečítaj self.cislo2.text
    ak sú a aj b celé čísla (isdigit):
        self.vysledok.text = "Výsledok: <a + b ako čísla>"
    inak:
        self.vysledok.text = "Zadaj dve celé čísla."
```

*(Skús najprv sám — podľa receptu. Keď budeš mať hotovo, porovnaj s učiteľkiným riešením.)*

Ďalšie nápady:
1. **Vynuluj.** Pridaj druhé tlačidlo `Vynuluj`, ktoré počítadlo (etuda 3) vráti na 0.
2. **Odčítanie.** Sprav z kalkulačky odčítačku. Zvládol by si tlačidlá na `+` aj `−` naraz?
