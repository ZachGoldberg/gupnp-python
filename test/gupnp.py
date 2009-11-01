from gi.repository import GLib, GUPnP, GSSDP, GObject, libsoup
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

def device_available(cp, device):
  global device_test_complete
  if device_test_complete:
     return
  test_begin("Check device location")
  test_end(t(device.get_location))

  test_begin("Check device udn")
  test_end(t(device.get_udn))

  test_begin("Check device type")
  test_end(t(device.get_device_type))

  test_begin("Check device friendly name")
  test_end(t(device.get_friendly_name))

  test_begin("Check device manufacturer")
  test_end(t(device.get_manufacturer))

  test_begin("Check device manufacturer url")
  test_end(t(device.get_manufacturer_url))

  test_begin("Check device model description")
  test_end(t(device.get_model_description))

  test_begin("Check device model name")
  test_end(t(device.get_model_name))

  test_begin("Check device model number")
  test_end(t(device.get_model_number))

  test_begin("Check device model url")
  test_end(t(device.get_model_url))

  test_begin("Check device serial number")
  test_end(t(device.get_serial_number))

  test_begin("Check device presentation url")
  test_end(t(device.get_presentation_url))

  test_begin("Check device upc")
  test_end(t(device.get_upc))

  test_begin("Check device dlna capabilities")
  test_end(t(device.list_dlna_capabilities))

  test_begin("Check device list_device_types")
  test_end(t(device.list_device_types))

  test_begin("Check device list_service_types")
  test_end(t(device.list_service_types))
	
  test_begin("Check device icon url")
  test_skip(device.get_icon_url, "Needs params")

  test_begin("Check device list_devices")
  test_skip(device.list_devices, "Known segv")

  test_begin("Check device list_services")
  test_skip(device.list_services, "known segv")

  test_begin("Check device description value")
  test_skip(device.get_description_value, "needs params")

  test_begin("Check device url")
  test_skip(device.get_url_base, "known segv")

  test_begin("Check device get_device")
  test_skip(device.get_device, "needs params")

  test_begin("Check device get_service")
  test_skip(device.get_service, "needs params")

  device_test_complete = True

  check_exit()

# Note: glib.thread_init() doesn't work here, have to use the gobject call
GObject.threads_init()

# Get a default maincontext
main_ctx = GLib.main_context_default() 


# Bind to eth0 in the maincontext on any port
ctx = GUPnP.UPnPContext(main_ctx, "eth0", 0)

# Pretend to be a root device (Zeeshan needs to document these uri things...)
cp  = GUPnP.UPnPControlPoint(ctx, "upnp:rootdevice")
#cp  = GUPnP.UPnPControlPoint(ctx, "ssdp:all")

# Use glib style .connect() as a callback on the controlpoint to listen for new devices
cp.connect("device-proxy-available", device_available)

# "Tell the Control Point to Start Searching"
GSSDP.ResourceBrowser.set_active(cp, True)

# Enter the main loop which begins the work and facilitates callbacks
GObject.MainLoop().run()

# Be cheeky, and intentionally NOT clean up memory because python is awesome
print "You'll never know I am here!"
