from cvs_rest.models import CustomUser
import userlist

print('--------- Clear Users --------------')

for i in range(0,10):
    username = 'test{0}'.format(i)
    try:
        user = CustomUser.objects.get(username = username)
        user.delete()
        print('\tDeleted user {0}'.format(username))
    except CustomUser.DoesNotExist:
        continue

print('--------- Creating Users -----------')

for (username, pwd) in userlist.create_users(10):
    user = CustomUser.objects.create_user(username=username, password=pwd, email='test@test.com')
    user.save()
    print('\tCreated user {0}'.format(username))

print('Intialization Successful!')
