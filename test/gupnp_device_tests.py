from gupnp_test_framework import *
import gupnp_test_framework as testing

def device_available(cp, device):
  if testing.device_test_complete:
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

  test_begin("Check device list_devices")
  test_end(t(device.list_devices)) 

  test_begin("Check device url")
  test_end(t(device.get_url_base))

  test_begin("Check device list_services")
  test_end(t(device.list_services))

  test_begin("Check device icon url")
  test_skip(device.get_icon_url, "Needs params")

  test_begin("Check device description value")
  test_skip(device.get_description_value, "needs params")

  test_begin("Check device get_device")
  test_skip(device.get_device, "needs params")

  test_begin("Check device get_service")
  test_skip(device.get_service, "needs params")

  testing.device_test_complete = True

  check_exit()
