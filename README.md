Ce programme est un crawler qui permet de parcourir un lien et extracter des informations. <br />
Le programme est utilisable en ligne de commande et proposer les fonctionnalités suivantes :<br />
<br />
Retourner un rapport dans le terminal<br />
$ crawler [--url|u] https://example.net<br />
<br />
Retourner un rapport dans un fichier passé en paramètre<br />
$ crawler [--url|u] https://example.net [--export] nom_fichier<br />
<br />
Le rapport généré est au format texte et contient les informations suivantes :<br />
<br />
Le nombre d'URL unique<br />
Les URL's pointant sur le même domaine<br />
Les adresses pointant sur un domaine externe<br />
Les adresses contenant des formulaires (tout formulaire confondu)<br />
Les adresses contenant des pages protégés par mot de passe<br />
Le nombre d'adresse pointant sur le même nom de domaine renvoyant une page 404<br />
<br />
Le mode d'utilations est comme suit:<br />
<br />
Retourner uniquement les pages retournant un code erreur 404<br />
$ crawler [--url|u] https://example.net --404<br />
<br />
Retourner uniquement les adresses pointant vers un nom de domaine externe<br />
$ crawler [--url|u] https://example.net --external-url<br />
<br />
Retourner uniquement les pages nécessitant une authentification<br />
$ crawler [--url|u] https://example.net --protected_url<br /><br />
