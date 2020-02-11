## Zajem
Na računalnik namestimo Astra SDK ter knjižnice dodamo v PATH (kot opišejo navodila). Potem prevedemo main.cpp s g++ ali clang++ in uporabimo `-std=c++14` ali višje. Potem ga zaženemo in pošljemo izhod v neko tekstovno datoteko. Na primer `./a.out > handshake.txt`.

## Priprava
Podatke lahko pripravimo z programom za pomoč `interface.py`, ki pokliče ostale podprograme (lahko pa te podprograme kličemo samostojno).

Tipična uporaba, ki podatke iz `dataset` pretvori v csv obliko (v `csv_dataset` bo ostalo še nekaj tekstovnih datotek, ki jih lahko izbrišemo)
```bash
python interface.py prepare --inputs dataset --outputs csv_dataset/
python interface.py csv --inputs csv_dataset/ --outputs csv_dataset/
```

## Analiza
Analiza se nahaja v `Astra_analysis.ipynb`
