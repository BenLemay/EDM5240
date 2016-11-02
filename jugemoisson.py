# coding utf-8

import csv, requests
from bs4 import BeautifulSoup

url = "https://www.conseildelamagistrature.qc.ca/rapports_enquete_conseil_magistrature_du_quebec.php?page=1&count=86"

fichier = "plaintes-juges.csv"

entete = {
    "User-Agent":"Benoit Lemay, pour un cours de journalisme de donnée",
    "From":"benoit.lemay@hotmail.ca"
}

contenu = requests.get(url,headers=entete)

page = BeautifulSoup(contenu.text,"html.parser")

#print(page)
#print(page.find_all("tr")[2:])
#print(page.find_all("th")[1:6])
titre = page.find_all("th")[1:6]

plainte = []
plainte.append(titre)

for ligne in page.find_all("tr")[2:]:
    info = ligne.find_all("td")[:-1]
#    print(info)
    plainte.append(info)

    lien = ligne.a.get("href")
    lien = "https://www.conseildelamagistrature.qc.ca/" + lien
#    print(lien)
    plainte.append(lien)

#print(plainte)

    vadboncoeur = open(fichier,"a")
    nguyen = csv.writer(vadboncoeur)
    nguyen.writerow(plainte)
