import requests




def create_refresh_link():
    params = {
        "refresh_token":'v3.r.130155215.54fa8ff6d22e69ce8c103c71266850983fe91b1a.0ffe34852f5c6ad9137da878318954226c065831',
        "client_id":'2100',
        "client_secret":'v3.r.130155215.06ddf3ef62c5c1a8df3d0d30e097411c2564d600.600bda4776c5f390978439b2518b6cc619f5965e'
    }

    endpoint = "https://api.superjob.ru/2.0/oauth2/refresh_token/"
    response = requests.get(endpoint, params=params)
    resjson = response.json()
    return resjson

print(create_refresh_link())

