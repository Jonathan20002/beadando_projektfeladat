Hallgató
Név: Sárközi János

## Feladat rövid leírása:
Egyszerű valutaváltó alkalmazás, amely egy grafikus felületen (Tkinter) keresztül külföldi valutát vált át forintra (HUF). A program a CIB Bank árfolyamait próbálja lekérdezni egy weboldalról, hiba esetén előre megadott tartalék árfolyamokat használ.

Modulok és a modulokban használt függvények

1. ## main.py
   - main()
     - Elindítja a Tkinter alapablakot (root), beállítja az ablak méretét és középre helyezi a képernyőn.
     - Példányosítja a CurrencyAppSJ osztályt és elindítja a mainloop-ot.

2. ## sj_gui_sj.py
   - Osztály: CurrencyAppSJ
     - __init__(self, root)
       - Elmenti a root ablakot, beállítja a címet, létrehozza a szükséges változókat és meghívja a felületet felépítő függvényt.
     - _build_ui_sj(self)
       - Felépíti a grafikus felületet (címkék, beviteli mezők, legördülő lista, gombok, eredmény kiírása).
       - Középre helyezi a fő keretet az ablakban.
     - _on_calculate_click_sj(self)
       - Eseménykezelő a "Átváltás HUF-ra" gombhoz.
       - Beolvassa és ellenőrzi a beírt összeget, lekéri az átváltási árfolyamot és kiírja az eredményt.

3. sj_rates_sj.py
   - _download_sj(url: str) -> str
     - Letölti a megadott URL HTML tartalmát (segédfüggvény).
   - _parse_rate_from_napiarfolyam_html_sj(html: str, base: str) -> float | None
     - A letöltött HTML-ből regex segítségével megpróbálja kinyerni a megadott deviza (pl. EUR) HUF árfolyamát.
   - fetch_rate_to_huf_sj(base: str) -> float
     - Megpróbálja lekérdezni az árfolyamot a weboldalról, hiba vagy sikertelen parszolás esetén tartalék (fallback) árfolyamot ad vissza.
   - convert_to_huf_sj(amount: float, base: str) -> float
     - A megadott összeget (amount) átváltja HUF-ra a fetch_rate_to_huf_sj által visszaadott árfolyam használatával.

Osztály(ok)
- CurrencyAppSJ
  - A teljes grafikus felületet és az eseménykezelést megvalósító saját osztály, amely tartalmazza a monogramot a nevében (SJ).
