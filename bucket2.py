URL_BASE = 'https://www.googleapis.com/'

def GenerateConfig(context):

  resources = [{
      'type': 'storage.v1.bucket',
      'name': context.env['deployment'],
      'properties': {
        'storageClass': context.properties['storageClass'],
        'location': context.properties['location'],
        'defaultObjectAcl': context.properties['defaultObjectAcl']
      }
    }
  ]
  return {'resources': resources}
