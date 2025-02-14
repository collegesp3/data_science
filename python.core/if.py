# ------ Switch - case ----------

choice = 'Cheb'

print ({ 'Gena' : 500,
         'Shapoklyak' : 300,
         'Cheb' : 150}[choice])

# ------------- defaults ---------------

prosto = {'Fedor'     : 12,
          'Sharik'    : 7,
          'Matroskin' : 5 }
print(prosto.get('Fedor', 'No one at home!'))
print(prosto.get('Pechkin', 'No one at home!'))

# ------------- functions ---------------

def say():
    print("It's nothing! A mundane matter")

astrid = {'Karlsson' : say,
          'Kid' : "I'm so bored..." ,
          'Freken Bok' : lambda: print(3*'God dag!')
          }

astrid.get('Karlsson')()

print(astrid.get('Kid'))

astrid.get('Freken Bok')()