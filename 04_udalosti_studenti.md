# PRX · Téma 04 — Udalosti a stav appky

**Cieľ:** naučiť appku **reagovať**. Doteraz sme len skladali a pozerali — tlačidlo síce bolo v okne, ale po kliknutí sa nič nestalo. Dnes mu dáme **prácu**: keď ho stlačím, niečo sa stane.

A druhá nová vec: appka si bude vedieť **niečo pamätať** (napr. koľkokrát som klikol). To voláme **stav appky**.

Pracujeme v `app.py`. Keď niečo nefunguje, prvé je **prečítať chybu v termináli**.

> Spustenie: v termináli VS Code (s aktívnym `.venv`) napíš `python app.py`.

---

## Etuda 0 — Rozcvička: nadpis a tlačidlo pod sebou

Aby sme mali čo klikať a kam písať výsledok, poskladáme si z minula jednoduché okno: hore nápis, dole tlačidlo.

```python
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

class MojaApp(App):
    def build(self) -> BoxLayout:
        koren = BoxLayout(orientation="vertical")
        koren.add_widget(Label(text="Zatiaľ nič"))
        koren.add_widget(Button(text="Klikni ma"))
        return koren

MojaApp().run()
```

**Otázka:** Klikni na tlačidlo. Čo sa stane? (Odpoveď: nič — a to dnes zmeníme.)

---

## Etuda 1 — Prvá reakcia: tlačidlo niečo spraví

Chceme, aby sa po stlačení tlačidla niečo stalo. Na to appke pridáme **vlastnú funkciu** — kúsok kódu, ktorý sa spustí **až vtedy, keď na tlačidlo klikneme**.

```python
from kivy.app import App
from kivy.uix.button import Button

class MojaApp(App):
    def build(self) -> Button:
        tlacidlo = Button(text="Klikni ma")
        tlacidlo.bind(on_press=self.klik)   # keď sa stlačí, zavolaj funkciu self.klik
        return tlacidlo

    def klik(self, instancia):
        print("Niekto ma klikol!")

MojaApp().run()
```

Dve nové veci:
- `tlacidlo.bind(on_press=self.klik)` — povieme tlačidlu: *„keď ťa stlačia, spusti funkciu `klik`."*
- `def klik(self, instancia):` — to je tá funkcia. Patrí appke, preto má `self`. `instancia` je to tlačidlo, ktoré nás zavolalo — zatiaľ ho nepotrebujeme, ale napísané tam byť musí.

Výsledok uvidíš **v termináli** (nie v okne). Klikaj viackrát.

**Otázka:** Čo sa vypíše do terminálu, keď klikneš trikrát?

---

## Etuda 2 — Appka mení nápis v okne

Vypisovať do terminálu je fajn na skúšku, ale chceme to vidieť **v okne**. Nápis (`Label`) si preto **odložíme do appky** (`self.vysledok`), aby sme ho vedeli neskôr zmeniť:

```python
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

class MojaApp(App):
    def build(self) -> BoxLayout:
        koren = BoxLayout(orientation="vertical")

        self.vysledok = Label(text="Zatiaľ nič")   # odložíme si nápis do appky
        tlacidlo = Button(text="Klikni ma")
        tlacidlo.bind(on_press=self.klik)

        koren.add_widget(self.vysledok)
        koren.add_widget(tlacidlo)
        return koren

    def klik(self, instancia):
        self.vysledok.text = "Klikol si!"        # zmeníme nápis

MojaApp().run()
```

**Prečo `self.vysledok`?** Lebo nápis vyrobíme v `build`, ale meníme ho až vo funkcii `klik`. Keď si ho odložíme do appky (`self.`), vidia ho **obe** funkcie.

**Otázka:** Zmeň text tak, aby po kliknutí písalo tvoje meno.

---

## Etuda 3 — Počítadlo: appka si pamätá číslo ⭐

Teraz nech appka **počíta**, koľkokrát som klikol. Číslo si tiež odložíme do appky (`self.pocet`) — to je **stav appky**, vec, ktorú si pamätá medzi klikmi.

```python
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

class MojaApp(App):
    def build(self) -> BoxLayout:
        koren = BoxLayout(orientation="vertical")

        self.pocet = 0                             # stav: zatiaľ 0 klikov
        self.vysledok = Label(text="Klikov: 0")
        tlacidlo = Button(text="Klikni ma")
        tlacidlo.bind(on_press=self.klik)

        koren.add_widget(self.vysledok)
        koren.add_widget(tlacidlo)
        return koren

    def klik(self, instancia):
        self.pocet = self.pocet + 1               # zvýšime o 1
        self.vysledok.text = f"Klikov: {self.pocet}"

MojaApp().run()
```

**Ľudsky:** `self.pocet` je zásuvka, kam si appka odkladá číslo. Pri každom kliku ho zoberie, pripočíta 1 a nápis prepíše.

**Otázka:** Čo by si zmenil, aby počítadlo rátalo po dvoch (0, 2, 4, …)?

---

## Etuda 4 — `on_press` vs `on_release`

Tlačidlo vie ohlásiť dve chvíle:
- `on_press` — v momente, keď ho **stlačíš** (prst/myš idú dole),
- `on_release` — keď ho **pustíš** (prst/myš idú hore).

Skús v etude 3 vymeniť `on_press` za `on_release`:

```python
tlacidlo.bind(on_release=self.klik)
```

**Otázka:** Stlač tlačidlo a **podrž**, potom pusti. Pri ktorom nastavení sa počítadlo zmení skôr — pri stlačení, alebo až pri pustení?

---

## Etuda 5 — Mini prevodník: z políčka → do nápisu

Konečne necháme appku **prečítať, čo užívateľ napísal**, a niečo s tým spraviť. Spravíme prevodník centimetrov na milimetre (1 cm = 10 mm).

Políčko (`TextInput`) si tiež odložíme do appky (`self.policko`), aby sme z neho vedeli prečítať text:

```python
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout

class MojaApp(App):
    def build(self) -> BoxLayout:
        koren = BoxLayout(orientation="vertical", spacing=10, padding=20)

        self.policko = TextInput(hint_text="Zadaj cm", multiline=False)
        tlacidlo = Button(text="Preveď na mm")
        tlacidlo.bind(on_press=self.preved)
        self.vysledok = Label(text="Výsledok: —")

        koren.add_widget(self.policko)
        koren.add_widget(tlacidlo)
        koren.add_widget(self.vysledok)
        return koren

    def preved(self, instancia):
        text = self.policko.text
        if text.isdigit():
            cm = int(text)
            self.vysledok.text = f"{cm} cm = {cm * 10} mm"
        else:
            self.vysledok.text = "Napíš celé číslo."

MojaApp().run()
```

Dve veci na všimnutie:
- `self.policko.text` — takto si prečítam, čo je v políčku. Je to **text** (napr. `"5"`), nie číslo.
- `text.isdigit()` — overí, že v políčku je naozaj (celé) číslo. `int(text)` ho potom premení z textu na číslo, s ktorým sa dá počítať.

**Otázka:** Čo sa stane, keď do políčka napíšeš `ahoj` a klikneš? A prečo tam potrebujeme ten `int(...)`?

---

### Na koniec hodiny — odpovedz si

- Na čo slúži `bind`? Čo doň píšeme?
- Prečo si nápis/políčko odkladáme do appky cez `self.`?
- Čo znamená „stav appky"? Uveď príklad (z dnešnej hodiny).

---

## ⭐ Pre šikovnejších — oživená kalkulačka

V téme 03 sme postavili **vzhľad** kalkulačky (dve políčka a výsledok). Teraz jej pridáme **mozog** — nech naozaj sčíta dve čísla.

Poskladaj okno: hore nadpis, pod ním dve políčka (`self.cislo1`, `self.cislo2`), tlačidlo `=` a dole `Label` na výsledok (`self.vysledok`). Tlačidlo naviaž na funkciu `spocitaj`:

```python
def spocitaj(self, instancia):
    a = self.cislo1.text
    b = self.cislo2.text
    if a.isdigit() and b.isdigit():
        self.vysledok.text = f"Výsledok: {int(a) + int(b)}"
    else:
        self.vysledok.text = "Zadaj dve celé čísla."
```

*(Celé riešenie je v učiteľskej ukážke — ale skús najprv sám.)*

Ďalšie nápady:
1. **Vynuluj.** Pridaj druhé tlačidlo `Vynuluj`, ktoré počítadlo (etuda 3) vráti na 0.
2. **Odčítanie.** Sprav z kalkulačky odčítačku (`int(a) - int(b)`). Zvládol by si tlačidlá na `+` aj `−` naraz?
