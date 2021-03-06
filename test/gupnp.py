from gi.repository import GLib, GUPnP, GSSDP, GObject, libsoup
from gupnp_device_tests import device_available
from gupnp_control_point_tests import test_control_point
from gupnp_service_proxy_tests import device_available_service_test

# Note: glib.thread_init() doesn't work here, have to use the gobject call
GObject.threads_init()

# Get a default maincontext
main_ctx = GLib.main_context_default() 

test_control_point()
ctx = GUPnP.Context(interface="eth0")

# Bind to eth0 in the maincontext on any port
cp  = GUPnP.ControlPoint().new(ctx, "upnp:rootdevice")

# Use glib style .connect() as a callback on the controlpoint to listen for new devices
cp.connect("device-proxy-available", device_available)
cp.connect("device-proxy-available", device_available_service_test)

# "Tell the Control Point to Start Searching"
GSSDP.ResourceBrowser.set_active(cp, True)

# Enter the main loop which begins the work and facilitates callbacks
GObject.MainLoop().run()
  

# Be cheeky, and intentionally NOT clean up memory because python is awesome
print "You'll never know I am here!"


def root_device_test():
  pass
