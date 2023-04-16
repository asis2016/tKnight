import os
from django.views.generic import TemplateView
import ldap3
from django.conf import settings
from dotenv import load_dotenv
import json


# Import .env
base_dir = os.path.join(settings.BASE_DIR)
env_path = f"{base_dir}../.env"
load_dotenv(dotenv_path=env_path)

#
LDAP_AUTH_URL = os.getenv("LDAP_HOST")
LDAP_BASE_DN = os.getenv("LDAP_BASE_DN")
LDAP_ADMIN_DN = os.getenv("LDAP_ADMIN_DN")
LDAP_ADMIN_PASSWORD = os.getenv("LDAP_ADMIN_PASSWORD")



class IdentitiesListView(TemplateView):
    template_name = "ds/identities.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        conn = None
        try:
            # Connect to the LDAP server
            server = ldap3.Server(LDAP_AUTH_URL)
            conn = ldap3.Connection(server, user=LDAP_ADMIN_DN, password=LDAP_ADMIN_PASSWORD)
            conn.bind()

            # Search for all user objects
            search_filter = "(objectClass=inetOrgPerson)"
            attrs = ["cn", "givenName", "sn"]
            conn.search(LDAP_BASE_DN, search_filter, attributes=attrs, search_scope=ldap3.SUBTREE)

            # Parse the search results into a list of user dictionaries
            users = []
            
            for entry in conn.entries:
                user = {
                    "cn": entry.cn,
                    "givenName": entry.givenName,
                    "sn": entry.sn,
                }
                users.append(user)

            # context
            context["users"] = users
            return context
        except ldap3.core.exceptions.LDAPException as e:
            # todo: make a "global" log
            print(str(e))
        finally:
            # Unbind from the server
            if conn:
                conn.unbind()
        

class DSSettingsView(TemplateView):
    template_name = "ds/settings.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        with open(os.path.join(settings.DATA_DIRS, "ds_settings.json")) as f:
            data = json.load(f)
            context["json_data"] = data
        return context
    

class DSListView(TemplateView):
    """
    """
    template_name = "ds/index.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
