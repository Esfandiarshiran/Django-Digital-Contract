from django.shortcuts import render
from Docusign_Contract.docusign_helper import *


DS_JWT = {

    "ds_client_id": "************************",
    "ds_impersonated_user_id": "**********************",  # The id of the user.
    "private_key_file": "Docusign_Contract/private.key",
    "authorization_server": "account-d.docusign.com",
    'account_id': '********************************',
}

SCOPES = [
    "signature", "impersonation"
]


def get_consent_url():
    url_scopes = "+".join(SCOPES)

    # Construct consent URL
    redirect_uri = 'http://127.0.0.1:8000/contract/confirm-contract'
    consent_url = f"https://{DS_JWT['authorization_server']}/oauth/auth?response_type=code&" \
                  f"scope={url_scopes}&client_id={DS_JWT['ds_client_id']}&redirect_uri={redirect_uri}"

    return consent_url


def get_token(private_key, api_client):
    # Call request_jwt_user_token method
    token_response = get_jwt_token(private_key, SCOPES, DS_JWT["authorization_server"], DS_JWT["ds_client_id"],
                                   DS_JWT["ds_impersonated_user_id"])
    access_token = token_response.access_token
    # Save API account ID
    user_info = api_client.get_user_info(access_token)
    accounts = user_info.get_accounts()
    api_account_id = accounts[0].account_id
    base_path = accounts[0].base_uri + "/restapi"

    return {"access_token": access_token, "api_account_id": api_account_id, "base_path": base_path}


def get_args(api_account_id, access_token, base_path, user_data={}):
    # you can get base path from get token function
    signer_email = user_data['signer_email']  # get this from form in your django page template (sending page)
    signer_name = user_data['signer_name']
    receiver_name = user_data['receiver_name']
    receiver_email = user_data['receiver_email']
    date = user_data['date']
    contract_text = user_data['contract_text']
    ds_return_url = user_data['ds_return_url']

    envelope_args = {

        "signer_email": signer_email,
        "signer_name": signer_name,
        'receiver_name': receiver_name,
        'receiver_email': receiver_email,
        'date': date,
        "status": "sent",
        'contract_text': contract_text,
        'ds_return_url': ds_return_url,
        'account_id': DS_JWT['account_id'],
        'signer_client_id': DS_JWT['ds_impersonated_user_id'],
    }
    args = {
        "account_id": api_account_id,
        "base_path": base_path,
        "access_token": access_token,
        "envelope_args": envelope_args
    }

    return args
