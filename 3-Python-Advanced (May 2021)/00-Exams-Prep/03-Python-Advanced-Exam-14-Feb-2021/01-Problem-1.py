# Problem 1
# First, you will be given a sequence of integers representing firework effects. Afterwards you will be given another
# sequence of integers representing explosive power.
# You need to start from the first firework effect and try to mix it with the last explosive power.
# If the sum of their values is:
# •	divisible by 3, but it is not divisible by 5 – create Palm firework and remove both materials
# •	divisible by 5, but it is not divisible by 3 – create Willow firework and remove both materials
# •	divisible by both 3 and 5 – create Crossette firework and remove both materials
# Otherwise, decrease the value of the firework effect by 1 and move it at the end of the sequence.
# Then, try to mix the same explosive power with the next firework effect.
# If any value is equal to or below 0, you should remove it from the sequence before trying to mix it with the other.
# When you have successfully prepared enough fireworks for the show or you have no more firework punches or explosive
# power, you need to stop mixing.
# To make the perfect firework show, Maria needs 3 of each of the firework types.
