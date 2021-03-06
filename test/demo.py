from gi.repository import GLib, GUPnP, GSSDP, GObject, libsoup

def device_available(device, cp):
  import pdb
  pdb.set_trace()
  print cp

# Note: glib.thread_init() doesn't work here, have to use the gobject call
GObject.threads_init()

# Get a default maincontext
main_ctx = GLib.main_context_default() 

ctx = GUPnP.Context(interface="eth0")

# Bind to eth0 in the maincontext on any port
cp  = GUPnP.ControlPoint().new(ctx, "upnp:rootdevice")

# Use glib style .connect() as a callback on the controlpoint to listen for new devices
cp.connect("device-proxy-available", device_available)

# "Tell the Control Point to Start Searching"
GSSDP.ResourceBrowser.set_active(cp, True)

# Enter the main loop which begins the work and facilitates callbacks
GObject.MainLoop().run()

# Be cheeky, and intentionally NOT clean up memory because python is awesome
print "You'll never know I am here!"
