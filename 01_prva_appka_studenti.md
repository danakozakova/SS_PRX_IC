# PRX · Téma 01 — Prvá appka v Kivy

**Cieľ:** rozbehať prvú okennú aplikáciu a osahať si, z čoho sa Kivy appka skladá — okno, widgety, udalosti, rozloženie.

Pracujeme v **jednom súbore `app.py`**, ktorý postupne rastie. **Nič nevymazávame** — každá etuda len pridá alebo upraví kúsok. Keď niečo nefunguje, čítaj chybu v termináli, nie je to nepriateľ.

> Spustenie: v termináli VS Code (s aktívnym `.venv`) napíš `python app.py`. Okno zatvoríš krížikom.

---

## Etuda 0 — Prázdne okno

Napíš presne toto a spusti:

```python
from kivy.app import App
from kivy.uix.label import Label

class MojaApp(App):
    def build(self) -> Label:
        return Label(text="Ahoj, Kivy!")

MojaApp().run()
```

**Otázka na zamyslenie:** Čo asi robí metóda `build`? Čo by sa stalo, keby si namiesto `Label` vrátil niečo iné?

---

## Etuda 1 — Widget má vlastnosti

Uprav `Label` tak, aby mal väčšie písmo a inú farbu. Skús:

```python
return Label(text="Ahoj, Kivy!", font_size="40sp", color=(0.2, 0.6, 1, 1))
```

Pohraj sa s číslami. `color` je štvorica `(R, G, B, A)`, kde každé číslo je od `0` do `1` (`A` = priehľadnosť).

**Otázka:** Ktoré vlastnosti si zmenil? Čo znamená posledná jednotka v `color`?

---

## Etuda 2 — Chcem dva widgety naraz

Skús do okna dostať **aj nápis, aj tlačidlo**. Problém: `build` vie vrátiť len **jeden** koreňový widget. Ako teda ukázať dva?

Riešenie je **kontajner** — layout. Ten do seba pojme viac widgetov:

```python
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

def build(self) -> BoxLayout:
    koren = BoxLayout(orientation="vertical")
    koren.add_widget(Label(text="Ahoj, Kivy!"))
    koren.add_widget(Button(text="Klikni ma"))
    return koren
```

**Otázka:** Čo spraví zmena `orientation="vertical"` na `"horizontal"`?

---

## Etuda 3 — Tlačidlo, ktoré reaguje

Zatiaľ tlačidlo nič nerobí. Nauč ho reagovať na kliknutie. To je **udalosť** — appka čaká a keď klikneš, zavolá tvoju funkciu:

```python
def build(self) -> BoxLayout:
    koren = BoxLayout(orientation="vertical")
    koren.add_widget(Label(text="Ahoj, Kivy!"))
    tlacidlo = Button(text="Klikni ma")
    tlacidlo.bind(on_press=self.klik)     # napoj udalosť na funkciu
    koren.add_widget(tlacidlo)
    return koren

def klik(self, tlacidlo: Button) -> None:
    print("Klikol si!")                   # pozri sa do terminálu
```

**Otázka:** Odkiaľ sa v `klik` berie parameter `tlacidlo`? Skús doňho `print(tlacidlo.text)`.

---

## Etuda 4 — Appka si niečo pamätá (počítadlo)

Nech tlačidlo **počíta kliknutia** a nápis ukazuje aktuálny počet. Na to si appka musí (1) pamätať číslo a (2) pamätať si nápis, aby ho vedela meniť:

```python
def build(self) -> BoxLayout:
    self.pocet: int = 0                       # stav appky
    self.label = Label(text="Klikov: 0", font_size="24sp")
    koren = BoxLayout(orientation="vertical")
    koren.add_widget(self.label)
    tlacidlo = Button(text="+1")
    tlacidlo.bind(on_press=self.klik)
    koren.add_widget(tlacidlo)
    return koren

def klik(self, tlacidlo: Button) -> None:
    self.pocet += 1
    self.label.text = f"Klikov: {self.pocet}"
```

**Otázka:** Prečo ukladáme nápis do `self.label`, a nie len do `label`? Akého typu je `self.pocet`?

---

## Etuda 5 — Rôzne rozloženia

Skúšaj a pozoruj:

1. `BoxLayout(orientation="horizontal")` — čo sa zmení?
2. Pridaj druhé tlačidlo `−1`, ktoré počet **znižuje** (vlastná funkcia, obdoba `klik`).
3. Vyskúšaj mriežku: `from kivy.uix.gridlayout import GridLayout`, potom `GridLayout(cols=2)` namiesto `BoxLayout`.

**Otázka:** Kedy sa ti hodí `BoxLayout` a kedy `GridLayout`?

---

## Etuda 6 (rozšírenie) — Mini appka: prevod °C → °F

Sprav malú appku: do políčka napíšem stupne Celzia, kliknem a dole sa ukáže výsledok v °F.

Nové widgety: `TextInput` (políčko na písanie). Vzorec: `F = C * 9 / 5 + 32`.

Tu už môžeš pustiť **AI ako pomocníka** — ale ty si recenzent: kódu musíš rozumieť a vedieť ho opraviť. Popros AI, nech ti to poskladá, a potom over: Prečo je tam `float(...)`? Čo sa stane, keď do políčka napíšem „mačka"?

---

### Na koniec hodiny — odpovedz si

- Z čoho sa skladá Kivy appka? (Vysvetli pojmy: `App`, widget, layout, udalosť.)
- Prečo `build` vie vrátiť len jeden widget a ako obídeme, keď chceme viac?
- Čo je „stav" appky a kde si ho appka drží?
