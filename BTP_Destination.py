from fastapi import Request, HTTPException
import os
import json
import requests

def get_sac_destination(dest_name: str):
    vcap_services = json.loads(os.environ.get("VCAP_SERVICES", "{}"))
    destinations = vcap_services.get("destination", [])

    if not destinations:
        raise Exception("No destination service found in VCAP_SERVICES")

    credentials = destinations[0]["credentials"]
    uri = credentials["uri"]
    clientid = credentials["clientid"]
    clientsecret = credentials["clientsecret"]
    token_url = credentials["url"] + "/oauth/token"

    # Step 1: Get access token for destination service
    token_resp = requests.post(token_url, data={
        "grant_type": "client_credentials"
    }, auth=(clientid, clientsecret))

    token_resp.raise_for_status()
    access_token = token_resp.json()["access_token"]

    # Step 2: Use token to call destination configuration
    dest_resp = requests.get(
        f"{uri}/destination-configuration/v1/destinations/{dest_name}",
        headers={"Authorization": f"Bearer {access_token}"}
    )
    dest_resp.raise_for_status()
    destination_config = dest_resp.json()
    return destination_config
