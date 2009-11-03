from gi.repository import GUPnP
from gupnp_test_framework import *
import gupnp_test_framework as testing

def test_control_point():
  if testing.control_point_test_complete:
     return

  test_begin("Create a new control point")
  ctx = GUPnP.Context(interface="eth0")
  cp = GUPnP.ControlPoint().new(ctx, "upnp:rootdevice")
  test_end(cp)

  test_begin("Create a control_point_new_full")
  rf = GUPnP.ResourceFactory.new()
  cp2 = GUPnP.ControlPoint().new_full(ctx, rf, "upnp:rootdevice")
  test_end(cp2)

  test_begin("Get resource factory")
  test_end(t(cp2.get_resource_factory))

  test_begin("Get Context")
  test_end(t(cp2.get_context))

  test_begin("List device proxies")
  test_end(t(cp2.list_device_proxies))

  test_begin("List service proxies")
  test_end(t(cp2.list_service_proxies))

  testing.control_point_test_complete = True

  check_exit()
