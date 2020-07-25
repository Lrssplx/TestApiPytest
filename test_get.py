import requests 

def test_status_and_data():

    headers = {

        'Accept': '*/*',
        'User-Agent': 'requests',
    }


    url = "http://dummy.restapiexample.com/api/v1/employees"

    reposta = requests.get(url, headers=headers)
    resposta_dict = reposta.json()

 


    status = resposta_dict['status']
    tamanholist = len(resposta_dict['data'])
    assert status == 'success' and tamanholist > 0
 


    

    

 