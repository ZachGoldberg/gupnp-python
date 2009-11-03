import sys

tests_total = 0
tests_pass = 0
tests_fail = 0
tests_skip = 0

device_test_complete = False


def check_exit():
  if (device_test_complete):
    sys.exit(0)

def test_begin(name):
  sys.stdout.write("Begin test %s..." % name)
  sys.stdout.flush()

def test_end(passed):
  if passed:
	sys.stdout.write("\033[1;32m Passed\033[00m\n")
  else:
	sys.stdout.write("\033[1;31m Failed\033[00m\n")

def test_skip(a=None, doc=""):
  sys.stdout.write("\033[0;33mSkipped... (%s)\033[00m\n" % doc)

def t(func, args=None):
  if not args: args={}
  obj = func(**args)
  sys.stdout.write("(Value: %s) " % obj.__repr__())
  return dir(obj) != None
