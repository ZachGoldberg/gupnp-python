from gi.repository import GObject
from gupnp_test_framework import *
import gupnp_test_framework as testing

def dummy():
  print "DUMMY TEST RUN"

def device_available_service_test(cp, device):
  if testing.service_test_complete:
      return

  test_begin("Check device list_services")
  test_end(t(device.list_services))

  services = device.list_services()
  service = None
  if len(services) > 0:
    service = services[0]

  test_begin("Check send action hash")
  test_end(f(service.send_action_hash, ["Action", {}, {}]))

  print "WARNING: send_action() and send_acton_valist() seem to be unsupported?"

  test_begin("Check begin action hash")
  test_end(f(service.begin_action_hash, ["Action", dummy, dummy, {}]))

  #service_action = service.begin_action_hash...

  print "WARNING: begin_action() and begin_acton_valist() seem to be unsupported?"

  test_begin("Check end action hash")
  test_end(f(service.end_action_hash, ["Action", {}]))

  print "WARNING: end_action() and end_acton_valist() seem to be unsupported?"

  test_begin("Check cancel action ")
  test_end(f(service.cancel_action, ["ServiceAction"]))

  test_begin("Check add notify ")
  test_end(f(service.add_notify, ["Acion", GObject.GType("GType"), dummy, None]))

  test_begin("Check remove notify")
  test_end(f(service.remove_notify, ["Action", None, None]))
  testing.service_test_complete = True

  check_exit()


def service_action_test(service_action = None):
   pass
