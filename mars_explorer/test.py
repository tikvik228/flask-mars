from requests import get, post

print(get('http://localhost:5000/api/jobs').json())
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
                 'is_finished': False}).json())  # некорректный запрос без collaborators