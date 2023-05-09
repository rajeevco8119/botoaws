import json
import openpyxl
from string import ascii_uppercase as asc

wb = openpyxl.load_workbook('new_wb.xlsx')
xls_data = wb['AmStack']

key = 2


def isEmpty(resource):
    if len(resource) == 0:
        return True
    return False


def get_deploy(key):
    f = open('all.json')
    key = 2
    data = json.load(f)
    deploy = {}
    total_deploy = []
    for item in data['items']:
        i = 66
        if item['kind'] in ['Deployment','Daemonset', 'StatefulSet', 'Job']:
            key += 1
            i = 66
            xls_data[str(chr(i)) + str(key)] = str(item['metadata']['name'])
            i += 1
            xls_data[str(chr(i)) + str(key)] = str(item['metadata']['namespace'])
            i += 1
            xls_data[str(chr(i)) + str(key)] = str(item['kind'])
            i += 1

            for item1 in item['spec']['template']['spec']['containers']:

                xls_data[str(chr(i)) + str(key)] = str(item['kind'])
                xls_data[str(chr(i)) + str(key)] = str(item['metadata']['name'])
                xls_data[str(chr(i)) + str(key)] = str(item['metadata']['namespace'])
                xls_data[str(chr(i)) + str(key)] = str(item1['name'])
                xls_data[str(chr(i+1)) + str(key)] = str(item1['image'].split('/')[-1])
                if len(item['spec']['template']['spec']['containers']) > 1:
                    key += 1

                resources = item1['resources']
                limit_cpu = 'na'
                limit_memory = 'na'
                request_cpu = 'na'
                request_memory = 'na'
                if resources.keys() is not None and 'limits' in resources:
                    if 'cpu' in resources['limits']:
                        limit_cpu = resources['limits']['cpu']
                    if 'memory' in resources['limits']:
                        limit_memory = resources['limits']['memory']

                    xls_data[str(chr(i + 2)) + str(key)] = str(limit_cpu)
                    xls_data[str(chr(i + 3)) + str(key)] = str(limit_memory)

                else:
                    continue

                if resources.keys() is not None and 'requests' in resources:
                    if 'cpu' in resources['requests']:
                        request_cpu = resources['requests']['cpu']
                    if 'memory' in resources['requests']:
                        request_memory = resources['requests']['memory']

                    xls_data[str(chr(i + 4)) + str(key)] = str(request_cpu)
                    xls_data[str(chr(i + 5)) + str(key)] = str(request_memory)
                else:
                    continue

get_deploy(key)

wb.save('new_wb.xlsx')

##############################################################################################################################


































# def get_daemonset():
#     f = open('sample_deploy.json')
#     data = json.load(f)
#     ds = []
#     daemonset = {}
#     for item in data['items']:
#         if item['kind'] == str('DaemonSet'):
#             daemonset['kind'] = str(item['kind'])
#             daemonset['Name'] = str(item['metadata']['name'])
#             daemonset['Namespace'] = str(item['metadata']['namespace'])
#             daemonset['Containers'] = []
#
#             for item1 in item['spec']['template']['spec']['containers']:
#                 try:
#                     daemonset['Containers'].append(item1['name'])
#                 except:
#                     pass
#         print(daemonset)
#
#
#
# # get_daemonset()
#
#
# def get_stateful_sets():
#     f = open('sample_deploy.json')
#     data = json.load(f)
#     statefulset = {}
#     sts = []
#     for item in data['items']:
#         if item['kind'] == str('StatefulSet'):
#             statefulset['kind'] = str(item['kind'])
#             statefulset['Name'] = str(item['metadata']['name'])
#             statefulset['Namespace'] = str(item['metadata']['namespace'])
#             statefulset['Containers'] = []
#             statefulset['Resources'] = []
#
#             for item1 in item['spec']['template']['spec']['containers']:
#                 try:
#                     statefulset['Containers'].append(item1['name'])
#                     if isEmpty(item1['resources']):
#                         continue
#                     else:
#                         statefulset['Resources'].append(item1['resources'])
#                 except:
#                     continue
#             print(statefulset)
#
#
# # get_stateful_sets()
#
# def get_resources():
#     f = open('sample_deploy.json')
#     data = json.load(f)
#     params = {}
#     limit_cpu = 'na'
#     limit_memory = 'na'
#     request_cpu = 'na'
#     request_memory = 'na'
#     for item in data['items']:
#         new_item = item['spec']['template']['spec']['containers']
#         for res in new_item:
#             resources = res['resources']
#
#             if resources.keys() is not None and 'limits' in resources:
#                 # print(resources['limits'])
#                 if 'cpu' in resources['limits']:
#                     limit_cpu = resources['limits']['cpu']
#                 if 'memory' in resources['limits']:
#                     limit_cpu = resources['limits']['memory']
#
#                 print(limit_cpu)
#                 print(limit_memory)
#             else:
#                 print('This resource has no limit function')
#
#             if resources.keys() is not None and 'requests' in resources:
#                 if 'cpu' in resources['requests']:
#                     request_cpu = resources['requests']['cpu']
#                 if 'memory' in resources['requests']:
#                     request_memory = resources['requests']['memory']
#                 print(request_cpu)
#                 print(request_memory)
#             else:
#                 print('This resource has no requests function')

# get_resources()


# def test():
#     f = open('sample_deploy.json')
#     data = json.load(f)
#     deploy['Containers'] = []
#     deploy['limit-cpu'] = ''
#     deploy['limit-memory'] = ''
#     deploy['request-cpu'] = ''
#     deploy['request-memory'] = ''
#
#     for item in data['items']:
#         for item1 in item['spec']['template']['spec']['containers']:
#             deploy['Containers'].append(item1['name'])
#             try:
#
#                 if isEmpty(item1['resources']):
#                     continue
#                 else:
#                     deploy['limit-cpu'].append(item1['resources']['limits']['cpu'])
#                     deploy['limit-memory'].append(item1['resources']['limits']['memory'])
#                     deploy['request-cpu'].append(item1['resources']['requests']['cpu'])
#                     deploy['request-memory'].append(item1['resources']['requests']['memory'])
#             except:
#                 deploy['limit-cpu'].append('na')
#                 deploy['limit-memory'].append('na')
#                 deploy['request-cpu'].append('na')
#                 deploy['request-memory'].append('na')
#
#     print(deploy['limit-cpu'])
#     print(deploy['limit-memory'])
#     print(deploy['request-cpu'])
#     print(deploy['request-memory'])
#
#     # deploy['Containers'].append(1)
#     # print(deploy)
#
# # test()
