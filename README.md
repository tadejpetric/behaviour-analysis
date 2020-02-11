Analiza obnašanja
=================
## Uvod
Naloga poteka s pomočjo službe na Inštututu Jožeta Stefana, Oddeleku za avtomatiko, biokibernetiko in robotiko; zanjo sem zadolžen sam.
Analiziral bom obnašanje večih oseb, ki sodelujejo v neki nalogi, in poskusil iz podatkov ugotoviti nekatere značilnosti interakcije. Ugotovitve pa so po analizi lahko uporabljene za izdelavo robotov z določenimi značilnostmi.

## Podatki
Analizo bom naredil na dveh virih podatkov.
Podatke zajamem sam s pomočjo naprave [Orbbec Astra](https://orbbec3d.com/product-astra-pro/). Naprava lahko zajema skelet osebe ter ga vrne preko C++ API. Zajel bom 2 osebe, ki opravljata preprosta opravila (na primer stisk roke in udarec rok).

## Opis podatkov

Iz naprave Orbbec bom zajemal skelet osebe ter metapodatke. Naprava sicer lahko zajema še ostalo okolico (ter globino) in zvok, vendar trenutno to ni potrebno.

### Struktura CSV datoteke
V datotekah so trenutno le vnosi kjer so na kameri vidne 2 osebe. Ostale datoteke nas trenutno ne zanimajo.
Struktura csv datotek je sledeča:
`<številka okvirja>, <število okvirjev na sekundo>, <število vidnih oseb>, <id osebe>, <R^3 vektor sklepa>*17`


## Cilj analize
Cilj je ugotoviti nekaj značilnosti človeškega obnašanja, da lahko naredimo robote, ki to obnašanje posnemajo. Iščem hitrosti, sunke, odzivne čase... Končna naloga je razbirati dominantno obnašanje, torej ali je mogoče ugotoviti ali katera od oseb vodi, druga pa le sledi. Možne lastnosti vodilne osebe bi lahko na primer bile to, da prej in močneje premakne roko, druga oseba pa ji le sledi in popravlja manjše napake.
Ker je to še odprto vprašanje, ni nujno, da bom prišel do odgovora, če pa se odkrije kaj, se to lahko uporabi pri izdelavi robotov s temi lastnostmi (na primer izdelava robota, ki le sledi našim navodilom. Ker bi ta robot posnemal osebo s takim obnašanjem, bi oseba, ki sodeluje z robotom dobila občutek, da je vodilna in nadzoruje položaj. Cilj je narediti robote čim bolj naravne in intuitivne).

## Uporaba programov

Podrobnejši opis priprave podatkov se nahaja v `uporaba_programov.md`, v kratkem pa lahko uporabite program `interface.py` z vgrajeno pomočjo.

Analiza podatkov se nahaja v `Astra_analysis.ipynb`
