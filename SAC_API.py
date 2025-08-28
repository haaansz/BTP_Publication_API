import requests

def get_csrf_token(destination_config):
    target_url = destination_config["destinationConfiguration"]["URL"]
    auth = destination_config["authTokens"][0]  # Contains access token
    access_token = auth["value"]
    token_type = auth["type"]  # Usually "Bearer"

    # Request CSRF token
    headers = {
        "Authorization": f"{token_type} {access_token}",
        "x-csrf-token": "fetch",
        "Content-Type": "application/json"
    }

    response = requests.get(
        f"{target_url}/api/v1/csrf",
        headers=headers
    )

    if response.status_code != 200:
        raise Exception(f"CSRF fetch failed: {response.status_code} {response.text}")

    csrf_token = response.headers.get("x-csrf-token")
    cookies = response.cookies  # May be needed for the follow-up call

    return csrf_token, cookies


def trigger_sac_multiaction(destination_config, csrf_token, cookies, multiaction_id):
    target_url = destination_config["destinationConfiguration"]["URL"]
    auth = destination_config["authTokens"][0]
    access_token = auth["value"]
    token_type = auth["type"]  # typically "Bearer"

    # === Schritt 2: MultiAction aufrufen ===
    post_url = f"{target_url}/api/v1/multiActions/{multiaction_id}/executions"

    headers = {
        "Authorization": f"{token_type} {access_token}",
        "x-csrf-token": csrf_token,
        "Content-Type": "application/json"
    }

    body = {
        "parameterValues": []
    }

    response = requests.post(
        post_url,
        headers=headers,
        cookies=cookies,
        json=body
    )

    if response.status_code != 202:
        return {
            "error": "MultiAction call failed",
            "status_code": response.status_code,
            "response_text": response.text,
            "post_url": post_url,
            "headers": headers,
            "body": body,
            "cookies_sent": cookies.get_dict() if cookies else None
        }

    return response.json()