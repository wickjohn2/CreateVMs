URL_BASE = 'https://www.googleapis.com/'

def GenerateConfig(context):

  resources = [{
      'type': 'storage.v1.bucket',
      'name': context.env['deployment'],
      'properties': {
        'storageClass': context.properties['storageClass'],
        'region': context.properties['region'],
        'acl': context.properties['acl']
      }
  }]
  return {'resources': resources}
