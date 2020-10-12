from utilFunctions import *

# change these urls according to yours...
jamiie_account_url = 'https://api-sandbox.dwolla.com/accounts/6b9567e8-825a-4198-be03-e0ee875459ea'
jamiie_funding_src = "https://api-sandbox.dwolla.com/funding-sources/5d09b038-c2a3-4f29-a7ac-6b9559f75043"
customer_url = 'https://api-sandbox.dwolla.com/customers/6c15acaf-3a13-483f-8d03-dfb3915d4a68'
customer_url2 = "https://api-sandbox.dwolla.com/customers/8fec57ed-03b0-4395-a7ac-89d51a079494"
document_url = 'https://api-sdandbox.dwolla.com/documents/b20b6cc1-fb1c-48aa-b699-ef3d0d892175'
funding_src = "https://api-sandbox.dwolla.com/funding-sources/5f13bbbf-39ff-4810-b104-130dba75c832"

jamiie_account = {
    'routingNumber': '222222226',
    'accountNumber': '123456789',
    'bankAccountType': 'checking',
    'name': 'My Bank'
}

customer_details = request_body = {
    'firstName': 'Batisddhah',
    'lastName': 'Paritoddshah2',
    'email': 'sdsdg22@gmfail.com',
    'type': 'personal',
    'address1': '99-99 33rd St',
    'city': 'Some City',
    'state': 'NY',
    'postalCode': '11101',
    'dateOfBirth': '1970-01-01',
    # For the first attempt, only the
    # last 4 digits of SSN required
    # If the entire SSN is provided,
    # it will still be accepted
    'ssn': '1224'
}

# https://docs.dwolla.com/#transfers
# details for request json
transfer_body = {
    '_links': {
        'source': {
            'href': jamiie_funding_src
        },
        'destination': {
            'href': funding_src
        }
    },
    'amount': {
        'currency': 'USD',
        'value': '1.00'
    },
    'clearing': {
        'destination': 'next-available'
    }
}

mass_payment_body = {
    '_links': {
        'source': {
            'href': jamiie_funding_src
        }
    },
    'clearing': {
        'source': 'standard'
    },
    'items': [
        {
            '_links': {
                'destination': {
                    'href': customer_url
                }
            },
            'amount': {
                'currency': 'USD',
                'value': '1.00'
            },
            'clearing': {
                'destination': 'next-available'
            },
            'metadata': {
                'payment1': 'payment1'
            },
        },
        {
            '_links': {
                'destination': {
                    'href': customer_url2
                }
            },
            'amount': {
                'currency': 'USD',
                'value': '5.00'
            },
            'clearing': {
                'destination': 'next-available'
            },
        }
    ],
    'metadata': {
        'batch1': 'batch1'
    },
}

## Setup owner account
# owner_acc_details()
# owner_funding_src(jamiie_account)
# get_owner_funding_src(jamiie_account_url)
# initiate_micro_deposits(jamiie_funding_src)
# verify_micro_deposits(jamiie_funding_src)


## Setting up customer
# create_customer(customer_details)
# customer_status(customer_url)
# get_customers(10)
# upload_customer_documents(customer_url, "https://jamiie-user-images.s3.amazonaws.com/DocumentImages/919816456565.jpg", "license")
# get_iav_token(customer_url)
# retrieve_funding_src(funding_srdwc)
# initiate_transfer(transfer_body)

## Mass payments
mass_payments(mass_payment_body)
