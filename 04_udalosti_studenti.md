# PRX · Téma 04 — Udalosti a stav appky

**Cieľ:** naučiť appku **reagovať**. Doteraz sme len skladali a pozerali — tlačidlo síce bolo v okne, ale po kliknutí sa nič nestalo. Dnes mu dáme **prácu**: keď ho stlačím, niečo sa stane.

A druhá nová vec: appka si bude vedieť **niečo pamätať** (napr. koľkokrát som klikol). To voláme **stav appky**.

Pracujeme v `app.py`. Keď niečo nefunguje, prvé je **prečítať chybu v termináli**.

> Spustenie: v termináli VS Code (s aktívnym `.venv`) napíš `python app.py`.

> **Ako čítať kostru pod každou etudou:** hlavičky (`Trieda`, `build()`, `funkcia …`) ti ukazujú, čo appka má mať. V tele je **slovom popísané, čo má daná časť robiť** — nie hotový kód. Ako to presne v Pythone zapíšeš (zátvorky, `self.`, odsadenie), je na tebe.

---

## Etuda 0 — Rozcvička: nadpis a tlačidlo pod sebou

Aby sme mali čo klikať a kam písať výsledok, poskladáme si z minula jednoduché okno: hore nápis, dole tlačidlo.

```
Trieda MojaApp:
    build():
        Okno so zvislým usporiadaním: hore nápis „Zatiaľ nič", pod ním tlačidlo „Klikni ma"
```

**Otázka:** Klikni na tlačidlo. Čo sa stane? (Odpoveď: nič — a to dnes zmeníme.)

---

## Etuda 1 — Prvá reakcia: tlačidlo niečo spraví

Chceme, aby sa po stlačení tlačidla niečo stalo. Na to appke pridáme **vlastnú funkciu** — kúsok kódu, ktorý sa spustí **až vtedy, keď na tlačidlo klikneme**.

```
Trieda MojaApp:
    build():
        Vytvor tlačidlo „Klikni ma" a nastav, aby sa pri stlačení zavolala funkcia klik

    funkcia klik(self, instancia):
        vypíše do terminálu „Niekto ma klikol!"
```

Dve nové veci:
- **naviazanie (`bind`)** — povieme tlačidlu: *„keď ťa stlačia, spusti funkciu `klik`."* Pozor: píšeme **meno** funkcie, nevoláme ju (bez zátvoriek).
- **vlastná funkcia `klik`** — patrí appke, preto má `self`. `instancia` je to tlačidlo, ktoré nás zavolalo — zatiaľ ho nepotrebujeme, ale napísané tam byť musí.

Výsledok uvidíš **v termináli** (nie v okne). Klikaj viackrát.

**Otázka:** Čo sa vypíše do terminálu, keď klikneš trikrát?

---

## Etuda 2 — Appka mení nápis v okne

Vypisovať do terminálu je fajn na skúšku, ale chceme to vidieť **v okne**. Nápis (`Label`) si preto **odložíme do appky** (`self.vysledok`), aby sme ho vedeli neskôr zmeniť:

```
Trieda MojaApp:
    build():
        Vytvor nápis (odlož si ho do appky — budeš ho meniť) a tlačidlo, ktoré pri stlačení zavolá funkciu klik

    funkcia klik(self, instancia):
        zmení text nápisu na „Klikol si!"
```

**Prečo `self.vysledok`?** Lebo nápis vyrobíme v `build`, ale meníme ho až vo funkcii `klik`. Keď si ho odložíme do appky (`self.`), vidia ho **obe** funkcie.

**Otázka:** Zmeň text tak, aby po kliknutí písalo tvoje meno.

---

## Etuda 3 — Počítadlo: appka si pamätá číslo ⭐

Teraz nech appka **počíta**, koľkokrát som klikol. Číslo si tiež odložíme do appky (`self.pocet`) — to je **stav appky**, vec, ktorú si pamätá medzi klikmi.

```
Trieda MojaApp:
    build():
        Zapamätaj si počet klikov (na začiatku 0). Vytvor nápis „Klikov: 0" a tlačidlo, ktoré pri stlačení zavolá funkciu klik

    funkcia klik(self, instancia):
        zvýši počet o 1 a prepíše nápis na aktuálny počet
```

**Ľudsky:** `self.pocet` je zásuvka, kam si appka odkladá číslo. Pri každom kliku ho zoberie, pripočíta 1 a nápis prepíše.

**Otázka:** Čo by si zmenil, aby počítadlo rátalo po dvoch (0, 2, 4, …)?

---

## Etuda 4 — `on_press` vs `on_release`

Tlačidlo vie ohlásiť dve chvíle:
- `on_press` — v momente, keď ho **stlačíš** (prst/myš idú dole),
- `on_release` — keď ho **pustíš** (prst/myš idú hore).

> To isté ako etuda 3, len v `build` nastav tlačidlo tak, aby sa funkcia `klik` volala pri **pustení** (`on_release`) namiesto stlačenia (`on_press`).

**Otázka:** Stlač tlačidlo a **podrž**, potom pusti. Pri ktorom nastavení sa počítadlo zmení skôr — pri stlačení, alebo až pri pustení?

---

## Etuda 5 — Mini prevodník: z políčka → do nápisu

Konečne necháme appku **prečítať, čo užívateľ napísal**, a niečo s tým spraviť. Spravíme prevodník centimetrov na milimetre (1 cm = 10 mm).

Políčko (`TextInput`) si tiež odložíme do appky (`self.policko`), aby sme z neho vedeli prečítať text:

```
Trieda MojaApp:
    build():
        Vytvor pole na zadanie cm (odlož si ho do appky), tlačidlo „Preveď na mm" (naviaž ho na funkciu preved) a nápis na výsledok

    funkcia preved(self, instancia):
        Prečíta text z poľa. Ak je to celé číslo, ukáže v nápise „X cm = (X·10) mm"; inak ukáže „Napíš celé číslo."
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

```
Trieda KalkulackaApp:
    build():
        Vytvor nadpis, dve polia na čísla (odlož si ich do appky), tlačidlo „=" (naviaž ho na funkciu spocitaj) a nápis na výsledok

    funkcia spocitaj(self, instancia):
        Prečíta obe polia. Ak sú v oboch celé čísla, ukáže ich súčet; inak vyzve zadať dve celé čísla
```

*(Skús najprv sám — podľa popisu. Keď budeš mať hotovo, porovnaj s učiteľkiným riešením.)*

Ďalšie nápady:
1. **Vynuluj.** Pridaj druhé tlačidlo `Vynuluj`, ktoré počítadlo (etuda 3) vráti na 0.
2. **Odčítanie.** Sprav z kalkulačky odčítačku. Zvládol by si tlačidlá na `+` aj `−` naraz?
