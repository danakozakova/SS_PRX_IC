# PRX · Téma 03 — Praktická úloha: Prihlasovacie okno (len vzhľad)

Postav okno, ktoré **vyzerá** ako prihlasovací formulár. **Nič sa nekliká ani nepočíta** — ide čisto o rozloženie a vlastnosti prvkov.

Pracuješ v `app.py`, spúšťaš `python app.py`. Keď niečo nefunguje, prvé je **prečítať chybu v termináli**.

## Ako má okno vyzerať

```
┌─────────────────────────┐
│       Prihlásenie        │   ← nadpis
│  [ Meno…              ]  │   ← políčko
│  [ Heslo…             ]  │   ← políčko (skryté písmená)
│  [ Zrušiť ] [   OK    ]  │   ← dve tlačidlá vedľa seba
└─────────────────────────┘
```

## Prvky a ich vlastnosti

1. **Nadpis** — `Label`, `text="Prihlásenie"`, väčšie písmo (`font_size`), nech zaberá len malú časť výšky (`size_hint`).
2. **Meno** — `TextInput`, `hint_text="Meno"`, jednoriadkové (`multiline=False`).
3. **Heslo** — `TextInput`, `hint_text="Heslo"`, jednoriadkové, skryté písmená (`password=True`).
4. **Dve tlačidlá** — `Button` s textami `Zrušiť` a `OK`, **vedľa seba v jednom rade**.

## Rozloženie (dôležité — vnáranie)

- Koreň je **zvislý** `BoxLayout` — prvky idú pod seba.
- Dve tlačidlá daj do **vodorovného** `BoxLayout`-u (jeden riadok) a ten riadok vlož ako posledný do koreňa.

## Hotovo, keď

- okno má nadpis, dve políčka pod sebou a dole dve tlačidlá vedľa seba,
- do políčka „Heslo" sa dá písať a písmená sa skrývajú,
- nakreslíš si na papier **strom** (čo je v čom vnorené).

## ⭐ Pre šikovnejších

- Pridaj medzery a okraje: `spacing` a `padding` na koreňovom layoute.
- Nad nadpis pridaj malý `Label` s `text="Vitaj!"` — kde v strome ho musíš vložiť, aby bol úplne hore?
