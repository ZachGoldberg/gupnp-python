from gi.repository import GLib, GUPnP, GUPnPAV, GSSDP, GObject, libsoup
import os
import pdb

devices = []
introspections = []
containers = []
objects = []
serv = None


def play_complete(service, action, userdata):
   print "PLAY COMPLETE"

def set_uri_complete(service, action, userdata):
   print "SET URI DONE"
   data2 = {"Speed": "1", "InstanceID": "0"}
   service.end_action_hash(action, {})
   service.begin_action_hash("Play", play_complete, None, data2)

def got_introspection(service, intro, error, userdata):
  print "Got introspection!"
  global introspections
  introspections[service] = intro

  actions = intro.list_actions()
  print len(actions)
  for i in actions:
      print service.get_service_type(), i.name      
      if i.name == "SetAVTransportURI":
          dict = {"Speed": "1", "InstanceID": "0"}
          muri = "http://192.168.1.55:49152/content/media/object_id=6327&res_id=0&ext=.mp3"
          curi = "http://192.168.1.55:49152/content/media/object_id=6327&res_id=0&ext=.mp3"
          data = {"InstanceID": "0", "CurrentURI": curi, "CurrentURIMetaData": muri} 
          service.send_action_hash(i.name, data, {})
	  print "Done setting URI"
          data2 = {"Speed": "1", "InstanceID": "0"}
          service.send_action_hash("Stop", {"InstanceID": 0}, {})
          print "Done Stopping"
          service.send_action_hash("Play", data2, {})


def new_item(node, object):
  print object.get_title() 
  objects.append(object)

def new_container(node, object):
  containers.append(object)
  in_data = {"ObjectID": object.get_id(), "BrowseFlag": "BrowseDirectChildren",
		    "Filter": "", "StartingIndex": "0", "RequestCount": "0",
		    "SortCriteria": ""}
  out_data = {"Result": "", "NumberReturned": "", "TotalMatches": "", "UpdateID": ""}
  return_data = serv.send_action_hash("Browse", in_data, out_data)
  parser = GUPnPAV.GUPnPDIDLLiteParser()
  parser.connect("container_available", new_container)
  parser.connect("item_available", new_item)
  parser.parse_didl(return_data[1]["Result"])
 
 

def server_introspection(service, introspection, error, userdata):
  print "Got server introspection"
  for i in introspection.list_actions():
      if i.name == "Browse":
         in_data = {"ObjectID": "0", "BrowseFlag": "BrowseDirectChildren",
		    "Filter": "", "StartingIndex": "0", "RequestCount": "0",
		    "SortCriteria": ""}
         out_data = {"Result": "", "NumberReturned": "", "TotalMatches": "", "UpdateID": ""}
	 print "SEND ACTION"
         return_data = service.send_action_hash("Browse", in_data, out_data)
	 global serv
	 serv=service
	 print "Good news!"
	 print return_data[1]["Result"]
	 parser = GUPnPAV.GUPnPDIDLLiteParser()
	 parser.connect("container_available", new_container)
	 parser.connect("item_available", new_item)
	 parser.parse_didl(return_data[1]["Result"])
	 print len(objects)

def device_available(cp, device):
  devices.append(device)
  print device.get_model_name()
  for service in device.list_services():
      print service.get_service_type()
      service.get_introspection_async(got_introspection, None)

#  if device.get_model_name() == "MediaTomb":
#      for service in device.list_services():
#          print service.get_service_type()
#          if "ContentDirectory" in service.get_service_type():
#              service.get_introspection_async(server_introspection, None)

def run_timer():
  return True

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

#GObject.timeout_add(1000, run_timer)

# Enter the main loop which begins the work and facilitates callbacks
GObject.MainLoop().run()

