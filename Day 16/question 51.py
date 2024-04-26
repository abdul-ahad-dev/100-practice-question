"""
Extract username from a given email.
    Eg if the email is abdulahad24@gmail.com
    then the username should be abdulahad24
"""


def extract_username(mail):

    user_name = ''

    for i in mail:

        if i != '@':
            user_name = user_name + i
        else:
            break

    return user_name


def main():

    email = 'abdulahad24@gmail.com'

    print(email)

    user = extract_username(email)

    print("user name is: ",end='')

    print(user)


if __name__ == "__main__":

    main()
