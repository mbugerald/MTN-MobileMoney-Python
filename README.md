mbugeraldjunior@gmail.com

docker run -d -e VIRTUAL_HOST=ui.bap.freidojo.net \
              -e LETSENCRYPT_HOST=ui.bap.freidojo.net  \
              -e LETSENCRYPT_EMAIL=james.regis@gmail.com \
              --network=webproxy \
              --name my_app \
              httpd:alpine


docker run -d -e VIRTUAL_HOST=api.bap.freidojo.net \
              -e LETSENCRYPT_HOST=api.bap.freidojo.net  \
              -e LETSENCRYPT_EMAIL=james.regis@gmail.com \
              --network=webproxy \
              --name my_api \
              bap_api