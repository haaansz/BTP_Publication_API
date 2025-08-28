from fastapi import FastAPI, Request, Body, HTTPException
import jwt
import requests
import BTP_Destination
import SAC_API

app = FastAPI()

#run CLI Check and install on startup
#cli_setup.check_and_install_tools()

@app.post("/")
async def auth_check(request: Request):
    # Authenticate the request using the authentication logic from auth.py
    # If authentication is successful, return HTTP 200 OK
    return {"message": "Authentication successful", "status": "200 OK"}

@app.api_route("/hello", methods=["GET", "POST"])
async def say_hello(request: Request):
    # Authenticate the request using the authentication logic from auth.py
    return {"message": "Hello, World"}


@app.api_route("/sac-auth-check", methods=["GET", "POST"])
async def test_dest(request: Request):
    dest = BTP_Destination.get_sac_destination("SAC_OAUTH2_APIACCESS")
    csrf_token, cookies = SAC_API.get_csrf_token(dest)
    return csrf_token, cookies

@app.api_route("/execute_multiaction", methods=["GET", "POST"])
async def call_multi(request: Request):
    if request.method == "POST":
        body = await request.json()
        multiaction_id = body.get("multiaction_id")
    dest = BTP_Destination.get_sac_destination("SAC_OAUTH2_APIACCESS")
    csrf_token, cookies = SAC_API.get_csrf_token(dest)
    response = SAC_API.trigger_sac_multiaction(dest, csrf_token, cookies, multiaction_id)
    return response

@app.get("/jwt-info")
async def jwt_info(request: Request):
    auth_header = request.headers.get("Authorization")
    print("Authorization header:", auth_header)  # <--- Add this line

    if not auth_header:
        raise HTTPException(status_code=401, detail="Missing Authorization header")

    token = auth_header[7:] if auth_header.lower().startswith("bearer ") else auth_header

    try:
        decoded = jwt.decode(token, options={"verify_signature": False})
        return decoded
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Invalid JWT: {str(e)}")

