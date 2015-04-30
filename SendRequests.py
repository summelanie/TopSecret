#-------------------------------------------------------------------------------
# Name:        SendRequests.py
# Purpose:     Send get and post requests through a single function.
#
# Author:      Melanie Summers
#
# Created:     30/04/2015
#-------------------------------------------------------------------------------


import requests


def sendRequests(URL, token, requestType='get',data={}):
    '''Sends the defined request, post or get, using the requests
    module with the data provided if post is specified.

    Data should be input as a dictionary'''

    if requestType == 'get':
        data = "&".join(['%s=%s' %(item, data[item]) for item in data])
        URL = "{}?f=json&token={}&{}".format(URL, token, data)
        return requests.get(URL).json()

    elif requestType =='post':
        data['f'] = 'json'
        data['token'] = token
        return requests.post(URL, data=data).json()

    else:
        print("THE REQUEST WAS NOT SENT: Request type must be get or post")


if __name__ == '__main__':

    URL = 'http://www.arcgis.com/sharing/rest/community/self'
    token = 'fTWSGobmk0nkHktwRgPP4oSMun0hFWBQcnBvac9B-ag8jZdFYJ3LCPo1Hu_dFq_reTyvLW4XsyxEudmoUkgokZb2UuF_QE7kJ1S92Jb8KGNxeK10DLNx_yEnXwc9iqOKxWD4YlOaLHQQ29sD0QIzrfpOg32G6NMJENxKhRD3APzL4MoNMeGfs1ZPrnij4t5O'

    get = sendRequests(URL, token, 'get', {'TL':'melanie', 'AL': 'kelly','number': 24})
    post = sendRequests(URL, token, 'post', {'TL':'melanie', 'AL': 'kelly','number': 24})



