""" error handing is used to create exception, there are differnt ways of handling exception, we use Try, except, else,
 finally. """

# challenge
""" We have got some buggy code, using what we have we have learnt, catch the error
 and make it to print 'Fruit = Pie' regardless of the error"""

fruits = eval(input())


# def make_pie(index):
#     try:
#         fruit = fruits[index]
#         print(fruit)
#     except IndexError:
#         print ("Fruit pie")
#     else:
#         print(fruit + "pie")
#
# print(make_pie(4))

"""Error handling for dictionary"""

facebook_post = eval(input())

total_likes = 0
for post in facebook_post:
    try:
        total_likes += post['likes']
    except KeyError:
        pass
print(total_likes)


""" i will be going to day 29 to make some changes on our password manager game. see you there"""




