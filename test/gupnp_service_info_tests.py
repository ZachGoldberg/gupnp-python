import gupnp_test_framework as testing
from gupnp_test_framework import *

def callback(stuff):
  print stuff
 

def service_info_tests(service):
  test_begin("Check service context")
  test_end(t(service.get_context))

  test_begin("Check service location")
  test_end(t(service.get_location))

  test_begin("Check service url base")
  test_end(t(service.get_url_base))

  test_begin("Check service udn")  
  test_end(t(service.get_udn))

  test_begin("Check service type")
  test_end(t(service.get_service_type))

  test_begin("Check service id")
  test_end(t(service.get_id))

  test_begin("Check service scpd url")
  test_end(t(service.get_scpd_url))

  test_begin("Check service control url")
  test_end(t(service.get_control_url))

  test_begin("Check service event_subscription_url")
  test_end(t(service.get_event_subscription_url))

  test_begin("Check service get introspection")
  test_end(t(service.get_introspection))

#  test_begin("Check service get introspection async")
#  test_end(f(service.get_introspection_async, [callback, None]))



