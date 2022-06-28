# Election_data_collector

Program sberac.py projde výsledky voleb pro vybraný volební okrsek a uloží do výstupního csv souboru vybrané data pro jednotlivé obce z daného okrsku. Data čerpá z odkazu, který musí směrovat na stránky ČSÚ, viz ukázka projektu.
data, která program sběrač u každé obce načte a uloží do výstupního souboru :

kód obce
název obce
voliči v seznamu
vydané obálky
platné hlasy
počty hlasů pro kandidující strany
##2. Instalace potřebných knihoven

Před spuštěním je třeba stáhnout extra moduly, které program pro běh využívá. Jejich seznam je uveden v souboru requirements.txt. Instalaci provedete následujícím příkazem :

pip install -r requirements.txt

##3. Ukázka projektu

Výsledky voleb pro okrsek Uherské Hradiště

1. argument - https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=13&xnumnuts=7202
2. argument - vysledky_UH.csv
Spuštění programu :

python sberac.py "https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=13&xnumnuts=7202" vysledky_UH.csv
Průběh stahování:

Ukázka výstupu :

Kód obce,Název obce,Voliči v seznamu,Vydané obálky,Platné hlasy,Občanská demokratická strana,...
592013,Babice,1452,873,866,79,0,0,60,0,55,66,5,6,3,0,2,74,0,23,254,1,0,95,5,1,0,133,4
592021,Bánov,1707,1070,1063,92,2,1,75,0,117,62,10,1,11,1,2,71,1,11,293,1,0,148,6,0,0,156,2
