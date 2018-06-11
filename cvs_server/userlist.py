def create_users(n):
    ls = []
    for i in range(0,n):
        ls.append(('test{0}'.format(i), 'test{0}password'.format(i)))
    return ls
