def fn(a, b=12, c=52):
	print(a, b, c)

fn(5, 7, 15)
fn(c=3, b=9, a=11)
fn(33, c=9, b=11)
fn(0)
fn(21, c=76)
fn(333, 8)

# ------------------------------------
print('_next_'.center(20,'-'))

def fn2(*args):
	print(args[0]*2, args[1]*3)

#fn2()
#fn2(11)
fn2(33, 'sol')

# ------------------------------------
print('_next_'.center(20,'-'))

def fn3(**args):
	print(args)

fn3()
fn3(a=45, b='wind')

F1, args = fn3, {'c':'moon', 'd':3.14}
F1(**args)

print(F1.__name__)
# ------------------------------------
print('_next_'.center(20,'-'))


