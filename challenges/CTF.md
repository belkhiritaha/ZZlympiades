# CTF

## Epreuves

### Getting started
Une chaîne de caractères en base64 est fournie. Il suffit de la décoder pour obtenir le flag et quelques règles essentielles pour le reste des épreuves.

10 points

No hints


### Miam
Une page web en cours de dev nous est fournie. Il faut deviner le bon paramètre GET, ainsi que la bonne valeur pour obtenir le flag.

70 points

Hint1: J'ai l'impression que "miam" est beaucoup trop utilisé sur cette page.


### Login
Un formulaire de login est fourni. En explorant le code source, on trouve en commentaire une liste de 10 usernames et 10 mots de passe. Il suffit de tester les combinaisons jusqu'à trouver la bonne.

100 points

No hints


### Message
Une plateforme qui permet d'envoyer des messages à un admin est fournie. Il faut trouver un moyen de récupérer les cookies de l'admin. (Stored XSS)
150 points

Le code source est fourni.

Hint1: Cross-site scripting? drôle de nom lol...

Hint2: Comment pourrais-je récupérer les cookies de l'admin ?


### Upload

Une page web permettant d'uploader des images est fournie. Ce site utilise une bibliothèque vulnérable. Il faut trouver cette vulnérabilité, et réussir à l'exploiter pour récupérer le flag. (CVE-2018-16509)

200 points

Le code source + Dockerfile sont fournis.

Hint1: Hmmm... il est intéressant ce Dockerfile...

Hint2: Y'a t-il des CVEs sur ghostscript ? :O

Hint3: CVE-2018-16509


### BONUS

50 points

En activant tous les hints du challenge Getting Started, on reçoit le flag du challenge bonus, comme quoi, prendre des indices des fois c'est pas si mal :)



## Général

Les épreuves sont hébérgées sur la plateforme CTFd. 

Un flag est de la forme `IsiLabs{F4K3_FL4G_F0R_T3ST1NG}`.

L'utilisation des indices coûte (je sais plus trop combien de) points par indice. Les ZZ1 ont droit à plus d'assistance du staff.
