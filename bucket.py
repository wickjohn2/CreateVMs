URL_BASE = 'https://www.googleapis.com/'

def GenerateConfig(context):

  resources = [{
      'type': 'storage.v1.bucket',
      'name': name,
      'properties': {
        'storageClass': ,
        'acl': 
      }
  }]
  return {'resources': resources}
