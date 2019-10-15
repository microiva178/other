#!/usr/bin/env python3
import time
import subprocess
import random
from threading import Timer
score=0

#startlogo

subprocess.call(['clear'])
time.sleep(1)
print('       __                       __                    ')
time.sleep(0.3)
print('     /                      | /                       ')
time.sleep(0.3)
print('    (___  ___  ___  ___  ___|(___  ___  ___  ___  ___ ')
time.sleep(0.3)
print('        )|   )|___)|___)|   )    )|    |   )|   )|___)')
time.sleep(0.3)
print('     __/ |__/ |__  |__  |__/  __/ |__  |__/ |    |__  ')
time.sleep(0.3)
print('         |                                                   ')
time.sleep(0.3)
print('                  >>>2017-2018 by noname                     ')
#logo1

time.sleep(1)
print('              ___       ___          __        ___ ')
time.sleep(0.3)
print('        |    |__  \  / |__  |       /  \ |\ | |__  ')
time.sleep(0.3)
print('        |___ |___  \/  |___ |___    \__/ | \| |___ ')
time.sleep(0.3)
print('')
print('                 Correct answer: 10 points         ')
time.sleep(0.3)
print('               ...press <Enter> to start....       ')

#level1

logo1input=input()
if logo1input=='':
  def input_with_timeout(prompt, timeout):
    class local:
      user_is_late = False
    def callback():
      print('time is over', end='', flush=True)
      local.user_is_late = True
    t = Timer(timeout, callback)
    t.start()
    answer = input(prompt)
    if not local.user_is_late:
      t.cancel()
      return answer
  while score<500:
    a=random.randint(1,9)
    b=random.randint(0,9)
    e=["+","yes","okay","yep","right","correctly","good"]
    y=random.choice(e)
    print(a, "+", b)
    ans = input_with_timeout('Type answer: ', 5)
    if type(ans)==type(None):
      print("error")
      print("Your score:", score)
      name=input('type your name for highscores: ')
      highscore=str(score)
      file=open('highscores.txt', 'a')
      scorename=name+" : "+highscore
      file.write(scorename + '\n')
      quit()
    ansisdigit=ans.isdigit()
    if ansisdigit==False:
      print("error")
      print("Your score:", score)
      name=input('type your name for highscores: ')
      highscore=str(score)
      file=open('highscores.txt', 'a')
      scorename=name+" : "+highscore
      file.write(scorename + '\n')
      quit()
    else:
      ans=int(ans)
    if ans:
      O=None
    else:
      print('you did not have time to answer')
      print("Your score:", score)
      name=input('type your name for highscores: ')
      highscore=str(score)
      file=open('highscores.txt', 'a')
      scorename=name+" : "+highscore
      file.write(scorename + '\n')
      quit()
    c=ans
    c=int(c)
    x=a+b
    if c==x:
      score=score+10
      print(y)
    else:
      print("Miss, game over")
      print("Your score:", score)
      name=input('type your name for highscores: ')
      highscore=str(score)
      file=open('highscores.txt', 'a')
      scorename=name+" : "+highscore
      file.write(scorename + '\n')
      quit()
if score==500:
  time.sleep(1)
  print('              ___       ___         ___       __  ')
  time.sleep(0.3)
  print('        |    |__  \  / |__  |        |  |  | /  \ ')
  time.sleep(0.3)
  print('        |___ |___  \/  |___ |___     |  |/\| \__/ ')
  time.sleep(0.3)
  print('')
  print('                 Correct answer: 15 points          ')
  print('               ...press <Enter> to continue...')
  logo2input=input()
  if logo2input=='':
    def input_with_timeout(prompt, timeout):
      class local:
        user_is_late = False
      def callback():
        print('time is over', end='', flush=True)
        local.user_is_late = True
      t = Timer(timeout, callback)
      t.start()
      answer = input(prompt)
      if not local.user_is_late:
        t.cancel()
        return answer
    while score<1250:
      a=random.randint(10,99)
      b=random.randint(0,9)
      e=["+","yes","okay","yep","right","correctly","good"]
      y=random.choice(e)
      print(a, "+", b)
      ans = input_with_timeout('Type answer: ', 5)
      if type(ans)==type(None):
        print("error")
        print("Your score:", score)
        name=input('type your name for highscores: ')
        highscore=str(score)
        file=open('highscores.txt', 'a')
        scorename=name+" : "+highscore
        file.write(scorename + '\n')
        quit()
      ansisdigit=ans.isdigit()
      if ansisdigit==False:
        print("error")
        print("Your score:", score)
        name=input('type your name for highscores: ')
        highscore=str(score)
        file=open('highscores.txt', 'a')
        scorename=name+" : "+highscore
        file.write(scorename + '\n')
        quit()
      else:
        ans=int(ans)
      if ans:
        O=None
      else:
        print('you did not have time to answer')
        print("Your score:", score)
        name=input('type your name for highscores: ')
        highscore=str(score)
        file=open('highscores.txt', 'a')
        scorename=name+" : "+highscore
        file.write(scorename + '\n')
        quit()
      c=ans
      c=int(c)
      x=a+b
      if c==x:
        score=score+15
        print(y)
      else:
        print("Miss, game over")
        print("Your score:", score)
        name=input('type your name for highscores: ')
        highscore=str(score)
        file=open('highscores.txt', 'a')
        scorename=name+" : "+highscore
        file.write(scorename + '\n')
        quit()
if score==1250:
  time.sleep(1)
  print('              ___       ___         ___       __   ___  ___ ')
  time.sleep(0.3)
  print('        |    |__  \  / |__  |        |  |__| |__) |__  |__  ')
  time.sleep(0.3)
  print('        |___ |___  \/  |___ |___     |  |  | |  \ |___ |___ ')
  time.sleep(0.3)
  print('')
  print('                 Correct answer: 20 points         ')
  print('               ...press <Enter> to continue...')
  logo3input=input()
  if logo3input=="":
    def input_with_timeout(prompt, timeout):
      class local:
        user_is_late = False
      def callback():
        print('time is over', end='', flush=True)
        local.user_is_late = True
      t = Timer(timeout, callback)
      t.start()
      answer = input(prompt)
      if not local.user_is_late:
        t.cancel()
        return answer
    while score<2250:
      a=random.randint(10,99)
      b=random.randint(10,99)
      e=["+","yes","okay","yep","right","correctly","good"]
      y=random.choice(e)
      print(a, "+", b)
      ans = input_with_timeout('Type answer: ', 5)
      if type(ans)==type(None):
        print("error")
        print("Your score:", score)
        name=input('type your name for highscores: ')
        highscore=str(score)
        file=open('highscores.txt', 'a')
        scorename=name+" : "+highscore
        file.write(scorename + '\n')
        quit()
      ansisdigit=ans.isdigit()
      if ansisdigit==False:
        print("error")
        print("Your score:", score)
        name=input('type your name for highscores: ')
        highscore=str(score)
        file=open('highscores.txt', 'a')
        scorename=name+" : "+highscore
        file.write(scorename + '\n')
        quit()
      else:
        ans=int(ans)
      if ans:
        O=None
      else:
        print('you did not have time to answer')
        print("Your score:", score)
        name=input('type your name for highscores: ')
        highscore=str(score)
        file=open('highscores.txt', 'a')
        scorename=name+" : "+highscore
        file.write(scorename + '\n')
        quit()
      c=ans
      c=int(c)
      x=a+b
      if c==x:
        score=score+20
        print(y)
      else:
        print("Miss, game over")
        print("Your score:", score)
        name=input('type your name for highscores: ')
        highscore=str(score)
        file=open('highscores.txt', 'a')
        scorename=name+" : "+highscore
        file.write(scorename + '\n')
        quit()
if score==2250:
  time.sleep(1)
  print('              ___       ___          ___  __        __  ')
  time.sleep(0.3)
  print('        |    |__  \  / |__  |       |__  /  \ |  | |__) ')
  time.sleep(0.3)
  print('        |___ |___  \/  |___ |___    |    \__/ \__/ |  \ ')
  time.sleep(0.3)
  print('')
  print('                 Correct answer: 25')
  print('               ...press <Enter> to continue...')
  logo4input=input()
  if logo4input=="":
    def input_with_timeout(prompt, timeout):
      class local:
        user_is_late = False
      def callback():
        print('time is over', end='', flush=True)
        local.user_is_late = True
      t = Timer(timeout, callback)
      t.start()
      answer = input(prompt)
      if not local.user_is_late:
        t.cancel()
        return answer
    while score<3500:
      a=random.randint(100,999)
      b=random.randint(10,99)
      e=["+","yes","okay","yep","right","correctly","good"]
      y=random.choice(e)
      print(a, "+", b)
      ans = input_with_timeout('Type answer: ', 5)
      if type(ans)==type(None):
        print("error")
        print("Your score:", score)
        name=input('type your name for highscores: ')
        highscore=str(score)
        file=open('highscores.txt', 'a')
        scorename=name+" : "+highscore
        file.write(scorename + '\n')
        quit()
      ansisdigit=ans.isdigit()
      if ansisdigit==False:
        print("error")
        print("Your score:", score)
        name=input('type your name for highscores: ')
        highscore=str(score)
        file=open('highscores.txt', 'a')
        scorename=name+" : "+highscore
        file.write(scorename + '\n')
        quit()
      else:
        ans=int(ans)
      if ans:
        O=None
      else:
        print('you did not have time to answer')
        print("Your score:", score)
        name=input('type your name for highscores: ')
        highscore=str(score)
        file=open('highscores.txt', 'a')
        scorename=name+" : "+highscore
        file.write(scorename + '\n')
        quit()
      c=ans
      c=int(c)
      x=a+b
      if c==x:
        score=score+25
        print(y)
      else:
        print("Miss, game over")
        print("Your score:", score)
        name=input('type your name for highscores: ')
        highscore=str(score)
        file=open('highscores.txt', 'a')
        scorename=name+" : "+highscore
        file.write(scorename + '\n')
        quit()
if score==3500:
  time.sleep(1)
  print('              ___       ___          ___         ___')
  time.sleep(0.3)
  print('        |    |__  \  / |__  |       |__  | \  / |__ ')
  time.sleep(0.3)
  print('        |___ |___  \/  |___ |___    |    |  \/  |___')
  time.sleep(0.3)
  print('')
  print('                 Correct answer: 30')
  print('               ...press <Enter> to continue...')
  logo5input=input()
  if logo5input=="":
    def input_with_timeout(prompt, timeout):
      class local:
        user_is_late = False
      def callback():
        print('time is over', end='', flush=True)
        local.user_is_late = True
      t = Timer(timeout, callback)
      t.start()
      answer = input(prompt)
      if not local.user_is_late:
        t.cancel()
        return answer
    while True:
      a=random.randint(100,999)
      b=random.randint(100,999)
      e=["+","yes","okay","yep","right","correctly","good"]
      y=random.choice(e)
      print(a, "+", b)
      ans = input_with_timeout('Type answer: ', 5)
      if type(ans)==type(None):
        print("error")
        print("Your score:", score)
        name=input('type your name for highscores: ')
        highscore=str(score)
        file=open('highscores.txt', 'a')
        scorename=name+" : "+highscore
        file.write(scorename + '\n')
        quit()
      ansisdigit=ans.isdigit()
      if ansisdigit==False:
        print("error")
        print("Your score:", score)
        name=input('type your name for highscores: ')
        highscore=str(score)
        file=open('highscores.txt', 'a')
        scorename=name+" : "+highscore
        file.write(scorename + '\n')
        quit()
      else:
        ans=int(ans)
      if ans:
        O=None
      else:
        print('you did not have time to answer')
        print("Your score:", score)
        name=input('type your name for highscores: ')
        highscore=str(score)
        file=open('highscores.txt', 'a')
        scorename=name+" : "+highscore
        file.write(scorename + '\n')
        quit()
      c=ans
      c=int(c)
      x=a+b
      if c==x:
        score=score+30
        print(y)
      else:
        print("Miss, game over")
        print("Your score:", score)
        name=input('type your name for highscores: ')
        highscore=str(score)
        file=open('highscores.txt', 'a')
        scorename=name+" : "+highscore
        file.write(scorename + '\n')
        quit()
