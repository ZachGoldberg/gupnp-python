from gi.repository import GLib, GUPnP, GSSDP, GObject

def device_available(cp, device):
   print "GOT A DEVICE!  Its model name is :", device.get_model_name()
   import pdb
#   pdb.set_trace()

# Note: glib.thread_init() doesn't work here, have to use the gobject call
GObject.threads_init()

# Get a default maincontext
main_ctx = GLib.main_context_default() 


# Bind to eth0 in the maincontext on any port
ctx = GUPnP.UPnPContext(interface="eth0", port=0)

import pdb
pdb.set_trace()

# Pretend to be a root device (Zeeshan needs to document these uri things...)
cp  = GUPnP.UPnPControlPoint()
cp = cp.new(ctx, "upnp:rootdevice")

# Use glib style .connect() as a callback on the controlpoint to listen for new devices
cp.connect("device-proxy-available", device_available)

# "Tell the Control Point to Start Searching"
GSSDP.ResourceBrowser.set_active(cp, True)

# Enter the main loop which begins the work and facilitates callbacks
GObject.MainLoop().run()

# Be cheeky, and intentionally NOT clean up memory because python is awesome
print "You'll never know I am here!"
