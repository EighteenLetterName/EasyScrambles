# Creator: github.com/EighteenLetterName
#
# Discord: @EighteenLetterName
#
# Telegram: t.me/EighteenLetterName
#
# VK: vk.com/EighteenLetterName

from cubeofrubik import RubiksCube
import random
import oll
import f2l
import cross
import rotation

#####################################################

#####################################################


def reverse(moves):
  moves.reverse()
  for i in range(len(moves)):
    if len(moves[i]) == 1:
      moves[i] += "'"
    else:
      if moves[i][1] == "'":
        moves[i] = moves[i][0]

  return moves


def reverse_new(moves):
  moves.reverse()
  for i in range(len(moves)):
    if len(moves[i]) == 1:
      moves[i] += "′"
    else:
      if moves[i][1] == "′":
        moves[i] = moves[i][0]

  return moves


#####################################################


def auf():
  return random.choice(["U", "U'", "U2", " "])


#####################################################


def scramble_generator():

  scramble = []

  scramble.append(auf())

  oll_alg = reverse(random.choice(oll.oll))
  for i in range(len(oll_alg)):
    scramble.append(oll_alg[i])

  scramble.append(auf())

  #####################################################

  pare1 = reverse(random.choice(f2l.f2l))
  pare1pos = []
  for i in pare1:
    pare1pos.append(i)
  pare1 = rotation.random_y_rotation(pare1)
  for i in range(len(pare1)):
    scramble.append(pare1[i])

  scramble.append(auf())

  if pare1 == pare1pos:

    pare2 = reverse(random.choice(f2l.f2l))
    pare2pos = []
    for i in pare2:
      pare2pos.append(i)

    pare2 = rotation.random_y_rotation_without_skip(pare2)
    for i in range(len(pare2)):
      scramble.append(pare2[i])

    scramble.append(auf())

    if pare2 == rotation.rotation_y(pare2pos):

      pare3 = reverse(random.choice(f2l.f2l))
      pare3pos = []
      for i in pare3:
        pare3pos.append(i)
      pare3 = rotation.random_y_rotation_without_skip_y(pare3)
      for i in range(len(pare3)):
        scramble.append(pare3[i])

      scramble.append(auf())

      if pare3 == rotation.rotation_y_prime(pare3pos):

        pare4 = reverse(random.choice(f2l.f2l))
        pare4pos = []
        for i in pare4:
          pare4pos.append(i)
        pare4 = rotation.rotation_y2(pare4)
        for i in range(len(pare4)):
          scramble.append(pare4[i])

        scramble.append(auf())
      else:

        pare4 = reverse(random.choice(f2l.f2l))
        pare4pos = []
        for i in pare4:
          pare4pos.append(i)
        pare4 = rotation.rotation_y_prime(pare4)
        for i in range(len(pare4)):
          scramble.append(pare4[i])

        scramble.append(auf())

    elif pare2 == rotation.rotation_y_prime(pare2pos):

      pare3 = reverse(random.choice(f2l.f2l))
      pare3pos = []
      for i in pare3:
        pare3pos.append(i)
      pare3 = rotation.random_y_rotation_without_skip_yprime(pare3)
      for i in range(len(pare3)):
        scramble.append(pare3[i])

      scramble.append(auf())

      if pare3 == rotation.rotation_y(pare3pos):

        pare4 = reverse(random.choice(f2l.f2l))
        pare4pos = []
        for i in pare4:
          pare4pos.append(i)
        pare4 = rotation.rotation_y2(pare4)
        for i in range(len(pare4)):
          scramble.append(pare4[i])

        scramble.append(auf())
      else:

        pare4 = reverse(random.choice(f2l.f2l))
        pare4pos = []
        for i in pare4:
          pare4pos.append(i)
        pare4 = rotation.rotation_y(pare4)
        for i in range(len(pare4)):
          scramble.append(pare4[i])

        scramble.append(auf())

    elif pare2 == rotation.rotation_y2(pare2pos):

      pare3 = reverse(random.choice(f2l.f2l))
      pare3pos = []
      for i in pare3:
        pare3pos.append(i)
      pare3 = rotation.random_y_rotation_without_skip_y2(pare3)
      for i in range(len(pare3)):
        scramble.append(pare3[i])

      scramble.append(auf())

      if pare3 == rotation.rotation_y(pare3pos):

        pare4 = reverse(random.choice(f2l.f2l))
        pare4pos = []
        for i in pare4:
          pare4pos.append(i)
        pare4 = rotation.rotation_y_prime(pare4)
        for i in range(len(pare4)):
          scramble.append(pare4[i])

        scramble.append(auf())
      else:

        pare4 = reverse(random.choice(f2l.f2l))
        pare4pos = []
        for i in pare4:
          pare4pos.append(i)
        pare4 = rotation.rotation_y(pare4)
        for i in range(len(pare4)):
          scramble.append(pare4[i])

        scramble.append(auf())

  elif pare1 == rotation.rotation_y(pare1pos):

    pare2 = reverse(random.choice(f2l.f2l))
    pare2pos = []
    for i in pare2:
      pare2pos.append(i)
    pare2 = rotation.random_y_rotation_without_y(pare2)
    for i in range(len(pare2)):
      scramble.append(pare2[i])

    scramble.append(auf())

    if pare2 == pare2pos:

      pare3 = reverse(random.choice(f2l.f2l))
      pare3pos = []
      for i in pare3:
        pare3pos.append(i)
      pare3 = rotation.random_y_rotation_without_skip_y(pare3)
      for i in range(len(pare3)):
        scramble.append(pare3[i])

      scramble.append(auf())
      ############
      if pare3 == rotation.rotation_y_prime(pare3pos):

        pare4 = reverse(random.choice(f2l.f2l))
        pare4pos = []
        for i in pare4:
          pare4pos.append(i)
        pare4 = rotation.rotation_y2(pare4)
        for i in range(len(pare4)):
          scramble.append(pare4[i])

        scramble.append(auf())
      else:

        pare4 = reverse(random.choice(f2l.f2l))
        pare4pos = []
        for i in pare4:
          pare4pos.append(i)
        pare4 = rotation.rotation_y_prime(pare4)
        for i in range(len(pare4)):
          scramble.append(pare4[i])

        scramble.append(auf())

    elif pare2 == rotation.rotation_y_prime(pare2pos):

      pare3 = reverse(random.choice(f2l.f2l))
      pare3pos = []
      for i in pare3:
        pare3pos.append(i)
      pare3 = rotation.random_y_rotation_without_y_yprime(pare3)
      for i in range(len(pare3)):
        scramble.append(pare3[i])

      scramble.append(auf())

      if pare3 == pare3pos:

        pare4 = reverse(random.choice(f2l.f2l))
        pare4pos = []
        for i in pare4:
          pare4pos.append(i)
        pare4 = rotation.rotation_y2(pare4)
        for i in range(len(pare4)):
          scramble.append(pare4[i])

        scramble.append(auf())
      else:

        pare4 = reverse(random.choice(f2l.f2l))
        for i in range(len(pare4)):
          scramble.append(pare4[i])

        scramble.append(auf())

    elif pare2 == rotation.rotation_y2(pare2pos):

      pare3 = reverse(random.choice(f2l.f2l))
      pare3pos = []
      for i in pare3:
        pare3pos.append(i)
      pare3 = rotation.random_y_rotation_without_y_y2(pare3)
      for i in range(len(pare3)):
        scramble.append(pare3[i])

      scramble.append(auf())
      ############
      if pare3 == pare3pos:

        pare4 = reverse(random.choice(f2l.f2l))
        pare4pos = []
        for i in pare4:
          pare4pos.append(i)
        pare4 = rotation.rotation_y_prime(pare4)
        for i in range(len(pare4)):
          scramble.append(pare4[i])

        scramble.append(auf())
      else:

        pare4 = reverse(random.choice(f2l.f2l))
        for i in range(len(pare4)):
          scramble.append(pare4[i])

        scramble.append(auf())

  elif pare1 == rotation.rotation_y_prime(pare1pos):

    pare2 = reverse(random.choice(f2l.f2l))
    pare2pos = []
    for i in pare2:
      pare2pos.append(i)
    pare2 = rotation.random_y_rotation_without_yprime(pare2)
    for i in range(len(pare2)):
      scramble.append(pare2[i])

    scramble.append(auf())

    if pare2 == pare2pos:

      pare3 = reverse(random.choice(f2l.f2l))
      pare3pos = []
      for i in pare3:
        pare3pos.append(i)
      pare3 = rotation.random_y_rotation_without_skip_yprime(pare3)
      for i in range(len(pare3)):
        scramble.append(pare3[i])

      scramble.append(auf())

      if pare3 == rotation.rotation_y(pare3pos):

        pare4 = reverse(random.choice(f2l.f2l))
        pare4pos = []
        for i in pare4:
          pare4pos.append(i)
        pare4 = rotation.rotation_y2(pare4)
        for i in range(len(pare4)):
          scramble.append(pare4[i])

        scramble.append(auf())
      else:

        pare4 = reverse(random.choice(f2l.f2l))
        pare4pos = []
        for i in pare4:
          pare4pos.append(i)
        pare4 = rotation.rotation_y(pare4)
        for i in range(len(pare4)):
          scramble.append(pare4[i])

        scramble.append(auf())

    elif pare2 == rotation.rotation_y(pare2pos):

      pare3 = reverse(random.choice(f2l.f2l))
      pare3pos = []
      for i in pare3:
        pare3pos.append(i)
      pare3 = rotation.random_y_rotation_without_y_yprime(pare3)
      for i in range(len(pare3)):
        scramble.append(pare3[i])

      scramble.append(auf())

      if pare3 == pare3pos:

        pare4 = reverse(random.choice(f2l.f2l))
        pare4pos = []
        for i in pare4:
          pare4pos.append(i)
        pare4 = rotation.rotation_y2(pare4)
        for i in range(len(pare4)):
          scramble.append(pare4[i])

        scramble.append(auf())
      else:

        pare4 = reverse(random.choice(f2l.f2l))
        for i in range(len(pare4)):
          scramble.append(pare4[i])

        scramble.append(auf())

    elif pare2 == rotation.rotation_y2(pare2pos):

      pare3 = reverse(random.choice(f2l.f2l))
      pare3pos = []
      for i in pare3:
        pare3pos.append(i)
      pare3 = rotation.random_y_rotation_without_yprime_y2(pare3)
      for i in range(len(pare3)):
        scramble.append(pare3[i])

      scramble.append(auf())

      if pare3 == pare3pos:

        pare4 = reverse(random.choice(f2l.f2l))
        pare4pos = []
        for i in pare4:
          pare4pos.append(i)
        pare4 = rotation.rotation_y(pare4)
        for i in range(len(pare4)):
          scramble.append(pare4[i])

        scramble.append(auf())
      else:

        pare4 = reverse(random.choice(f2l.f2l))
        for i in range(len(pare4)):
          scramble.append(pare4[i])

        scramble.append(auf())

  elif pare1 == rotation.rotation_y2(pare1pos):

    pare2 = reverse(random.choice(f2l.f2l))
    pare2pos = []
    for i in pare2:
      pare2pos.append(i)
    pare2 = rotation.random_y_rotation_without_y2(pare2)
    for i in range(len(pare2)):
      scramble.append(pare2[i])

    scramble.append(auf())

    if pare2 == rotation.rotation_y(pare2pos):

      pare3 = reverse(random.choice(f2l.f2l))
      pare3pos = []
      for i in pare3:
        pare3pos.append(i)
      pare3 = rotation.random_y_rotation_without_y_y2(pare3)
      for i in range(len(pare3)):
        scramble.append(pare3[i])

      scramble.append(auf())
      ############
      if pare3 == pare3pos:

        pare4 = reverse(random.choice(f2l.f2l))
        pare4pos = []
        for i in pare4:
          pare4pos.append(i)
        pare4 = rotation.rotation_y_prime(pare4)
        for i in range(len(pare4)):
          scramble.append(pare4[i])

        scramble.append(auf())
      else:

        pare4 = reverse(random.choice(f2l.f2l))
        for i in range(len(pare4)):
          scramble.append(pare4[i])

        scramble.append(auf())

    elif pare2 == pare2pos:

      pare3 = reverse(random.choice(f2l.f2l))
      pare3pos = []
      for i in pare3:
        pare3pos.append(i)
      pare3 = rotation.random_y_rotation_without_skip_y2(pare3)
      for i in range(len(pare3)):
        scramble.append(pare3[i])

      scramble.append(auf())

      if pare3 == rotation.rotation_y(pare3pos):

        pare4 = reverse(random.choice(f2l.f2l))
        pare4pos = []
        for i in pare4:
          pare4pos.append(i)
        pare4 = rotation.rotation_y_prime(pare4)
        for i in range(len(pare4)):
          scramble.append(pare4[i])

        scramble.append(auf())
      else:

        pare4 = reverse(random.choice(f2l.f2l))
        pare4pos = []
        for i in pare4:
          pare4pos.append(i)
        pare4 = rotation.rotation_y(pare4)
        for i in range(len(pare4)):
          scramble.append(pare4[i])

        scramble.append(auf())

    elif pare2 == rotation.rotation_y_prime(pare2pos):

      pare3 = reverse(random.choice(f2l.f2l))
      pare3pos = []
      for i in pare3:
        pare3pos.append(i)
      pare3 = rotation.random_y_rotation_without_yprime_y2(pare3)
      for i in range(len(pare3)):
        scramble.append(pare3[i])

      scramble.append(auf())

      if pare3 == pare3pos:

        pare4 = reverse(random.choice(f2l.f2l))
        pare4pos = []
        for i in pare4:
          pare4pos.append(i)
        pare4 = rotation.rotation_y(pare4)
        for i in range(len(pare4)):
          scramble.append(pare4[i])

        scramble.append(auf())
      else:

        pare4 = reverse(random.choice(f2l.f2l))
        for i in range(len(pare4)):
          scramble.append(pare4[i])

        scramble.append(auf())

  crosss = rotation.random_y_rotation(random.choice(cross.cross))
  for i in range(len(crosss)):
    scramble.append(crosss[i])

  for i in scramble:
    if i == ' ':
      scramble.remove(i)

  scramble = rotation.rotation_z2(scramble)

  general_scramble = ""
  for i in scramble:
    general_scramble += i

  while "'" in general_scramble:
    general_scramble = general_scramble.replace("'", "′")

  cube = RubiksCube()
  cube.move(general_scramble)
  scramble = cube.solve()

  output = []

  for i in range(len(scramble) - 1):
    if (scramble[i] != "′"
        and scramble[i] != "2") and (scramble[i + 1] != "′"
                                     and scramble[i + 1] != "2"):
      output.append(scramble[i])
    elif (scramble[i] != "′"
          and scramble[i] != "2") and (scramble[i + 1] == "′"
                                       or scramble[i + 1] == "2"):
      output.append(scramble[i] + scramble[i + 1])
  if scramble[-1] != "′" and scramble[-1] != "2":
    output.append(scramble[-1])
  output = reverse_new(output)

  return '  '.join(output)


print(scramble_generator())
