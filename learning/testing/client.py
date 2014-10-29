__author__ = 'arobres'
# -*- coding: utf-8 -*-


from commons.rest_utils import Rest_Utils

def main():

    finish = False
    print ('Welcome to the learning machine')
    #username = input('Introduce username: ')
    #password = input('Introduce password: ')

    username = 'qa'
    password = 'qa'

    rest_utils = Rest_Utils(username=username, password=password)
    response = rest_utils.get_user(user_id=username)
    assert response.ok, 'User not exists'

    print 'Enjoy!'

    while True:

        response = rest_utils.get_question_play()
        assert response.ok
        response = response.json()
        question_id = response['id']
        answer = input('Question: {}\n Answer: '.format(response['question'].encode('utf-8')))
        if answer == 'exit':
            break

        answer_body = {'id': question_id, 'answer': answer}
        response = rest_utils.send_answer(body=answer_body)
        assert response.ok
        print response.content

if __name__ == '__main__':
    main()