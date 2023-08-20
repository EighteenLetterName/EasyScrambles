import random


def rotation_x(moves):
  movesmoves = []

  for i in moves:
    movesmoves.append(i)

  for i in range(len(movesmoves)):
    if movesmoves[i][0] == "U":
      if len(movesmoves[i]) == 2:
        movesmoves[i] = "B" + movesmoves[i][1]
      else:
        movesmoves[i] = "B"

    elif movesmoves[i][0] == "D":
      if len(movesmoves[i]) == 2:
        movesmoves[i] = "F" + movesmoves[i][1]
      else:
        movesmoves[i] = "F"

    elif movesmoves[i][0] == "F":
      if len(movesmoves[i]) == 2:
        movesmoves[i] = "U" + movesmoves[i][1]
      else:
        movesmoves[i] = "U"

    elif movesmoves[i][0] == "B":
      if len(movesmoves[i]) == 2:
        movesmoves[i] = "D" + movesmoves[i][1]
      else:
        movesmoves[i] = "D"

  return movesmoves


def rotation_x_prime(moves):
  movesmoves = []

  for i in moves:
    movesmoves.append(i)

  for i in range(len(movesmoves)):
    if movesmoves[i][0] == "U":
      if len(movesmoves[i]) == 2:
        movesmoves[i] = "F" + movesmoves[i][1]
      else:
        movesmoves[i] = "F"

    elif movesmoves[i][0] == "D":
      if len(movesmoves[i]) == 2:
        movesmoves[i] = "B" + movesmoves[i][1]
      else:
        movesmoves[i] = "B"

    elif movesmoves[i][0] == "F":
      if len(movesmoves[i]) == 2:
        movesmoves[i] = "D" + movesmoves[i][1]
      else:
        movesmoves[i] = "D"

    elif movesmoves[i][0] == "B":
      if len(movesmoves[i]) == 2:
        movesmoves[i] = "U" + movesmoves[i][1]
      else:
        movesmoves[i] = "U"

  return movesmoves


def rotation_x2(moves):
  movesmoves = []

  for i in moves:
    movesmoves.append(i)

  for i in range(len(movesmoves)):
    if movesmoves[i][0] == "U":
      if len(movesmoves[i]) == 2:
        movesmoves[i] = "D" + movesmoves[i][1]
      else:
        movesmoves[i] = "D"

    elif movesmoves[i][0] == "D":
      if len(movesmoves[i]) == 2:
        movesmoves[i] = "U" + movesmoves[i][1]
      else:
        movesmoves[i] = "U"

    elif movesmoves[i][0] == "F":
      if len(movesmoves[i]) == 2:
        movesmoves[i] = "B" + movesmoves[i][1]
      else:
        movesmoves[i] = "B"

    elif movesmoves[i][0] == "B":
      if len(movesmoves[i]) == 2:
        movesmoves[i] = "F" + movesmoves[i][1]
      else:
        movesmoves[i] = "F"

  return movesmoves


def rotation_y(moves):
  movesmoves = []

  for i in moves:
    movesmoves.append(i)

  for i in range(len(movesmoves)):
    if movesmoves[i][0] == "R":
      if len(movesmoves[i]) == 2:
        movesmoves[i] = "F" + movesmoves[i][1]
      else:
        movesmoves[i] = "F"

    elif movesmoves[i][0] == "L":
      if len(movesmoves[i]) == 2:
        movesmoves[i] = "B" + movesmoves[i][1]
      else:
        movesmoves[i] = "B"

    elif movesmoves[i][0] == "F":
      if len(movesmoves[i]) == 2:
        movesmoves[i] = "L" + movesmoves[i][1]
      else:
        movesmoves[i] = "L"

    elif movesmoves[i][0] == "B":
      if len(movesmoves[i]) == 2:
        movesmoves[i] = "R" + movesmoves[i][1]
      else:
        movesmoves[i] = "R"

  return movesmoves


def rotation_y_prime(moves):
  movesmoves = []

  for i in moves:
    movesmoves.append(i)

  for i in range(len(movesmoves)):
    if movesmoves[i][0] == "R":
      if len(movesmoves[i]) == 2:
        movesmoves[i] = "B" + movesmoves[i][1]
      else:
        movesmoves[i] = "B"

    elif movesmoves[i][0] == "L":
      if len(movesmoves[i]) == 2:
        movesmoves[i] = "F" + movesmoves[i][1]
      else:
        movesmoves[i] = "F"

    elif movesmoves[i][0] == "F":
      if len(movesmoves[i]) == 2:
        movesmoves[i] = "R" + movesmoves[i][1]
      else:
        movesmoves[i] = "R"

    elif movesmoves[i][0] == "B":
      if len(movesmoves[i]) == 2:
        movesmoves[i] = "L" + movesmoves[i][1]
      else:
        movesmoves[i] = "L"

  return movesmoves


def rotation_y2(moves):
  movesmoves = []

  for i in moves:
    movesmoves.append(i)

  for i in range(len(movesmoves)):
    if movesmoves[i][0] == "R":
      if len(movesmoves[i]) == 2:
        movesmoves[i] = "L" + movesmoves[i][1]
      else:
        movesmoves[i] = "L"

    elif movesmoves[i][0] == "L":
      if len(movesmoves[i]) == 2:
        movesmoves[i] = "R" + movesmoves[i][1]
      else:
        movesmoves[i] = "R"

    elif movesmoves[i][0] == "F":
      if len(movesmoves[i]) == 2:
        movesmoves[i] = "B" + movesmoves[i][1]
      else:
        movesmoves[i] = "B"

    elif movesmoves[i][0] == "B":
      if len(movesmoves[i]) == 2:
        movesmoves[i] = "F" + movesmoves[i][1]
      else:
        movesmoves[i] = "F"

  return movesmoves


def rotation_z(moves):
  movesmoves = []

  for i in moves:
    movesmoves.append(i)

  for i in range(len(movesmoves)):
    if movesmoves[i][0] == "R":
      if len(movesmoves[i]) == 2:
        movesmoves[i] = "U" + movesmoves[i][1]
      else:
        movesmoves[i] = "U"

    elif movesmoves[i][0] == "L":
      if len(movesmoves[i]) == 2:
        movesmoves[i] = "D" + movesmoves[i][1]
      else:
        movesmoves[i] = "D"

    elif movesmoves[i][0] == "U":
      if len(movesmoves[i]) == 2:
        movesmoves[i] = "L" + movesmoves[i][1]
      else:
        movesmoves[i] = "L"

    elif movesmoves[i][0] == "D":
      if len(movesmoves[i]) == 2:
        movesmoves[i] = "R" + movesmoves[i][1]
      else:
        movesmoves[i] = "R"

  return movesmoves


def rotation_z_prime(moves):
  movesmoves = []

  for i in moves:
    movesmoves.append(i)

  for i in range(len(movesmoves)):
    if movesmoves[i][0] == "R":
      if len(movesmoves[i]) == 2:
        movesmoves[i] = "D" + movesmoves[i][1]
      else:
        movesmoves[i] = "D"

    elif movesmoves[i][0] == "L":
      if len(movesmoves[i]) == 2:
        movesmoves[i] = "U" + movesmoves[i][1]
      else:
        movesmoves[i] = "U"

    elif movesmoves[i][0] == "U":
      if len(movesmoves[i]) == 2:
        movesmoves[i] = "R" + movesmoves[i][1]
      else:
        movesmoves[i] = "R"

    elif movesmoves[i][0] == "D":
      if len(movesmoves[i]) == 2:
        movesmoves[i] = "L" + movesmoves[i][1]
      else:
        movesmoves[i] = "L"

  return movesmoves


def rotation_z2(moves):
  movesmoves = []

  for i in moves:
    movesmoves.append(i)

  for i in range(len(movesmoves)):
    if movesmoves[i][0] == "R":
      if len(movesmoves[i]) == 2:
        movesmoves[i] = "L" + movesmoves[i][1]
      else:
        movesmoves[i] = "L"

    elif movesmoves[i][0] == "L":
      if len(movesmoves[i]) == 2:
        movesmoves[i] = "R" + movesmoves[i][1]
      else:
        movesmoves[i] = "R"

    elif movesmoves[i][0] == "U":
      if len(movesmoves[i]) == 2:
        movesmoves[i] = "D" + movesmoves[i][1]
      else:
        movesmoves[i] = "D"

    elif movesmoves[i][0] == "D":
      if len(movesmoves[i]) == 2:
        movesmoves[i] = "U" + movesmoves[i][1]
      else:
        movesmoves[i] = "U"

  return movesmoves


#####################################################


def random_y_rotation(moves):
  a = random.randint(1, 4)
  if a == 1:
    return rotation_y(moves)
  elif a == 2:
    return rotation_y_prime(moves)
  elif a == 3:
    return rotation_y2(moves)
  elif a == 4:
    return moves


def random_y_rotation_without_skip(moves):
  a = random.randint(1, 3)
  if a == 1:
    return rotation_y(moves)
  elif a == 2:
    return rotation_y_prime(moves)
  elif a == 3:
    return rotation_y2(moves)


def random_y_rotation_without_y(moves):
  a = random.randint(1, 3)
  if a == 1:
    return rotation_y_prime(moves)
  elif a == 2:
    return rotation_y2(moves)
  elif a == 3:
    return moves


def random_y_rotation_without_yprime(moves):
  a = random.randint(1, 3)
  if a == 1:
    return rotation_y(moves)
  elif a == 2:
    return rotation_y2(moves)
  elif a == 3:
    return moves


def random_y_rotation_without_y2(moves):
  a = random.randint(1, 3)
  if a == 1:
    return rotation_y(moves)
  elif a == 2:
    return rotation_y_prime(moves)
  elif a == 3:
    return moves


def random_y_rotation_without_skip_yprime(moves):
  a = random.randint(1, 2)
  if a == 1:
    return rotation_y(moves)
  elif a == 2:
    return rotation_y2(moves)


def random_y_rotation_without_skip_y(moves):
  a = random.randint(1, 2)
  if a == 1:
    return rotation_y_prime(moves)
  elif a == 2:
    return rotation_y2(moves)


def random_y_rotation_without_skip_y2(moves):
  a = random.randint(1, 2)
  if a == 1:
    return rotation_y(moves)
  elif a == 2:
    return rotation_y_prime(moves)


def random_y_rotation_without_y_yprime(moves):
  a = random.randint(1, 2)
  if a == 1:
    return rotation_y2(moves)
  elif a == 2:
    return moves


def random_y_rotation_without_y_y2(moves):
  a = random.randint(1, 2)
  if a == 1:
    return rotation_y_prime(moves)
  elif a == 2:
    return moves


def random_y_rotation_without_yprime_y2(moves):
  a = random.randint(1, 2)
  if a == 1:
    return rotation_y(moves)
  elif a == 2:
    return moves
