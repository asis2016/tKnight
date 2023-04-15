import os
from django.views.generic import TemplateView
import ldap3
from dotenv import load_dotenv

# load environment variables from .env file
load_dotenv()


class LDAPView(TemplateView):
    """
    """
    template_name = "ldap.html"
    
    # set LDAP server and bind credentials
    server = ldap3.Server('ldap://ldap.example.com')
    bind_dn = 'cn=admin,dc=example,dc=com'
    bind_password = 'password'

    base_dn = 'dc=example,dc=com'
    search_filter = '(objectClass=inetOrgPerson)'
    attributes = ['count']

    x = os.environ.get('MYSQL_PASS')
    print(x)


