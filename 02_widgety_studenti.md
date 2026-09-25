# PRX · Téma 02 — Widgety a ich vlastnosti

**Cieľ:** osahať si, že widget je „vec" v okne, ktorá má **vlastnosti** (čo píše, aké má písmo, akú farbu…). Naučíme sa tie vlastnosti nastavovať a hrať sa s nimi.

Dnes pracujeme stále len s **jedným widgetom v okne**. Ako doň dostať viac vecí naraz, to si necháme na budúcu tému (layouty).

Pracujeme v súbore `app.py`. **Nič nevymazávame** — každú étudu len upravíme kúsok kódu a spustíme znova. Keď niečo nefunguje, prvé, čo spravíš, je **prečítať chybu v termináli**. Nie je to nepriateľ, je to nápoveda.

> Spustenie: v termináli VS Code (s aktívnym `.venv`) napíš `python app.py`. Okno zatvoríš krížikom, potom uprav kód a spusti znova.

---

## Etuda 0 — Nápis v okne (rozcvička)

Napíš presne toto a spusti:

```python
from kivy.app import App
from kivy.uix.label import Label

class MojaApp(App):
    def build(self) -> Label:
        return Label(text="Ahoj, Kivy!")

MojaApp().run()
```

**Otázka:** Toto sme robili minule. Vieš vysvetliť, čo robí `build` a čo robí `run()`?

---

## Etuda 1 — Widget má vlastnosti

Widget vyrábame tak, že do zátvoriek napíšeme jeho **vlastnosti** vo forme `vlastnosť = hodnota`. Skús pridať väčšie písmo a farbu:

```python
return Label(text="Ahoj, Kivy!", font_size="40sp", color=(0.2, 0.6, 1, 1))
```

Pohraj sa s číslami:

- `color` je štvorica `(R, G, B, A)` — červená, zelená, modrá a priehľadnosť. **Každé číslo je od `0` do `1`** (pozor, nie od 0 do 255!). Napríklad `(1, 0, 0, 1)` je čistá červená.
- `font_size="40sp"` — skús `"20sp"`, `"80sp"`. (`sp` je jednotka veľkosti, ktorá sa neskôr na mobile sama prispôsobí displeju.)

**Otázka:** Akú trojicu čísel dáš pre žltú farbu? A pre bielu? Čo spraví posledné číslo, keď ho dáš na `0.3`?

---

## Etuda 2 — Namiesto nápisu tlačidlo

Zmeň `Label` na `Button`. Všimni si, že **vlastnosti sú takmer rovnaké** — widgety sa správajú podobne:

```python
from kivy.uix.button import Button

class MojaApp(App):
    def build(self) -> Button:
        return Button(text="Klikni ma", font_size="30sp", bold=True)

MojaApp().run()
```

Skús pridať aj `color=(1, 1, 0, 1)` (farba textu).

**Otázka:** Čím sa `Button` na pohľad líši od `Label`? Ktoré vlastnosti fungujú u oboch rovnako?

---

## Etuda 3 — Políčko na písanie (`TextInput`)

`TextInput` je políčko, do ktorého môže užívateľ **písať**. Zatiaľ s tým, čo napíše, nič nerobíme — len sa pozeráme, ako políčko vyzerá a ako sa doň píše.

```python
from kivy.uix.textinput import TextInput

class MojaApp(App):
    def build(self) -> TextInput:
        return TextInput(hint_text="Sem píš…", font_size="24sp", multiline=False)

MojaApp().run()
```

- `hint_text` — bledý text, ktorý poradí, čo tam napísať (zmizne, keď začneš písať).
- `multiline=False` — políčko na jeden riadok (Enter ho nezväčší).

**Otázka:** Skús spustiť a napísať do políčka svoje meno. Čo sa stane, keď `multiline` prepneš na `True`?

---

## Etuda 4 — Obrázok (`Image`) *(ak máš po ruke obrázok)*

Ak máš v priečinku nejaký obrázok (napr. `obrazok.png`), skús ho zobraziť:

```python
from kivy.uix.image import Image

class MojaApp(App):
    def build(self) -> Image:
        return Image(source="obrazok.png")

MojaApp().run()
```

**Otázka:** Čo sa stane, keď názov súboru napíšeš zle? Prečítaj, čo hovorí terminál.

---

### Na koniec hodiny — odpovedz si

- Čo je to „vlastnosť" widgetu? Vymenuj aspoň tri.
- Prečo `color=(255, 0, 0, 1)` nefunguje ako červená? Aký je správny rozsah?
- Aký je rozdiel medzi `Label`, `Button` a `TextInput`?

---

## ⭐ Pre šikovnejších

Skús objaviť (pokojne aj s pomocou AI alebo dokumentácie — ale musíš vedieť **vysvetliť každý riadok**, čo ti dá):

1. **Farebné pozadie tlačidla.** Skús `Button(text="Farebné", background_color=(0.2, 0.7, 0.3, 1))`. Zafarbí sa málo? Pridaj ešte `background_normal=""` a spusti znova. *Zamysli sa: prečo to bez tohto riadku vyzeralo inak?*
2. **Tučné a šikmé písmo, priehľadnosť.** Vyskúšaj na `Label` vlastnosti `bold=True`, `italic=True`, `opacity=0.5`.
3. **Zarovnanie textu.** Nech je text v `Label` zarovnaný vľavo hore. Budeš potrebovať tri vlastnosti naraz: `halign="left"`, `valign="top"` a `text_size=self.size`. *Otázka: prečo samotné `halign` nestačí?*
4. **Heslo.** Sprav z `TextInput` políčko na heslo — písmená sa majú skrývať. Nájdi vlastnosť, ktorá to vie (`password=…`).
5. **Neaktívne tlačidlo.** Nájdi vlastnosť, ktorá tlačidlo „zošedne" a nedá sa naň klikať (`disabled=…`).
