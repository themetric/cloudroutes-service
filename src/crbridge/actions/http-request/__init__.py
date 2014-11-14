#!/usr/bin/python
######################################################################
# Cloud Routes Bridge
# -------------------------------------------------------------------
# Actions Module
######################################################################

import rethinkdb as r
from rethinkdb.errors import RqlRuntimeError, RqlDriverError
import syslog
import time
import datetime
import json


def failed(redata, jdata, rdb, r_server):
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
        result = make_request(jdata, rdb, r_server)
        return result
    else:
        return None


def make_request(jdata, rdb, r_server):

