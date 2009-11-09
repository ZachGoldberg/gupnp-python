import sys

tests_total = 0
tests_pass = 0
tests_fail = 0
tests_skip = 0

root_device_test_complete = False
device_test_complete = False
control_point_test_complete = False
service_test_complete = False

def check_exit():
  if device_test_complete and control_point_test_complete \
    and service_test_complete:
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

def e(val, expected):
  sys.stdout.write(" (got %s expected %s) " % (val, expected))
  return val == expected

def t(func, args=None):
  if not args: args=[]
  obj = func(*args)
  sys.stdout.write("(Value: %s) " % obj.__repr__())
  if isinstance(obj, list):
    return dir(obj) != None and obj[0] != None
  return dir(obj) != None

def f(func, args=None):
  if not args: args=[]
  success = True
  try:
      obj = func(*args)
  except Exception, e:
      success = False
      sys.stdout.write(" (%s) " % str(e))

  return not success

