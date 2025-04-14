from flask import Flask, request, jsonify
import logging
import json
import random

app = Flask(__name__)

logging.basicConfig(level=logging.INFO)

# создаем словарь, в котором ключ — название города,
# а значение — массив, где перечислены id картинок,
# которые мы записали в прошлом пункте.

cities = {
    'москва': ['997614/a05245fa2118b5bd99b4',
               '997614/fb923d90ecc729fc95a8'],
    'нью-йорк': ['997614/11374bc307eaaa0447d0',
                 '997614/7d97c4a6606f44255812'],
    'париж': ["13200873/f844d391d2ba42ef234d",
              '1030494/be81af63e1bf8a1351c9']
}

sessionStorage = {}


@app.route('/post', methods=['POST'])
def main():
    logging.info(f'Request: {request.json!r}')
    response = {
        'session': request.json['session'],
        'version': request.json['version'],
        'response': {
            'end_session': False
        }
    }
    handle_dialog(response, request.json)
    logging.info(f'Response: {response!r}')
    return jsonify(response)


def handle_dialog(res, req):
    user_id = req['session']['user_id']
    if req['session']['new']:
        res['response']['text'] = 'Привет, назови свое имя!'
        sessionStorage[user_id] = {
            'first_name': None,
            'game_started': False
        }
        return
    if sessionStorage[user_id]['first_name'] is None:
        first_name = get_first_name(req)
        if first_name is None:
            res['response']['text'] = 'Не расслышала имя! Пожалуйста повтори!'
        else:
            sessionStorage[user_id]['first_name'] = first_name
            sessionStorage[user_id]['guessed_cities'] = []
            res['response']['text'] = f'Приятно познакомиться, {first_name.title()}. Угадаешь ли ты город по фото?'
            res['response']['buttons'] = [
                {
                    'title': 'Да',
                    'hide':  True
                 },
                {
                    'title': 'Нет',
                    'hide': True
                }
            ]
    else:
        if not sessionStorage[user_id]['game_started']:
            if 'да' in req['request']['nlu']['tokens']:
                if len(sessionStorage[user_id]['guessed_cities']) == 3:
                    res['response']['text'] = 'Ты отгадал все города'
                    res['response']['end_session'] = True
                else:
                    sessionStorage[user_id]['game_started'] = True
                    sessionStorage[user_id]['attempt'] = 1
                    play_game(res, req)
            elif 'нет' in req['request']['nlu']['tokens']:
                res['response']['text'] = 'Ну и ладно'
                res['response']['end_session'] = True
            elif req['request']['original_utterance'].lower() == "помощь":
                res['response']['text'] = 'Это текст помощи, посылаю тебе лучи поддержки.'
            else:
                res['response']['text'] = 'Я ничего не поняла. Так да или нет?'
                res['response']['buttons'] = [
                    {
                        'title': 'Да',
                        'hide': True
                    },
                    {
                        'title': 'Нет',
                        'hide': True
                    },
                    {
                        'title': 'Помощь',
                        'hide': True
                    }
                ]
        else:
            play_game(res, req)


def get_city(req):
    # перебираем именованные сущности
    for entity in req['request']['nlu']['entities']:
        # если тип YANDEX.GEO то пытаемся получить город(city),
        # если нет, то возвращаем None
        if entity['type'] == 'YANDEX.GEO':
            # возвращаем None, если не нашли сущности с типом YANDEX.GEO
            return entity['value'].get('city', None)


def get_first_name(req):
    # перебираем сущности
    for entity in req['request']['nlu']['entities']:
        # находим сущность с типом 'YANDEX.FIO'
        if entity['type'] == 'YANDEX.FIO':
            # Если есть сущность с ключом 'first_name',
            # то возвращаем ее значение.
            # Во всех остальных случаях возвращаем None.
            return entity['value'].get('first_name', None)


def play_game(res, req):
    user_id = req['session']['user_id']
    attempt = sessionStorage[user_id]['attempt']
    if attempt == 1:
        city = random.choice(list(cities))
        while city in sessionStorage[user_id]['guessed_cities']:
            city = random.choice(list(cities))
        sessionStorage[user_id]['city'] = city
        res['response']['card'] = {}
        res['response']['card']['type'] = 'BigImage'
        res['response']['card']['title'] = 'Какой это город?'
        res['response']['card']['image_id'] = cities[city][0]
        res['response']['text'] = 'Начинаем игру'
    else:
        city = sessionStorage[user_id]['city']
        if get_city(req) == city:
            res['response']['text'] = 'Правильно! Давай еще раз.'
            sessionStorage[user_id]['game_started'] = False
            sessionStorage[user_id]['guessed_cities'] = city
            return
        else:
            if attempt == 3:
                res['response']['text'] = f'Вы пытались. Это город {city.title()}. Давай сыграем снова.'
                sessionStorage[user_id]['game_started'] = False
                sessionStorage[user_id]['guessed_cities'] = city
            else:
                res['response']['card'] = {}
                res['response']['card']['type'] = 'BigImage'
                res['response']['card']['title'] = 'Попробуй еще раз, посмотри внимательней....'
                res['response']['card']['image_id'] = cities[city][0]
                res['response']['text'] = 'Не угадал.'
    sessionStorage[user_id]['attempt'] += 1


if __name__ == '__main__':
    app.run()
