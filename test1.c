#include <glib.h>
#include "libgupnp/gupnp.h"

static GMainLoop *main_loop;

static void
device_available_cb (GUPnPControlPoint *cp,
                            GUPnPDeviceProxy *proxy)
{

  GUPnPDeviceInfo* gupnp_device_info = GUPNP_DEVICE_INFO(proxy);
  g_print("Device model name: %s\n", gupnp_device_info_get_model_name(gupnp_device_info));

}


int main(int argc, char** argv)
{
  GUPnPContext *context;
  GUPnPControlPoint *cp;
  
  /* Required initialisation */
  g_thread_init (NULL);
  g_type_init ();

  /* Create a new GUPnP Context.  By here we are using the default GLib main
     context, and connecting to the current machine's default IP on an
     automatically generated port. */
  context = gupnp_context_new (NULL, NULL, 0, NULL);

  /* Create a Control Point targeting WAN IP Connection services */
  cp = gupnp_control_point_new
    (context, "upnp:rootdevice");

  /* The service-proxy-available signal is emitted when any services which match
     our target are found, so connect to it */
    g_signal_connect (cp,
		    "device-proxy-available",
		    G_CALLBACK (device_available_cb),
		    NULL);
    

  /* Tell the Control Point to start searching */
  gssdp_resource_browser_set_active (GSSDP_RESOURCE_BROWSER (cp), TRUE);
  
  /* Enter the main loop. This will start the search and result in callbacks to
     service_proxy_available_cb. */
  main_loop = g_main_loop_new (NULL, FALSE);

  g_main_loop_run (main_loop);

  /* Clean up */
  g_main_loop_unref (main_loop);
  g_object_unref (cp);
  g_object_unref (context);
  
  return 0;
}
