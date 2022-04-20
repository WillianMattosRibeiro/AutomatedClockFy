#LANCADOR DE HORAS NO CLOCKFY
from utils.will_utils import init_spark

init_spark("teste")
#
# import json, requests, datetime
#
# base_url = #get_from_json
# time_entry_path = #get_from_json
# credentials = #get_from_json
#
# url = '{}{}'.format(base_url, time_entry_path)
#
# headers = {'X-Api-Key': '{}'.format(credentials),
#            'Content-Type': 'application/json'}
#
# date_now = datetime.datetime.now().strftime("%Y-%m-%d")
#
# first_time = {
#   "start": "{}T12:00:00.000Z".format(date_now),
#   "billable": "true",
#   "description": "BRF e Gestao Squad",
#   "projectId": "5ef21ac043162e08f73ac890",
#   "end": "{}T15:00:00.000Z".format(date_now),
#   "tagIds": [
#      "5e72352dcb758f10a10e61af",
#      "5e723533d5d30e3d6f0a45f5",
#      "5e8f554c3b138c4dc4465c72"
#    ]
# }
#
#
# second_time = {
#   "start": "{}T16:00:00.000Z".format(date_now),
#   "billable": "true",
#   "description": "BRF e Gestao Squad",
#   "projectId": "5ef21ac043162e08f73ac890",
#   "end": "{}T21:00:00.000Z".format(date_now),
#   "tagIds": [
#      "5e72352dcb758f10a10e61af",
#      "5e723533d5d30e3d6f0a45f5",
#      "5e8f554c3b138c4dc4465c72"
#    ]
# }
#
# r = requests.post(url, data=json.dumps(first_time), headers=headers)
# print(r.content)
#
# r = requests.post(url, data=json.dumps(second_time), headers=headers)
# print(r.content)
