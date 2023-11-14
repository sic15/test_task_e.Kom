import requests

url = "http://127.0.0.1:5000/get_form"

test_data = [{
    "name": "CheckForm 100",
    "call_result": "answer",
    "phone_number": "+7 111 111 11 11"
    },
    {
        "name": "CheckForm 101",
        "call_result": "a@ya.ru",
        "phone_number": "+7 111 111 11 11"
    },
    {
        "name": "CheckForm 102",
        "result": "Некий текст",
        "phone_number": "+7 111 111 11 11"
    },
    {
        "name": "CheckForm 103",
        "call_result": "a@ya.ru",
        "phone_number": "+7 111 111 11 11",
        "spare_number": "+123",
        "messgae": "Hi!"
    },
    {
        "name": "CheckForm 104",
        "email": "s@p.ru",
        "response date": "23.11.1990"
    },
    {
        "name": "CheckForm 105",
        "order_date": "2020-02-02",
        "order_number": "text",
        "additional_field": "23"},
    {
        "name": "CheckForm 106"
    },
    {
        "name": "CheckForm 107",
        "wrong_field": "want work"}
]

for item in range(len(test_data)):
    print(f'Тест № {item + 1}')
    response = requests.post(url, json=test_data[item])
    result = response.json()
    if res := result.get('template_name'):
        print(f'{res} подходящая форма')
    else:
        print(response.json())
    print()
