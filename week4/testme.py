import string
import random

def inputChar():
    char = 0
    #string.ascii_letters #'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    char = random.choice(string.ascii_letters + string.punctuation + ' ')
    #print(char)
    return char

def inputString():
  letters = 'r' + 'e' + 's' + 't' + '\0' + 'a' + 'b' + 'c' + 'd' + 'e'
  randString = ''.join([random.choice(letters) for n in range(6)])
  #randString = ''.join([random.choice(string.ascii_lowercase + '\0') for n in range(6)])
  #print(randString)
  return randString


def testme():
  tcCount = 0
  s = 0
  c = 0
  state = 0
  while (1):
    tcCount+=1
    c = inputChar()
    s = inputString()
    #outPut = "Iteration" + tcCount +", c"+ c + ", s" + s + ", state" + state
    print('Iteration {}, c {}, s {}, state {}'.format(tcCount, c, s, state))
    if (c == '[' and state == 0):
      state = 1
    if (c == '(' and state == 1):
      state = 2
    if (c == '{' and state == 2):
      state = 3
    if (c == ' 'and state == 3):
      state = 4
    if (c == 'a' and state == 4):
      state = 5
    if (c == 'x' and state == 5):
      state = 6
    if (c == '}' and state == 6):
      state = 7
    if (c == ')' and state == 7):
      state = 8
    if (c == ']' and state == 8):
      state = 9
    if (s[0] == 'r' and s[1] == 'e' and s[2] == 's' and s[3] == 'e'
       and s[4] == 't' and s[5] == '\0' and state == 9):
          print("error ")
          exit(200)

def main():
  testme()


if __name__ == "__main__":
  testme()