import requests
import time
import json
import json







def getinfo(keyword,town,i):


                    # newid=newid
                    params = {
                    "sort_new": time.time(),
                    "keyword":f"{keyword}",
                    "town":f'{town}'
                    }
                    headers={
                    'X-Api-App-Id': "v3.r.130155215.a338c216d6fb51385312670e906c0b708b7c3e2b.3be37d75e69e47c96e6e44000d613035b9d07b00",
                    'Authorization': "Bearer r.130155215.06ddf3ef62c5c1a8df3d0d30e097411c2564d600.600bda4776c5f390978439b2518b6cc619f5965e"
                     }
                    endpoint = "https://api.superjob.ru/2.0/vacancies/"
                    response = requests.get(endpoint, headers=headers, params=params).json()
                    resjson_form = json.dumps(response, ensure_ascii=False, indent=2)
                    pyform = json.loads(resjson_form)
                    newvacancy=pyform['objects'][i]
                    newid=newvacancy['id']

                    profession = newvacancy['profession']
                    link = newvacancy['link']
                    payment = f"{newvacancy['payment_from']} - {newvacancy['payment_to']}"
                    if newvacancy['payment_from'] == 0 and newvacancy['payment_to'] == 0:
                         payment = "после собеседования"
                    elif newvacancy['payment_from'] != 0 and newvacancy['payment_to'] == 0:
                         payment = newvacancy['payment_from']
                    elif newvacancy['payment_from'] != 0 and newvacancy['payment_to'] == 0:
                         payment = newvacancy['payment_to']
                    company = newvacancy['firm_name']

                    return f"💼Вакансия: {profession} \n 🏙Компания:{company} \n 💲Условия оплаты: {payment} \n 🔜Оставить заявку и узнать подробне о вакансии:\n {link} "

                    # return compareid(newvacancy,oldid,newid,keyword,town)

def compareid(newvacancy, oldid, newid,keyword,town):
    while True:
        time.sleep(10)
        if oldid != newid:
            oldid=newid
            return doprint(newvacancy,keyword,town,oldid, newid)
        elif oldid ==newid:
            return(getinfo(keyword,town,oldid,newid))




def doprint(newvacancy,keyword,town,oldid,newid):

                     profession=newvacancy['profession']
                     payment=f"{newvacancy['payment_from']} - {newvacancy['payment_to']}"
                     if newvacancy['payment_from'] == 0 and newvacancy['payment_to'] == 0 :
                        payment="после собеседования"
                     elif newvacancy['payment_from'] != 0 and newvacancy['payment_to'] == 0 :
                        payment = newvacancy['payment_from']
                     elif newvacancy['payment_from'] != 0 and newvacancy['payment_to'] == 0 :
                        payment = newvacancy['payment_to']
                        company=newvacancy['firm_name']
                        link=newvacancy['link']
                        print(f"💼Вакансия: {profession} \n 🏙Компания:{company} \n 💲Условия оплаты: {payment} \n 🔜Оставить заявку и узнать подробне о вакансии:\n {link} ")
                        return getinfo(keyword,town,oldid,newid)
i=0
while True:
    print(getinfo('стажер','москва',i))
    time.sleep(1)
    print('sled vac')
    u=input()
    if u !='нет':
        i+=1



















