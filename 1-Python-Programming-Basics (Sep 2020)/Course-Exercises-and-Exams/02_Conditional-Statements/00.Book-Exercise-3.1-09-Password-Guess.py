# познай паролата
# Да се напише програма, която въвежда парола (произволен текст) и проверява дали въведеното съвпада с фразата "s3cr3t!P@ssw0rd".
# При съответствие да се изведе "Welcome", а при несъответствие да се изведе "Wrong password!"

password = input()

if password == 's3cr3t!P@ssw0rd':
    print('Welcome')
else:
    print('Wrong password!')