import looker_sdk
import urllib3
import os
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
import datetime
import json

with open('looker_api_creds.json', 'r') as f:
    looker_api_creds = json.load(f)
os.environ['LOOKERSDK_BASE_URL'] = looker_api_creds["LOOKERSDK_BASE_URL"]
os.environ['LOOKERSDK_CLIENT_ID'] = looker_api_creds["LOOKERSDK_CLIENT_ID"]
os.environ['LOOKERSDK_CLIENT_SECRET'] = looker_api_creds["LOOKERSDK_CLIENT_SECRET"]

os.environ['LOOKERSDK_VERIFY_SSL']= 'False'
os.environ['LOOKERSDK_API_VERSION']= '4.0'
os.environ["LOOKERSDK_TIMEOUT"] = "120"

sdk = looker_sdk.init40()

def looker_search_user(user_email):
  response = sdk.user_for_credential('email', user_email)
  print(response)
  return response

def looker_create_sso_url_as_me(dashboard_url, user_id):
    # login User for URL creation
    a = sdk.auth.login_user(str(user_id))
    body=looker_sdk.models40.EmbedParams(
        target_url=f"{dashboard_url}",
        session_length=600,
        force_logout_login=True
      )
    response = sdk.create_embed_url_as_me(body)
    return response