# Election data collector
Third project to Engeto Python Academy.

##1. Project description
This project can use for extraction results of the parliamentary elections 2017 for selected region (example Žďár nad Sázavou).

Can choose region on link: https://volby.cz/pls/ps2017nss/ps3?xjazyk=CZ

##2. Installation of libraries
Libraries which you have to use are saved in file requirements.txt. 
It is recommended to use new venv.

You can use: pip install -r requirements.txt -> install all necessary libraries or you can install it manually in IDE.

##3. Run project
To run project collector.py in command line use 2 arguments (mandatory).

python collector.py 'link' 'file_name.csv' -> you have to use csv file

###Result are saved in new csv file.

##4. Sample project
1. argument: https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=10&xnumnuts=6105
2. argument: Zdar_nad_Sazavou.csv

Run the project:
python collector.py 'https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=10&xnumnuts=6105' 'Zdar_nad_Sazavou.csv'

###Download progress:
DOWNLOADING DATA FROM URL: https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=10&xnumnuts=6105

SAVING DATA TO FILE: Zdar_nad_Sazavou.csv

TERMINATING collector.py, ALL DATA ARE SAVED. 

###Sample output
Kód obce,Název obce,Voliči v seznamu,Vydané obálky,Platné hlasy,......
595217,Baliny,102,71,71,8,0,0,6,0,3,8,2,1,0,0,0,8,0,6,12,0,8,0,0,0,1,5,3
595241,Blažkov,229,162,161,7,0,0,15,0,9,26,2,3,4,1,1,13,0,3,36,0,16,0,0,0,0,25,0
595250,Blízkov,272,191,191,5,0,0,14,0,4,19,3,1,3,0,0,21,0,11,42,0,50,0,1,0,0,14,3
