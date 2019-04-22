from flask import Flask, request
import logging
import json
import random

app = Flask(__name__)

logging.basicConfig(level=logging.INFO)

a = 0
narod = 10
chin = 10
cash = 0
day = 1
end = 0
win = 1
task = []

ends = {
    1: '965417/ab0a9f4eee5f8bba1b01',
    2: '1540737/115a97c58d76aa7991fe',
    3: '1652229/87124d040a501b472c16'
}

days = [['Сын прокурора может сесть в тюрьму. За его освобождение вам хотят дать взятку в размере 50000 дублей. Возьмете ли вы деньги?', ['Да', 'Нет'], [[-1, 2, 500000], [1, -7, 0]]]]
sessionStorage = {}


@app.route('/post', methods=['POST'])
def main():
    logging.info('Request: %r', request.json)
    response = {
        'session': request.json['session'],
        'version': request.json['version'],
        'response': {
            'end_session': False
        }
    }
    handle_dialog(response, request.json)
    logging.info('Response: %r', response)
    return json.dumps(response)



def handle_dialog(res, req):
    global a, end, narod, chin, cash, day, win, task
    user_id = req['session']['user_id']

    if req['session']['new']:
        a = 0
        narod = 10
        chin = 10
        cash = 0
        day = 1
        end = 0
        win = 1
        task = []
        res['response']['text'] = 'Привет! Назови свое имя!'
        sessionStorage[user_id] = {
            'first_name': None
        }
        return

    if sessionStorage[user_id]['first_name'] is None:
        first_name = get_first_name(req)
        if first_name is None:
            res['response']['text'] = \
                'Не расслышала имя. Повтори, пожалуйста!'
        else:
            sessionStorage[user_id]['first_name'] = first_name
            res['response'][
                'text'] = 'Приятно познакомиться, ' + first_name.title() \
                          + '. Я - Алиса. Давай сыграем в игру!'
            res['response']['buttons'] = [
                {
                    'title': 'Давай',
                    'hide': True
                }
            ]
    else:
        if a == 0:
            res['response']['text'] = 'Вы - президент Фоссии, которую уже давно терроризируют продажные чиновники. Настал последний месяц вашего последнего срока на посту, и вы очень хотите бежать из страны. Ваша задача - заработать 1000000 дублей на билеты из Фоссии. Для этого вы 30 дней принимаете по решению, которое влияет на один из 2 параметров: отношение народа и отношение чиновников. Однако вас казнят если один из параметров превысит 20 или упадет ниже 0. Вы готовы?'
            res['response']['buttons'] = [
                {
                    'title': 'Да',
                    'hide': True
                }
            ]
            a = 1
        else:
            if narod < 0 or chin < 0 or narod > 20 or chin > 20:
                win = 0
            if win:
                if day <= 2:
                    if not end:
                        task = random.choice(days)
                        end = 1
                        res['response']['text'] = 'День {}: '.format(day) + task[0] + ' (Ваши показатели сейчас: {}, {}, {})'.format(narod, chin, cash)
                        res['response']['buttons'] = [
                        {
                            'title': qqq,
                            'hide': True
                        } for qqq in task[1]
                        ]
                    else:
                        end = 0
                        day += 1
                        if req['request']['command'] == task[1][0]:
                            sp = task[2][0]
                        else:
                            sp = task[2][1]
                        narod += sp[0]
                        chin += sp[1]
                        cash += sp[2]
                        res['response']['text'] = 'Теперь ваши показатели такие: отношение народа: {}, отношение чиновников: {}, деньги: {}'.format(narod, chin, cash)
                        res['response']['buttons'] = [
                        {
                            'title': 'Новый день',
                            'hide': True
                        }
                ]
                else:
                    if cash >= 1000000:
                        res['response']['card'] = {}
                        res['response']['card']['type'] = 'BigImage'
                        res['response']['card']['image_id'] = ends[3]
                        res['response']['card']['title'] = 'Вы выиграли, и смогли бежать в Геликобританию, чтобы начать там новую жизнь. Игра окончена.'
                        res['response']['text'] = 'Игра окончена.'
                        res['response']['end_session'] = True
                    else:
                        res['response']['card'] = {}
                        res['response']['card']['type'] = 'BigImage'
                        res['response']['card']['image_id'] = ends[2]
                        res['response']['card']['title'] = 'К сожалению, вы не смогли накопить денег, и вы будете жить в нищете до конца своих дней. Игра окончена.'
                        res['response']['text'] = 'Игра окончена.'
                        res['response']['end_session'] = True
            else:
                res['response']['card'] = {}
                res['response']['card']['type'] = 'BigImage'
                res['response']['card']['image_id'] = ends[1]
                res['response']['card']['title'] = 'В стране произошли массовые беспорядки, и вас осудили на 30 лет за коррупционые схемы. Игра окончена.'
                res['response']['text'] = 'Игра окончена.'
                res['response']['end_session'] = True



def get_first_name(req):
    for entity in req['request']['nlu']['entities']:
        if entity['type'] == 'YANDEX.FIO':
            return entity['value'].get('first_name', None)


if __name__ == '__main__':
    app.run()