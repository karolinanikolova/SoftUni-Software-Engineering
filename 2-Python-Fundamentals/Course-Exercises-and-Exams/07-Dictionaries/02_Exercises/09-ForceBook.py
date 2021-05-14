# 9.	*ForceBook
# The force users are struggling to remember which side are the different forceUsers from, because they switch them too often.
# So you are tasked to create a web application to manage their profiles. You should store an information
# for every unique forceUser, registered in the application.
# You will receive several input lines in one of the following formats:
# {forceSide} | {forceUser}
# {forceUser} -> {forceSide}
# The forceUser and forceSide are strings, containing any character.
# If you receive forceSide | forceUser, you should check if such forceUser already exists,
# and if not, add him/her to the corresponding side.
# If you receive a forceUser -> forceSide, you should check if there is such a forceUser already and if so, change his/her side.
# If there is no such forceUser, add him/her to the corresponding forceSide, treating the command as a new registered forceUser.
# Then you should print on the console: "{forceUser} joins the {forceSide} side!"
# You should end your program when you receive the command "Lumpawaroo". At that point you should print each force side,
# ordered descending by forceUsers count, than ordered by name. For each side print the forceUsers, ordered by name.
# In case there are no forceUsers in a side, you shouldn`t print the side information.

data = input()

force_book = {"Light": [], "Lighter": [], "Dark": [], "Darker": []}

while not data == "Lumpawaroo":
    if " | " in data:
        force_side, force_user = data.split(" | ")

        for value_list in force_book.values():
            if force_user not in value_list:
                force_book[force_side].append(force_user)

    if " -> " in data:
        force_user, force_side = data.split(" -> ")

        for value_list in force_book.values():
            if force_user not in value_list:
                force_book[force_side].append(force_user)
            else:
                value_list.remove(force_user)
                force_book[force_side].append(force_user)
                print(f"{force_user} joins the {force_side} side!")
                break

    data = input()

print(force_book)
# for force_user, force_side in force_book.items():
