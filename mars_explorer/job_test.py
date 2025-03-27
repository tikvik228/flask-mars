from requests import get, post, delete


print(1, get('http://localhost:5000/api/v2/jobs').json())
print(2, get('http://localhost:5000/api/v2/jobs/1').json())
print(3, get('http://localhost:5000/api/v2/jobs/52').json())
print(4, get('http://localhost:5000/api/v2/jobs/kk').json())
print(5, post('http://localhost:5000/api/v2/jobs', json={}).json())
print(6, post('http://localhost:5000/api/v2/jobs', json={'teamleader': 1}).json())
print(7, post('http://localhost:5000/api/v2/jobs', json={'teamleader': 2, 'job': 'eat sand',
                                                             'work_size': 18, 'collaborators': '1, 2',
                                                             'is_finished': False}).json())
print(8, delete('http://localhost:5000/api/v2/jobs/5').json())