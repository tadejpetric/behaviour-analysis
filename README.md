Analiza obnašanja
=================
### Uvod
Naloga poteka s pomočjo službe na Inštututu Jožeta Stefana, Oddeleku za avtomatiko, biokibernetiko in robotiko; zanjo sem zadolžen sam.
Analiziral bom obnašanje večih oseb, ki sodelujejo v neki nalogi, in poskusil iz podatkov ugotoviti nekatere značilnosti interakcije. Ugotovitve pa so po analizi lahko uporabljene za izdelavo robotov z določenimi značilnostmi.

### Podatki
Analizo bom naredil na dveh virih podatkov.
Prvi je že bil zajet nekaj let nazaj vendar je v zelo surovi obliki. Gre za zajete podatki pri ekspirimentu, kjer dve osebi stojita ena nasproti druge. V roki držita palico, vsaka eno stran; pod njima je zaslon. Na zaslonu se prikaže pika in osebi morata premakniti palico nad piko. Zajeti so položaji rok obeh oseb. Cilj je predstaviti podatke na razumljiv način ter poiskati ključne značilnosti premikanja, končni cilj pa je razbrati katera oseba je vodilna v sodelovanju (in kakšne značilnosti ima).
Drugi vir zajamem sam s pomočjo naprave Orbbec ( https://orbbec3d.com/product-astra-pro/ ). Naloga je pa zelo podobna, le da še napišem manjšo knižnjico za branje in celotno analizo izvedem sam, od začetka.

### Opis podatkov
Pri prvem ekspirimentu so zajeti položaji rok ob določenem času, velikost pike in položaj pike. Zajetih je bilo 16 različnih oseb, položaji pa so 3 dimenzionalni. Podatki imajo še manjše napako (npr. povsod konča palica na eno stran od pike), tako da je potrebno še razbrati napake in jih popraviti na ne-destruktiven način.
Iz naprave Orbbec pa bom zajemal skelet osebe. Naprava sicer lahko zajema še ostalo okolico (ter globino) in zvok, vendar trenutno to ni potrebno.

### Cilj analize
Cilj je ugotoviti nekaj značilnosti človeškega obnašanja, da se lahko naredi robote, ki to obnašanje posnemajo. Iščem hitrosti, sunke, odzivne čase... Stranski cilj je še poiskati povezavo med velikostjo pike in hitrostjo zadetka (če je oseba sama je že znan rezultat, da se hitreje odzivamo na večje pike, tokrat iščem če je v paru ta razlika enako očitna). Končna naloga pa je razbirati dominantno obnašanje, torej ali je mogoče ugotoviti ali katera od oseb vodi, druga pa le sledi. Možne lastnosti vodilne osebe bi lahko na primer bile to, da prej in močneje premakne palico, druga oseba pa ji le sledi in popravlja manjše napake.
Ker je to še odprto vprašanje, ni nujno, da bom prišel do odgovora, če pa se odkrije kaj, se to lahko uporabi pri izdelavi robotov s temi lastnostmi (na primer izdelava robota, ki le sledi našim navodilom. Ker bi ta robot posnemal osebo s takim obnašanjem, bi oseba, ki sodeluje z robotom dobila občutek, da je vodilna in nadzoruje položaj. Cilj je narediti robote čim bolj naravne in intuitivne).
