from gi.repository import GUPnP
from gupnp_test_framework import *
import gupnp_test_framework as testing
from gupnp_root_device_tests import root_device_tests

def test_control_point():
  if testing.control_point_test_complete:
     return

  ctx = test_context()

  test_begin("Create a new control point") 
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

  root_device_tests(cp, ctx)

  check_exit()

def test_context():

  test_begin("Create new GUPnPContext")
  ctx = GUPnP.Context(interface="eth0")
  test_end(dir(ctx))
 
  test_begin("Get context host ip")
  test_end(t(ctx.get_host_ip))

  test_begin("Get context port")
  test_end(t(ctx.get_port))

  test_begin("Get context server")
  test_end(t(ctx.get_server))

  test_begin("Get context session")
  test_end(t(ctx.get_session))

  test_begin("Get context subscription timeout")
  test_end(t(ctx.get_subscription_timeout))

  test_begin("set context subscription timeout")
  test_end(t(ctx.set_subscription_timeout, [1500]))

  test_begin("Get context subscription timeout")
  test_end(e(ctx.get_subscription_timeout(), 1500))

  test_begin("Get context host path")
  path = "/home/zgold/progrepo/guPnP/gupnp-python/desc.txt"
  test_end(t(ctx.host_path, [path, "/"]))

  test_begin("Get context unhost path")
  test_end(t(ctx.unhost_path, [path]))

  return ctx
