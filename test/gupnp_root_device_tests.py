from gi.repository import GUPnP

from gupnp_test_framework import *
import gupnp_test_framework as testing

def root_device_tests(cp, ctx):
  if testing.root_device_test_complete:
     return

  desc = "/home/zgold/progrepo/guPnP/gupnp-python/desc.txt"
  desc_loc = "/tmp"  

  test_begin("New Root Device")
  rd = GUPnP.RootDevice.new(ctx, desc, desc_loc)
  return
  test_end(dir(rd))

  test_begin("Get rd avail should be default False")
  test_end(not rd.get_available())

  test_begin("Set root device to available")
  test_end(t(rd.set_available, [True]))

  test_begin("Root device should now be available")
  test_end(rd.get_available())
  
  test_begin("Get relative location")
  test_end(t(rd.get_relative_location))
 
  test_begin("Get description dir")
  test_end(rd.get_description_dir() == desc_loc)

  test_begin("Get description path")
  test_end(rd.get_description_path() == desc)

  testing.root_device_test_complete = True
