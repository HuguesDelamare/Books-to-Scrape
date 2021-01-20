
***INSTALLATION ENVIRONEMENT***

-Ouvrez votre CMD windows (Invite de commande en FR).

-Choisissez le lieu ou créer votre dossier qui contiendra le projet en utilisant la commande ci-dessous :
	Ex: C:\Users\NomUtilisateur>mkdir NomDossier

-Installez l'environement dans ce dossier avec la commande :
	Ex: C:\Users\NomUtilisateur>python -m venv NomDeMonDossier\venv *cela peut prendre quelques secondes à installer

-Une fois cela fait, nous allons rentrer dans notre environement avec la commande :
	Ex: C:\Users\NomUtilisateur>NomDeMonDossier\venv\Scripts\activate.bat

-Installons maintenant les packages, pour cela on place le fichier "requirements.txt" et "main.py" à l'intérieur de notre dossier.

-On rentre la commande suivante afin d'installer le tout :
	Ex: C:\Users\NomUtilisateur>pip install -r requirements.txt

-On rentre dans le dossier pour lancer le projet via la console:
	Ex: (venv) C:\Users\NomUtilisateur>cd NomDossier

-L'environement étant créée nous pouvons maintenant lancer le projet :
	Ex: (venv) C:\Users\NomUtilisateur\NomDossier>python main.py

-Le projet se lancera et le déroulement sera visible dans la console CMD