from collections import Counter, defaultdict

users = [
        { "id": 0, "name": "Hero" },
        { "id": 1, "name": "Dunn" },
        { "id": 2, "name": "Sue" },
        { "id": 3, "name": "Chi" },
        { "id": 4, "name": "Thor" },
        { "id": 5, "name": "Clive" },
        { "id": 6, "name": "Hicks" },
        { "id": 7, "name": "Devin" },
        { "id": 8, "name": "Kate" },
        { "id": 9, "name": "Klein" }
]

friendships = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4),
               (4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)]


users_and_friends = map(lambda x: dict(id=x["id"], name=x["name"], friends=[]), users)

for friendship in friendships:
    i, j = friendship
    users_and_friends[i]["friends"].append(users_and_friends[j])
    users_and_friends[j]["friends"].append(users_and_friends[i])


def friendlen(user):
    return len(user["friends"])

#answers

total_connections = sum(friendlen(user) for user in users_and_friends)
total_peoples = len(users_and_friends)
avg_connections = total_connections / total_peoples
mapped_connections = map(lambda x: (x["id"], len(x["friends"])), users_and_friends)

print "Total Connections, {}".format(total_connections)
print "Total Peoples, {}".format(total_peoples)
print "Average Connectins, {}".format(avg_connections)
print "Mapped Connections, {}".format(sorted(mapped_connections, key=lambda x: x[1]))

# suggesting friends
def friends_of_friends(user):
    return [foaf["id"] for friend in user["friends"] for foaf in friend["friends"]]

def suggestion(user):
    lst = friends_of_friends(user)
    friends = [x["id"] for x in users_and_friends[user["id"]]["friends"]]
    result = Counter(lst) - Counter(friends)
    result.pop(user["id"], None)
    return result

print "Suggested Friend for 3 is, {}".format(suggestion(users_and_friends[3]))


## Data once again
interests = [
        (0, "Hadoop"), (0, "Big Data"), (0, "HBase"), (0, "Java"),
        (0, "Spark"), (0, "Storm"), (0, "Cassandra"),
        (1, "NoSQL"), (1, "MongoDB"), (1, "Cassandra"), (1, "HBase"),
        (1, "Postgres"), (2, "Python"), (2, "scikit-learn"), (2, "scipy"),
        (2, "numpy"), (2, "statsmodels"), (2, "pandas"), (3, "R"), (3, "Python"),
        (3, "statistics"), (3, "regression"), (3, "probability"),
        (4, "machine learning"), (4, "regression"), (4, "decision trees"),
        (4, "libsvm"), (5, "Python"), (5, "R"), (5, "Java"), (5, "C++"),
        (5, "Haskell"), (5, "programming languages"), (6, "statistics"),
        (6, "probability"), (6, "mathematics"), (6, "theory"),
        (7, "machine learning"), (7, "scikit-learn"), (7, "Mahout"),
        (7, "neural networks"), (8, "neural networks"), (8, "deep learning"),
        (8, "Big Data"), (8, "artificial intelligence"), (9, "Hadoop"),
        (9, "Java"), (9, "MapReduce"), (9, "Big Data")
]

user_by_interests = defaultdict(list)
interest_by_user = defaultdict(list)


for user, interest in interests:
    user_by_interests[interest].append(user)
    interest_by_user[user].append(interest)

def most_common_interests_with(user):
     return Counter(interested_user_id
                    for interest in interest_by_user[user["id"]]
                    for interested_user_id in user_by_interests[interest]
                    if interested_user_id != user["id"])

# Answers for most_common interest
print "Most Common interest : {}".format(most_common_interests_with(users_and_friends[3]))


salaries_and_tenures = [(83000, 8.7), (88000, 8.1),
                            (48000, 0.7), (76000, 6),
                            (69000, 6.5), (76000, 7.5),
                            (60000, 2.5), (83000, 10),
                            (48000, 1.9), (63000, 4.2)]


def group_tenure(gp):
    sal, tenure = gp
    if tenure <= 2:
        return "genin", sal
    if 2 < tenure <= 5:
        return "chunin", sal
    if 5 < tenure:
        return "jounin", sal

mapped_bucked = map(group_tenure, salaries_and_tenures)

grouped_bucket = defaultdict(list)

for key, value in mapped_bucked:
    grouped_bucket[key].append(value)

grouped_dict = { tenure: sum(values)/len(values)
                      for tenure, values in grouped_bucket.items() }

print grouped_dict

paid = 1,
unpaid = 0

paying_data = [(0.7, paid),(1.9, unpaid),
    (2.5, paid),
    (4.2, unpaid),
    (6, unpaid),
    (6.5, unpaid),
    (7.5, unpaid),
    (8.1, unpaid),
    (8.7, paid),
    (10,  paid)
]


"""
Question:

Accordingly,
if you wanted to create a model though this is definitely not
enough data to base a model on you might try to predict paid for users with
very few and very many years of experience
and unpaid for users with middling amounts of experience

"""

def group_paid(data):
    yeard, status = data
    if yeard <= 3:
        return "paid"
    elif 3< yeard <= 10:
        return "unpaid"
    return "paid"

group_payee = map(group_paid, paying_data)

#answer
print group_payee


interests = [
        (0, "Hadoop"), (0, "Big Data"), (0, "HBase"), (0, "Java"),
        (0, "Spark"), (0, "Storm"), (0, "Cassandra"),
        (1, "NoSQL"), (1, "MongoDB"), (1, "Cassandra"), (1, "HBase"),
        (1, "Postgres"), (2, "Python"), (2, "scikit-learn"), (2, "scipy"),
        (2, "numpy"), (2, "statsmodels"), (2, "pandas"), (3, "R"), (3, "Python"),
        (3, "statistics"), (3, "regression"), (3, "probability"),
        (4, "machine learning"), (4, "regression"), (4, "decision trees"),
        (4, "libsvm"), (5, "Python"), (5, "R"), (5, "Java"), (5, "C++"),
        (5, "Haskell"), (5, "programming languages"), (6, "statistics"),
        (6, "probability"), (6, "mathematics"), (6, "theory"),
        (7, "machine learning"), (7, "scikit-learn"), (7, "Mahout"),
        (7, "neural networks"), (8, "neural networks"), (8, "deep learning"),
        (8, "Big Data"), (8, "artificial intelligence"), (9, "Hadoop"),
        (9, "Java"), (9, "MapReduce"), (9, "Big Data")
]


"""
Question

As you re wrapping up your first day,
the VP of Content Strategy asks you for data about what topics users are most interested in,
so that she can plan out her blog calendar accordingly.
You already have the raw data from the friend-suggester project:
"""

print Counter(map(lambda x: x[1], interests))
