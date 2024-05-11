#!/usr/bin/env python
"""Update the Beeminder goal 'curfew' and shut down the system."""
import datetime
import os
import subprocess

import requests

offset_ago = datetime.datetime.now(datetime.UTC) - datetime.timedelta(hours=4)
date = offset_ago.date()
hours = offset_ago.timestamp() / 60 / 60 % 24
token = os.environ["BEEMINDER_TOKEN"]
parameters = {"auth_token": token, "requestid": str(date), "value": hours}
ENDPOINT = "https://www.beeminder.com/api/v1/users/me/goals/curfew/datapoints.json"
requests.post(ENDPOINT, parameters, timeout=60)
subprocess.run(["/usr/sbin/shutdown"], check=True)
