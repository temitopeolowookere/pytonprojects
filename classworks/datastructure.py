users = [
    {'name': 'hadizq',
     'age': 21,
     'gender': 'Female',
     'username': 'deezah',
     'is verified': True,
     'tweets': [{'content': 'PO for president', 'likes': 450, 'retweets': 233},
                {'content': 'Atiku', 'likes': 4, 'retweets': 2},
                ]
     },

    {'name': 'ibrahim',
     'age': 32,
     'gender': 'Male',
     'username': 'ibro',
     'is verified': False,
     'tweets': [{'content': 'Programming is fun', 'likes': 34, 'retweets': 12},
                {'content': 'Atiku', 'likes': 4, 'retweets': 2},
                ]
     },

    {'name': 'james',
     'age': 25,
     'gender': 'male',
     'username': 'jam',
     'is verified': True,
     'tweets': [{'content': 'i love her', 'likes': 40, 'retweets': 20},
                {'content': 'Atiku', 'likes': 4, 'retweets': 2},
                ]
     },
    {'name': 'racheal',
     'age': 21,
     'gender': 'Female',
     'username': 'betty',
     'is verified': False,
     'tweets': [{'content': '.', 'likes': 450, 'retweets': 233},
                {'content': 'thinking about ameez', 'likes': 4, 'retweets': 2},
                ]
     }, {'name': 'elijah',
         'age': 18,
         'gender': 'male',
         'username': 'el_d_si',
         'is verified': True,
         'tweets': [{'content': 'osun decides', 'likes': 450, 'retweets': 233},
                    {'content': 'Atiku', 'likes': 4, 'retweets': 2},
                    ]
         },

    {'name': 'dorris',
     'age': 16,
     'gender': 'Female',
     'username': 'anything',
     'is verified': False,
     'tweets': [{'content': 'i love chimamanda ', 'likes': 450, 'retweets': 233},
                {'content': 'feminism is the goal', 'likes': 4, 'retweets': 2},
                ]
     },
    {'name': 'jacob',
     'age': 37,
     'gender': 'male',
     'username': 'elder',
     'is verified': True,
     'tweets': [{'content': 'reflection is my goal', 'likes': 450, 'retweets': 233},
                {'content': 'how to get more like on twitter', 'likes': 1, 'retweets': 1},
                ]
     },

    {'name': 'derrick',
     'age': 21,
     'gender': 'male',
     'username': 'standbygen',
     'is verified': True,
     'tweets': []

     }

]

no_of_users = len(users)
usernames = {user ['username'] for user in users}
female_users = [user['name'] for user in users if user['gender']== 'Female']
print(usernames)

inactive_users = [user for user in users if len(user['tweets']) == 0]
print(female_users)

name_and_age = [{'name': user['name'], 'age': user['age']} for user in users]
avg_age_of_users = sum(user['age']for user in users) / len(users)
print(inactive_users)
print(name_and_age)
print(avg_age_of_users)