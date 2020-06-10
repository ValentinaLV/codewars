from operator import attrgetter


class User:
    def __init__(self, user_id, last_name, first_name):
        self.user_id = user_id
        self.last_name = last_name
        self.first_name = first_name

    def __repr__(self):
        return f'User {self.user_id} {self.last_name} {self.first_name}'


users = [User(23, 'Test', 'Test'), User(33, 'Test2', 'Test2'), User(15, 'Test3', 'Test3')]

users_sort = sorted(users, key=lambda user: user.user_id)
print(users_sort)

users_sort_by_id = sorted(users, key=attrgetter('user_id'))
users_sort_by_name = sorted(users, key=attrgetter('last_name', 'first_name'))
print(users_sort_by_id)
print(users_sort_by_name)

max_user_id = max(users, key=attrgetter('user_id'))
min_user_id = min(users, key=attrgetter('user_id'))
print(max_user_id)
print(min_user_id)
