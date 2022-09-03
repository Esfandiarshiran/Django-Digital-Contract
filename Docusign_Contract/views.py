import datetime

from django.http import HttpResponse
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt
from docusign_esign import ApiException

from .eg001_embedded_signing import Eg001EmbeddedSigningController
from .docusign import get_args
from .forms import ContractForm, SignForm
from Docusign_Contract.docusign import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


def essential_data(user_data_dic):
    # ----------------------------------------------------------------------------
    api_client = ApiClient()
    api_client.set_base_path(DS_JWT["authorization_server"])
    api_client.set_oauth_host_name(DS_JWT["authorization_server"])
    # ---------------
    private_key = get_private_key(DS_JWT["private_key_file"]).encode("ascii").decode("utf-8")
    # --------------
    access_token_data = get_token(private_key, api_client)  # access_token, api_account_id, base_path
    # --------------
    args = get_args(access_token_data["api_account_id"], access_token_data["access_token"],
                    access_token_data["base_path"],
                    user_data_dic)  # return: account_id, base_path , access_token, envelope_args
    # -----------------------------------------------------------------------------
    return {
        'api_client': api_client,
        'api_account_id': access_token_data['api_account_id'],
        'args': args,
        'account_id': args['account_id'],
        'base_path': args['base_path'],
        'access_token': args['access_token'],
        'envelope_args': args['envelope_args'],
    }


# write contract and authenticate user to write contract
@login_required(login_url='/account/login')
def open_contract(request):
    form = ContractForm(request.POST or None)
    context = {
        'form': form,
    }
    if form.is_valid():
        cd = form.clean()
        contract_text = cd['contract']
        # defining global fuction to return value (ex: form value) everywhere you want
        global contract

        def contract():
            return contract_text

        consent_url = get_consent_url()
        return redirect(consent_url)

    return render(request, 'Docusign_Contract/create_contract.html', context)


@login_required(login_url='/account/login')
def confirm_contract(request):
    try:
        contract_text = contract()
    except Exception as err:
        # todo: redirect user to previous page
        raise err
    form = SignForm(request.POST or None)
    # pass data, and render in contract page
    context = {
        'form': form,
        'signer_name': 'fill out signer name please...',
        'signer_email': 'fill out signer name please...',
        'date': datetime.date.today(),
        'sender_name': request.user.first_name,
        'sender_email': request.user.email,
        'contract_text': contract_text,
    }
    # --------------- argument to p pass in  essential_data - get_args-----------------------
    if form.is_valid():
        cd = form.clean()
        date = datetime.date.today()
        user_data_dic = {
            'signer_name': request.user.first_name,
            'signer_email': request.user.email,
            'receiver_name': cd['full_name'],
            'receiver_email': cd['email'],
            'date': cd['date'],
            'contract_text': contract_text,
            'ds_return_url': 'http://127.0.0.1:8000/contract/success-contract',
            'signer_client_id': DS_JWT['ds_client_id'],
        }

        try:
            args = essential_data(user_data_dic)['args']
            # 2. use embedded method to do first sign by user
            results = Eg001EmbeddedSigningController.worker(args)
        except ApiException as err:
            raise Exception("Exception when calling DocuSign API: %s" % err)

        global envelope_deta
        def envelope_data():
            return user_data_dic
        return redirect(results["redirect_url"])

    return render(request, 'Docusign_Contract/sending_contract.html', context)


@csrf_exempt
def success_contract(request):
    context = {
        'user_data': None
    }
    # todo: add usr data here to show success page
    return render(request, 'Docusign_Contract/success_sent.html', context)

