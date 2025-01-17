# -------------- s t a r t ------------------------
print('\n',11*'- ', 's t a r t ',11*'- ', '\n')

def tester(start):
    def nested(label):
        print(label, nested.state)
        nested.state += 1
    nested.state = start
    return nested

F = tester(0)
F('star')
F('sky')

print('F.state : ', F.state)


# -------------- e n d ------------------------
print('\n',11*'- ', 'e n d ',11*'- ', '\n')