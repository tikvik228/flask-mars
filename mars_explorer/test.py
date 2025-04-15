from requests import get, post, delete, put

'''print(get('http://localhost:5000/api/jobs').json())
print(get('http://localhost:5000/api/jobs/1').json())
print(get('http://localhost:5000/api/jobs/2').json())
print(get('http://localhost:5000/api/jobs/228').json())
print(get('http://localhost:5000/api/jobs/aefgaw').json())
print(post('http://localhost:5000/api/jobs/',
           json={'job': 'tesst',
                 'teamleader': 1,
                 'work_size': 6,
                 'collaborators':'2, 3',
                 'is_finished': False}).json())  # корректный запрос
print(post('http://localhost:5000/api/jobs/', json={}).json())  # пустой запрос
print(post('http://localhost:5000/api/jobs/',
           json={'job': 'tesst',
                 'teamleader': 1,
                 'work_size': 6,
                 'is_finished': False}).json())  # некорректный запрос без collaborators'''

'''print(get('http://localhost:5000/api/jobs').json())
print(put('http://localhost:5000/api/jobs/1',
          json={'job': 'change_tesst',
                'teamleader': 1,
                'work_size': 8,
                'is_finished': False}).json())  # OK
print(put('http://localhost:5000/api/jobs/999', json={'job': 'new_work'}).json())  # not found
print(put('http://localhost:5000/api/jobs/mrmtyem', json={'job': 'new_work'}).json())  # invalid id
print(put('http://localhost:5000/api/jobs/1', json={}).json())  # empty request
print(get('http://localhost:5000/api/jobs').json())'''

print(get('http://localhost:5000/api/users').json())
print(get('http://localhost:5000/api/users/1').json())
print(get('http://localhost:5000/api/users/228').json())  # not found
print(get('http://localhost:5000/api/users/aefgaw').json())  # invalid id

print(post('http://localhost:5000/api/users/',
           json={'surname': 'just_new_user',
                 'name': 'no_name_user',
                 'age': 23,
                 'position': 'definitely not captain',
                 'speciality': 'hobo',
                 'address': 'streets of Revachol',
                 'email': 'RodeoInMySoul@mars.org',
                 'hashed_password': 'secret_password777'}).json())  # корректный запрос
print(post('http://localhost:5000/api/users/',
           json={'surname': 'just_new_user',
                 'name': 'no_name_user',
                 'age': 23,
                 'position': 'definitely not captain',
                 'speciality': 'hobo',
                 'address': 'streets of Revachol',
                 'email': 'RodeoInMySoul@mars.org',
                 'hashed_password': 'secret_password777'}).json())  # error: email already exist
print(post('http://localhost:5000/api/users/', json={}).json())  # пустой запрос
print(post('http://localhost:5000/api/users/',
           json={'surname': 'incorrect_test',
                 'name': 'error_name',
                 'age': 34,
                 'address': '--'}).json())  # некорректный запрос с неполными данными

print(get('http://localhost:5000/api/users').json())

print(put('http://localhost:5000/api/users/2',
          json={'name': 'changed_no_name_user',
                'age': 25,
                'hashed_password': 'changed_secret_password777'}).json())  # OK
print(put('http://localhost:5000/api/users/999', json={'name': 'new_name'}).json())  # not found
print(put('http://localhost:5000/api/users/mrmtyem', json={'name': 'new_name'}).json())  # invalid id
print(put('http://localhost:5000/api/users/1', json={}).json())  # empty request

print(get('http://localhost:5000/api/users').json())

print(delete('http://localhost:5000/api/users/999').json())
print(delete('http://localhost:5000/api/users/2').json())

print(get('http://localhost:5000/api/users').json())

'''print(1, get('http://localhost:5000/api/v2/users').json())
print(2, get('http://localhost:5000/api/v2/users/1').json())
print(3, get('http://localhost:5000/api/v2/users/52').json())
print(4, get('http://localhost:5000/api/v2/users/kk').json())
print(5, post('http://localhost:5000/api/v2/users', json={}).json())
print(6, post('http://localhost:5000/api/v2/users', json={'name': 'meee'}).json())
print(7, post('http://localhost:5000/api/v2/users', json={'name': 'meee', 'position':'prog',
                                                          'surname':'meme', 'age':12, 'address': 'module_2',
                                                          'speciality': 'science',
                                                          'hashed_password': 'meme228', 'email': 'pp@mars.org'}).json())
print(8, delete('http://localhost:5000/api/v2/users/2').json())'''

