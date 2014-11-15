#!/usr/bin/python
######################################################################
# Cloud Routes Bridge
# -------------------------------------------------------------------
# Actions Module
######################################################################

import rethinkdb as r
from rethinkdb.errors import RqlRuntimeError, RqlDriverError
import syslog
import json
import requests
import ast


def failed(redata, redata, jdata, rdb, r_server):
    ''' This method will be called when a monitor has failed '''
    run = True
    if "failed" in jdata['check']['prev_status']:
        run = False

    if run:
        result = make_request(jdata, rdb, r_server)
        return result
    else:
        return None


def healthy(redata, jdata, rdb, r_server):
    ''' This method will be called when a monitor has passed '''
    run = True
    if "healthy" in jdata['check']['prev_status']:
        run = False

    if run:
        result = make_request(jdata, redata, rdb, r_server)
        return result
    else:
        return None


def make_request(jdata, redata, rdb, r_server):
    ''' Make the HTTP request '''
    url = redata['url']
    # Parse the headers from a string to
    # header like {'Authorization': 'my-token'}
    if redata['request_headers'] is not None:
        headers = ast.literal_eval(redata['request_headers'])
    else:
        headers = {}
    timeout = 3.00
    if redata['request_type'] == "post":
        body = redata['post_body']
        try:
            result = requests.post(
                url, timeout=timeout, headers=headers, data=body, verify=False)
        except:
            return False
    else:
        try:
            result = requests.get(
                url, timeout=timeout, headers=headers, verify=False)
        except:
            return False
    return True

