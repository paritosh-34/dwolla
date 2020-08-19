import dwollav2
import os
import json
from dotenv import load_dotenv

load_dotenv()

client = dwollav2.Client(
    key=os.environ['DWOLLA_APP_KEY'],
    secret=os.environ['DWOLLA_APP_SECRET'],
    environment='sandbox',  # defaults to 'production'
)
app_token = client.Auth.client()

# https://docs.dwolla.com/#create-a-funding-source-for-an-account
# creating funding source for JAMIIE

# https://docs.dwolla.com/#idempotency-key
# To prevent multiple post req
headers = {
    'Idempotency-Key': '19051a62-3403-11e6-ac61-9e71128cae77'
}


def owner_acc_details():
    r = app_token.get('/')
    indented_json = json.dumps(r.body, indent=4, separators=(',', ': '), sort_keys=True)
    print(indented_json)
    print(r.body['_links']['account']['href'])


def owner_funding_src(request_body):
    r = app_token.post('funding-sources', request_body)
    indented_json = json.dumps(r.body, indent=4, separators=(',', ': '), sort_keys=True)
    print(indented_json)
    print(r.headers['location'])


def get_customers(limit):
    r = app_token.get('customers', {'limit': limit})
    indented_json = json.dumps(r.body, indent=4, separators=(',', ': '), sort_keys=True)
    print(indented_json)


def create_customer(request_body):
    r = app_token.post('customers', request_body)
    indented_json = json.dumps(r.body, indent=4, separators=(',', ': '), sort_keys=True)
    print(indented_json)
    print(r.headers['location'])


def customer_status(url):
    r = app_token.post(url)
    indented_json = json.dumps(r.body, indent=4, separators=(',', ': '), sort_keys=True)
    print(indented_json)
    print(r.body['status'])


def upload_customer_documents(url):
    r = app_token.post('%s/documents' % url, file=open('NewLogo.png', 'rb'), documentType='license')
    indented_json = json.dumps(r.body, indent=4, separators=(',', ': '), sort_keys=True)
    print(indented_json)
    print(r.headers['location'])


# get a iav token valid for 60min
def get_iav_token(url):
    r = app_token.post('%s/iav-token' % url)
    indented_json = json.dumps(r.body, indent=4, separators=(',', ': '), sort_keys=True)
    print(indented_json)
    print(r.body['token'])


def retrieve_funding_src(funding_src):
    r = app_token.get(funding_src)
    indented_json = json.dumps(r.body, indent=4, separators=(',', ': '), sort_keys=True)
    print(indented_json)
    print(r.body['name'])


def initiate_transfer(request_body):
    r = app_token.post('transfers', request_body)
    indented_json = json.dumps(r.body, indent=4, separators=(',', ': '), sort_keys=True)
    print(indented_json)
    print(r.headers['location'])


def mass_payments(request_body):
    r = app_token.post('mass-payments', request_body)
    indented_json = json.dumps(r.body, indent=4, separators=(',', ': '), sort_keys=True)
    print(indented_json)
    print(r.headers['location'])
