# qr_code_api
api de generation de qr code unique avec des fonctionnalité comme l'inscription, l'ouverture de registre d'utilisation des qr code par les utilisateurs avec django rest framework.
Les qr code peuvent être gravé au laser sur des porte-clés ou autre

Création d'un lot de qr_code par l'administrateur : https://qrcodeapi.pythonanywhere.com/api/qr_code/create/

Inscription d'un utilisateur : https://qrcodeapi.pythonanywhere.com/api/dj-rest-auth/registration/

Informations sur un utilisateur : https://qrcodeapi.pythonanywhere.com/api/dj-rest-auth/user/

Informations sur les utilisateurs et le qr code qui leur est associé (possibilité de filtré) : https://qrcodeapi.pythonanywhere.com/api/userinfo/list/

liste de tous les utilisateurs : https://qrcodeapi.pythonanywhere.com/api/user/list

liste des qr_code créent (possibilité de filtré) : https://qrcodeapi.pythonanywhere.com/api/qr_code/list/

Récupération les details d'un seul qr code avec son id : https://qrcodeapi.pythonanywhere.com/api/qr_code/detail/1/

Ouvertur d'un registre : https://qrcodeapi.pythonanywhere.com/api/registre/create/

Modification d'un registre connaissant l'id : https://qrcodeapi.pythonanywhere.com/api/registre/update/1/
