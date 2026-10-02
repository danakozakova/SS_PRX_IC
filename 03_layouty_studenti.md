# PRX · Téma 03 — Layouty (kontajnery)

**Cieľ:** dostať do okna **viac widgetov naraz** a rozmiestniť ich, ako chceme. Na to slúžia **kontajnery** — v Kivy sa volajú **layouty**.

Dnes žiadne klikanie ani počítanie — iba **skladáme a pozeráme**. Ako z widgetov naučiť appku reagovať, to príde neskôr (téma 04).

Pracujeme v `app.py`. Keď niečo nefunguje, prvé je **prečítať chybu v termináli**.

> Spustenie: v termináli VS Code (s aktívnym `.venv`) napíš `python app.py`.

---

## Etuda 0 — Rozcvička: widgety z minula

Než začneme skladať viac vecí naraz, overíme si, že vieme dostať do okna **jeden** widget. Každú úlohu rieš zvlášť — vždy len **jeden widget** v `return`.

> **Keď widget vymením, musím sa pozrieť aj hore.** Každý widget (`Label`, `Button`, `TextInput`, `Image`…) je trieda a Python o nej nevie, kým ju nepriniesieme z knižnice. Ak vidíš `NameError: name '...' is not defined`, chýba ti riadok `from kivy.uix.… import …`. Názov modulu je zvyčajne názov widgetu **malými písmenami**.

1. **Tlačidlo** s nápisom `Klik` a veľkým písmom.
   - Trieda: `Button`
   - Nastav: `text`, `font_size`

2. **Políčko na heslo** — dá sa v ňom písať, ale písmená sa skrývajú (ako pri hesle). Jednoriadkové, s nápovedou `Heslo`.
   - Trieda: `TextInput`
   - Nastav: `hint_text`, `password`, `multiline`

3. **Neaktívne tlačidlo** `Nedá sa`, ktoré sa nedá stlačiť.
   - Trieda: `Button`
   - Nastav: `text`, `disabled`

4. **Farebný nápis** s textom podľa seba, tučný a v ľubovoľnej farbe.
   - Trieda: `Label`
   - Nastav: `text`, `bold`, `color`
   - *Tip:* farba je štvorica čísel v rozsahu **0–1**.

---

## Etuda 1 — Chcem v okne dve veci naraz

Skús do okna dostať **aj nápis, aj tlačidlo**:

```python
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button

class MojaApp(App):
    def build(self):
        return Label(text="Ahoj"), Button(text="Klik")   # POZOR: takto to NEPÔJDE

MojaApp().run()
```

Nepôjde to — `build` vie vrátiť len **jeden** widget. Ako teda ukázať dva?

**Riešenie je kontajner — layout.** Je to špeciálny widget, ktorý sám nič nezobrazuje, len **do seba pojme iné widgety** a rozmiestni ich:

```python
from kivy.uix.boxlayout import BoxLayout

class MojaApp(App):
    def build(self) -> BoxLayout:
        koren = BoxLayout(orientation="vertical")
        koren.add_widget(Label(text="Ahoj"))
        koren.add_widget(Button(text="Klik"))
        return koren

MojaApp().run()
```

**Otázka:** Čo robí `add_widget`? V akom poradí sa widgety ukladajú?

---

## Etuda 2 — Vodorovne alebo zvislo?

`BoxLayout` ukladá widgety **do jedného radu**. Smer radu určuje `orientation`:

```python
koren = BoxLayout(orientation="horizontal")   # skús aj "vertical"
```

**Otázka:** Prepni `orientation` medzi `"vertical"` a `"horizontal"` a spusti. Aký je rozdiel?

---

## Etuda 3 — Viac widgetov v jednom rade

Pridaj do layoutu tri tlačidlá:

```python
def build(self) -> BoxLayout:
    koren = BoxLayout(orientation="horizontal")
    koren.add_widget(Button(text="Jeden"))
    koren.add_widget(Button(text="Dva"))
    koren.add_widget(Button(text="Tri"))
    return koren
```

**Otázka:** Ako si `BoxLayout` rozdelil miesto medzi tlačidlá? Čo sa stane s ich veľkosťou, keď okno roztiahneš myšou?

---

## Etuda 4 — Mriežka jednoducho: `GridLayout`

Ak chceme okno rozdeliť na **mriežku** (tabuľku), použijeme `GridLayout` — kontajner v tvare tabuľky. Povieme mu počet stĺpcov (`cols`) a on si riadky doplní sám:

```python
from kivy.uix.gridlayout import GridLayout

def build(self) -> GridLayout:
    koren = GridLayout(cols=2)
    koren.add_widget(Button(text="A"))
    koren.add_widget(Button(text="B"))
    koren.add_widget(Button(text="C"))
    koren.add_widget(Button(text="D"))
    return koren
```

**Otázka:** Čo sa stane, keď dáš `cols=3`? A keď pridáš piate a šieste tlačidlo?

---

## Etuda 5 — Kto dostane koľko miesta (`size_hint`)

Štandardne si widgety delia miesto rovnakým dielom. Vlastnosť `size_hint` to vie zmeniť. Napr. nech je horný nápis nízky a spodná časť veľká:

```python
def build(self) -> BoxLayout:
    koren = BoxLayout(orientation="vertical")
    koren.add_widget(Label(text="Nadpis", size_hint=(1, 0.2)))   # 20 % výšky
    koren.add_widget(Button(text="Veľké tlačidlo"))              # zvyšok
    return koren
```

**Otázka:** Skús nadpisu dať `size_hint=(1, 0.5)`. Čo sa stane? Čo asi znamenajú tie dve čísla?

---

## Etuda 6 — Layout v layoute (vnáranie) ⭐

Toto je pri layoutoch to najdôležitejšie. **Layout môžeme vložiť do iného layoutu** — tak vieme spraviť zložitejšie rozloženie. Predstav si okno rozdelené na **riadky**, a v každom riadku sú vedľa seba tlačidlá.

Spravíme zvislý `BoxLayout` (koreň), a doň vložíme **dva vodorovné** `BoxLayout`-y ako dva riadky:

```python
def build(self) -> BoxLayout:
    koren = BoxLayout(orientation="vertical")

    riadok1 = BoxLayout(orientation="horizontal")
    riadok1.add_widget(Button(text="A"))
    riadok1.add_widget(Button(text="B"))

    riadok2 = BoxLayout(orientation="horizontal")
    riadok2.add_widget(Button(text="C"))
    riadok2.add_widget(Button(text="D"))

    koren.add_widget(riadok1)
    koren.add_widget(riadok2)
    return koren
```

Dostaneš tabuľku 2×2. Koreň ukladá **riadky pod seba** (vertical), každý riadok ukladá **tlačidlá vedľa seba** (horizontal).

**Otázka:** Nakresli si na papier „strom": čo je v čom vložené? Skús pridať do `riadok1` tretie tlačidlo — čo sa zmení?

---

### Na koniec hodiny — odpovedz si

- Prečo `build` vie vrátiť len jeden widget a ako obídeme, keď chceme viac?
- Čím sa líši `BoxLayout` od `GridLayout`? Kedy použiješ ktorý?
- Čo znamená „layout v layoute" (vnáranie)? Nakresli príklad.

---

## ⭐ Pre šikovnejších

1. **Rozloženie kalkulačky (len vzhľad, žiadne počítanie).** Poskladaj okno, ktoré vyzerá ako kalkulačka: hore nadpis, pod ním riadok s dvoma políčkami `TextInput` a tlačidlom „=", a dole veľký `Label` na výsledok. **Nič sa nepočíta** — ide čisto o rozloženie. *(Toto je presne kostra appky, ktorú neskôr „oživíme".)*
2. **Vycentruj tlačidlo doprostred okna** pomocou `AnchorLayout`:
   ```python
   from kivy.uix.anchorlayout import AnchorLayout
   koren = AnchorLayout(anchor_x="center", anchor_y="center")
   koren.add_widget(Button(text="Som v strede", size_hint=(0.4, 0.2)))
   ```
   *Otázka: čím sa `AnchorLayout` líši od `BoxLayout`?*
3. **Medzery a okraje.** Skús `BoxLayout(orientation="vertical", spacing=10, padding=20)`. Čo robí `spacing` a čo `padding`?
4. **Číselná klávesnica 3×4.** Skús `GridLayout(cols=3)` a pridaj tlačidlá 1–9, potom 0 a dve prázdne miesta. Je to veľa `add_widget` riadkov, však? *Keď sa neskôr naučíme **cykly**, spravíme to na pár riadkov — dnes to napíš „ručne" a uvidíš, prečo sa cykly oplatia.*
