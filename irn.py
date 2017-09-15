'''
Project: PayU Turkey IRN API Python3 Sample Code
Author: Göktürk Enez
'''
# Importing required libraries.
from datetime import datetime
import hmac
import hashlib
from urllib.parse import urlencode
from urllib.request import Request, urlopen
import collections
#Endpoint
url = 'https://secure.payu.com.tr/order/irn.php'

#Secret Key
secret = 'SECRET_KEY'

array = collections.OrderedDict()
array['MERCHANT'] = 'OPU_TEST'
array['ORDER_REF'] = '39537992'
array['ORDER_AMOUNT'] = '129.33'
array['ORDER_CURRENCY'] = 'TRY'
array['IRN_DATE'] = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
array['AMOUNT'] = '10'

# Initializing the hashstring @param
hashstring = ''
#Order Directory
# Getting Array @params
for k, v in array.items():
# Adding the UTF-8 byte length of each field value at the beginning of field value
    hashstring += str(len(v)) + str(v)
print(hashstring)

# Calculating signature
signature = hmac.new(secret.encode('utf-8'), hashstring.encode('utf-8'), hashlib.md5).hexdigest()

# Adding signature @param to request array
array['ORDER_HASH'] = signature
print(signature)

# Sending Request to Endpoint
request = Request(url, urlencode(array).encode())
response = urlopen(request).read().decode()

# Printing result/response
print(response)

