from pypodio2 import api

podio_client_id = 'e'   #write the client id
podio_client_secret = ''   #write the client secret
podio_login_id = ''   #write the username
podio_login_pw = ''   #write the password
podio = api.OAuthClient(podio_client_id, podio_client_secret, podio_login_id, podio_login_pw)

