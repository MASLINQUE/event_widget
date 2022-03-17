#!/bin/env python3

import json
import requests

resp = requests.get('https://ipinfo.io').text
ipinfo = json.loads(resp)

print("<div class='stat'><h3>"+ipinfo["ip"]+"</h3><span class='subtitle'>"+ipinfo["city"]+"</span></div>")