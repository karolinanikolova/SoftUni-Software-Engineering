# 5.	Electron Distribution
# You are a mad scientist and you decided to play with electron distribution among atom's shells. ' \
#         'You know that basic idea of electron distribution is that electrons should fill a shell until it's holding the maximum number of electrons.
# The rules for electron distribution are as follows:
# •	Maximum number of electrons in a shell is distributed with a rule of 2n^2 (n being position of a shell a.k.a. the list index + 1).
# •	For example, maximum number of electrons in 3rd shield is 2*3^2 = 18.
# •	Electrons should fill the lowest level shell first.
# •	If the electrons have completely filled the lowest level shell, the other unoccupied electrons will fill the higher level shell and so on.

electrons = int(input())

electrons_distribution = []

shell_position = 1

while electrons > 0:
    max_electrons_in_shell = 2 * shell_position ** 2
    if electrons > max_electrons_in_shell:
        electrons_distribution.append(max_electrons_in_shell)
    else:
        electrons_distribution.append(electrons)
    electrons -= max_electrons_in_shell
    shell_position += 1

print(electrons_distribution)
