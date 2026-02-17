# 1. Différences entre HTTP et HTTPS

## 1.1 HTTP

*Hypertext Transfer Protocol*
    - Protocole non sécurisé sur un réseau où tout le monde peut voir le contenu.
    - URL : http://

## 1.2 HTTPS

*Hypertext Transfer Protocol Secure*
    - Protocole sécurisé, HTTP + TLS (SSL) pour chiffrer requêtes/réponses HTTP.
    - URL : https://

## 1.3 Comparaison des connexions HTTP et HTTPS

+-----------+--------+----------------------+--------------------------------+
| Protocole | Acteur | Type de connexion    | Description                    |
+-----------+--------+----------------------+--------------------------------+
| http://   | User   | Insecure Connection  | Normal HTTP                    |
| https://  | User   | Encrypted Connection | Secure HTTPS (SSL Certificate) |
+-----------+--------+----------------------+--------------------------------+

# 2. Structure HTTP requête et réponse

```
(Requête : Client -> Server)
GET /hello.txt HTTP/1.1 (méthode - chemin - version)
User-Agent : curl/7.63.0 libcurl/7.63.0 OpenSSL/1.1.l zlib/1.2.11
Host : www.example.com
Accept-Language : en
```

```
(Réponse : Serveur -> Client)
HTTP/1.1 200 OK (version - chemin - méthode)
Date : Wed, 30 Jan 2019 12:14:39 GMT
Server : Apache
Last-Modified : Mon, 28 Jan 2019 11:17:01 GMT
Accept-Ranges : bytes
Content-Length : 12
Vary : Accept-Encoding
Content-Type : text/plain
```

# 3. Fonctionnement du protocole HTTP/HTTPS

## 3.1 Méthodes

GET : Récupère une ressource.
POST : Envoie des données au serveur.
PUT : Met à jour une ressource entière.
DELETE : Supprime une ressource donnée.

## 3.2 Codes de status

+----------------+---------------------------+------------------------------------+
| Status code    | Nom                       | Description                        |
+----------------+---------------------------+------------------------------------+
| 200            | OK                        | Succès.                            |
| 201            | Created                   | Création d'une nouvelle ressource. |
| 301            | Moved Permanently         | Redirigé vers HTTPS.               |
| 400            | Bad Request               | Requête invalide.                  |
| 404            | Not Found                 | Ressource introuvable.             |
| 500            | Internal Server Error     | Erreur sur le serveur.             |
+----------------+---------------------------+------------------------------------+
