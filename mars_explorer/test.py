from requests import get, post, delete

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

print(1, get('http://localhost:5000/api/v2/users').json())
print(2, get('http://localhost:5000/api/v2/users/1').json())
print(3, get('http://localhost:5000/api/v2/users/52').json())
print(4, get('http://localhost:5000/api/v2/users/kk').json())
print(5, post('http://localhost:5000/api/v2/users', json={}).json())
print(6, post('http://localhost:5000/api/v2/users', json={'name': 'meee'}).json())
print(7, post('http://localhost:5000/api/v2/users', json={'name': 'meee', 'position':'prog',
                                                          'surname':'meme', 'age':12, 'address': 'module_2',
                                                          'speciality': 'science',
                                                          'hashed_password': 'meme228', 'email': 'pp@mars.org'}).json())
print(8, delete('http://localhost:5000/api/v2/users/2').json())

