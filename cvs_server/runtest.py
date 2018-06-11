import userlist
import requests
from time import sleep
from random import randint

def get_json_or_error_new(link, uname, upwd):
    sleep(0.05)
    try:
        res = requests.get(link, auth=(uname, upwd))
        if res.status_code != 200:
            print("ERROR: Cannot get {0} : {1}, id = {2}, pwd = {3}".format(link, res.status_code    , uname, upwd))
            exit(1)
        resjson = res.json()
        return resjson
    except Exception:
        print("ERROR: Cannot get {0}".format(link))
        exit(1)

def get_json_or_error(link):
    sleep(0.05)
    try:
        res = requests.get(link).json()
        return res
    except Exception:
        print('ERROR: Cannot get {0}'.format(link))
        exit(1)

def get_id(users_json, uname):
    for user_json in users_json:
        if user_json['username'] == uname:
            return user_json['id']
    print('Cannot find user {0}!'.format(uname))

def find_userinfo(users, q_uid):
    for (uname, upwd, uid, utoken) in users:
        if uid == q_uid :
            return (uname, upwd, utoken)
    print('Cannot find user with id {0}'.format(q_uid))
    exit(1)

def post_or_error(link, data, token):
    sleep(0.05)
    try:
        headers={'Authorization':'Token '+token}
        if not token:
            res = requests.post(link, data=data)
        else:
            res = requests.post(link, data=data, headers=headers)
        if res.status_code not in [201, 200] :
            print('ERROR: Cannot post {0}: {1}, token={2}'.format(link, res.status_code, token))
            print('ERROR: with Payload {0} data={1}'.format(res.json(), data))
            exit(1)
        return res.json()
    except Exception:
        print('ERROR: Cannot post {0}'.format(link))
        exit(1)

def put_or_error(link, data, token):
    sleep(0.05)
    try:
        headers={'Authorization':'Token '+token}
        res = requests.put(link, data=data, headers=headers)
        if res.status_code not in [201,200]:
            print('ERROR: Cannot put {0}: {1}, token = {2}'.format(link, res.status_code, token))
            exit(1)
    except Exception:
        print('ERROR: Cannot put {0}'.format(link))
        exit(1)

def delete_or_error(link, token):
    sleep(0.05)
    try:
        headers={'Authorization':'Token '+token}
        res = requests.delete(link, headers=headers)
        if res.status_code not in [201, 200, 204]:
            print('ERROR: Cannot delete {0}: {1}, token = {2}'.format(link, res.status_code, token))
            exit(1)
    except Exception:
        print('ERROR: Cannot delete {0}'.format(link))
        exit(1)



userN = 10
user_pairs = userlist.create_users(userN)
url = 'http://127.0.0.1:8000/'
users = []
print('1. Getting users list.')
for (uname, upwd) in user_pairs:
    user_json = post_or_error(url+'login/', {'username':uname, 'password':upwd}, '')
    users.append((uname, upwd, user_json['id'], user_json['token']))
print(users)

print('****************************************************************************************')

print('2. Checking GET '+url+'products/')
prods = get_json_or_error(url+'products/')
prodN = prods['count']
print(prods)

print('****************************************************************************************')
commentN = 10
contents = ['delicious!', 'So bad :(', 'So so... ^^', 'What a best!', 'Advertisement', 
    'So Sick!', 'Fantastic!', 'Good! :)', 'Ha ha', 'Hello, sir!']
ratings = []
for i in range(0,commentN):
    ratings.append(randint(1,5))
comts = []

print('3. Checkig POST '+url+'comments/ by creating {0} comments'.format(commentN))
for i in range(0,commentN):
    user = users[randint(0, len(users)-1)][2]
    product_id = randint(1,prodN)
    data_for_store = {'content':contents[i], 'rating':ratings[i], 'product':product_id, 'user_id':user}
    comts.append(data_for_store)
    data = {'content':contents[i], 'rating':ratings[i], 'product':product_id}
    (pname, ppwd, ptoken) = find_userinfo(users, user)
    print('\tPosting with user: {0}'.format((pname,ppwd)))
    post_or_error(url+'comments/', data, ptoken)

comts_json = get_json_or_error(url+'comments/')
print(comts)
print(comts_json)

for comt in comts:
    found = False
    for comt_json in comts_json:
        if comt_json['user_id']['id'] == comt['user_id'] and comt_json['product']['id'] == comt['product'] and comt_json['rating'] == comt['rating'] and comt_json['content'] == comt['content']:
            found = True
            break
    if not found:
        print('ERROR: Not found : {0}'.format(comt))
        exit(1)


print('****************************************************************************************')

put_data = [
    {'content': 'first put', 'rating': 1},
    {'content': 'second put', 'rating': 2},
    {'content': 'third put', 'rating': 3},
    {'content': 'fourth put', 'rating': 4},
    {'content': 'fifth put', 'rating': 5},
]
put_cnt = 0
delete_ids = []
print('4. Checking PUT '+url+'comments/id/')

for comt_json in comts_json:
    if put_cnt == 5 :
        break
    comt_id = comt_json['id']
    user_id = comt_json['user_id']['id']
    (uname, upwd, utoken) = find_userinfo(users, user_id)
    print('\tPutting with user : {0}'.format((uname, upwd)))
    put_or_error(url+'comments/'+str(comt_id)+'/', put_data[put_cnt], utoken)
    put_cnt = put_cnt + 1

comts_json = get_json_or_error(url+'comments/')
for da in put_data:
    found = False
    for comt_json in comts_json:
        if comt_json['rating'] == da['rating'] and comt_json['content'] == da['content']:
            delete_ids.append((comt_json['id'], comt_json['user_id']['id']))
            found = True
            break
    if not found:
        print('ERROR: Not found : {0}'.format(comt))
        exit(1)


print('****************************************************************************************')

print('5. Checking DELETE '+url+'comments/id/')

for (d_id, u_id) in delete_ids:
    (uname, upwd, utoken) = find_userinfo(users, u_id)
    print('\tDeleting commet {0}'.format(d_id))
    delete_or_error(url+'comments/'+str(d_id)+'/', utoken)

print('****************************************************************************************')

reviewN = 10
reviews = ['first', 'second', 'third', 'fourth', 'fifth', 
    'sixth', 'seventh', '8th', '9th', '10th']
ratings = []
for i in range(0,reviewN):
    ratings.append(randint(1,5))
revs = []

print('6. Checking POST '+url+'reviews/')

for i in range(0,reviewN):
    user = users[randint(0, len(users)-1)][2]
    product_id = randint(1,prodN)
    data_for_store = {'title':reviews[i], 'rating':ratings[i], 'product':product_id, 'user_id':user}
    revs.append(data_for_store)
    data = {'title':reviews[i], 'rating':ratings[i], 'product':product_id}
    (pname, ppwd, ptoken) = find_userinfo(users, user)
    print('\tPosting with user: {0}'.format((pname,ppwd)))
    post_or_error(url+'reviews/', data, ptoken)

revs_json = get_json_or_error(url+'reviews/')
print(revs)
print(revs_json)

for rev in revs:
    found = False
    for rev_json in revs_json:
        if rev_json['user_id']['id'] == rev['user_id'] and rev_json['product']['id'] == rev['product'] and rev_json['rating'] == rev['rating'] and rev_json['title'] == rev['title']:
            found = True
            break
    if not found:
        print('ERROR: Not found : {0}'.format(rev))
        exit(1)


print('****************************************************************************************')

print('7. Checking PUT '+url+'reviews/id/')

put_data = [
    {'title': 'first put', 'rating': 1},
    {'title': 'second put', 'rating': 2},
    {'title': 'third put', 'rating': 3},
    {'title': 'fourth put', 'rating': 4},
    {'title': 'fifth put', 'rating': 5},
]
put_cnt = 0
delete_ids = []
for rev_json in revs_json:
    if put_cnt == 5 :
        break
    rev_id = rev_json['id']
    user_id = rev_json['user_id']['id']
    (uname, upwd, utoken) = find_userinfo(users, user_id)
    print('\tPutting with user : {0}'.format((uname, upwd)))
    put_or_error(url+'reviews/'+str(rev_id)+'/', put_data[put_cnt], utoken)
    put_cnt = put_cnt + 1

revs_json = get_json_or_error(url+'reviews/')
for da in put_data:
    found = False
    for rev_json in revs_json:
        if rev_json['rating'] == da['rating'] and rev_json['title'] == da['title']:
            delete_ids.append((rev_json['id'],rev_json['user_id']['id']))
            found = True
            break
    if not found:
        print('ERROR: Not found : {0}'.format(da))
        exit(1)


print('****************************************************************************************')

print('8. Checking DELETE '+url+'reviews/id/')

for (d_id, u_id) in delete_ids:
    (uname, upwd, utoken) = find_userinfo(users, u_id)
    print('\tDeleting review {0}'.format(d_id))
    delete_or_error(url+'reviews/'+str(d_id)+'/', utoken)

print('****************************************************************************************')

recipeN = 10
titles = ['first', 'second', 'third', 'fourth', 'fifth', 
    'sixth', 'seventh', '8th', '9th', '10th']
ingreds = [
    [1,4,5,2],
    [2,3],
    [31,2],
    [11],
    [12,5],
    [1],
    [7,32],
    [13,33],
    [2,1],
    [10,3]
]
recs = []

print('9. Checking POST '+url+'recipes/')

for i in range(0,recipeN):
    user = users[randint(0, len(users)-1)][2]
    data_for_store = {'title':titles[i], 'ingredients':ingreds[i], 'user_id':user}
    recs.append(data_for_store)
    data = {'title':titles[i], 'ingredients':ingreds[i]}
    (pname, ppwd, ptoken) = find_userinfo(users, user)
    print('\tPosting with user: {0}'.format((pname,ppwd)))
    post_or_error(url+'recipes/', data, ptoken)

recs_json = get_json_or_error(url+'recipes/')
print(recs)
print(recs_json)

for rec in recs:
    found = False
    for rec_json in recs_json:
        if rec_json['user_id']['id'] == rec['user_id'] and rec_json['title'] == rec['title']:
            found = True
            break
    if not found:
        print('ERROR: Not found : {0}'.format(rec))
        exit(1)


print('****************************************************************************************')

print('10. Checking PUT '+url+'recipes/id/')

put_data = [
    {'title': 'first put', 'ingredients': [1]},
    {'title': 'second put', 'ingredients': [2]},
    {'title': 'third put', 'ingredients': [3]},
    {'title': 'fourth put', 'ingredients': [4]},
    {'title': 'fifth put', 'ingredients': [5]},
]
put_cnt = 0

delete_ids=[]

for rec_json in recs_json:
    if put_cnt == 5 :
        break
    rec_id = rec_json['id']
    user_id = rec_json['user_id']['id']
    (uname, upwd, utoken) = find_userinfo(users, user_id)
    print('\tPutting with user : {0}'.format((uname, upwd)))
    put_or_error(url+'recipes/'+str(rec_id)+'/', put_data[put_cnt], utoken)
    put_cnt = put_cnt + 1

recs_json = get_json_or_error(url+'recipes/')
for da in put_data:
    found = False
    for rec_json in recs_json:
        if rec_json['title'] == da['title']:
            delete_ids.append((rec_json['id'], rec_json['user_id']['id']))
            found = True
            break
    if not found:
        print('ERROR: Not found : {0}'.format(da))
        exit(1)


print('****************************************************************************************')

print('11. Checking DELETE '+url+'recipes/id/')

for (d_id, u_id) in delete_ids:
    (uname, upwd, utoken) = find_userinfo(users, u_id)
    print('\tDeleting recipe {0}'.format(d_id))
    delete_or_error(url+'recipes/'+str(d_id)+'/', utoken)

print('****************************************************************************************')
'''
print('12. Checking GET '+url+'posts/')

print('****************************************************************************************')

print('13. Checking DELETE '+url+'posts/id/')

print('****************************************************************************************')
'''
print('TEST SUCCESSFUL!')
