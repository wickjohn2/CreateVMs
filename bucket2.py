URL_BASE = 'https://www.googleapis.com/'

def GenerateConfig(context):

  resources = [{
      'type': 'storage.v1.bucket',
      'name': context.env['deployment'],
      'properties': {
        'storageClass': context.properties['storageClass'],
        'location': context.properties['location']
      }
      },
    {
      'type': 'storage.v1.bucketAccessControl',
      'name': '$(ref.' + context.env['deployment'] + '.selfLink)',
      'properties': {
        'acl': context.properties['acl'],
        'bucket': '$(ref.' + context.env['deployment'] + '.selfLink)',
        'entity': context.properties['entity'],
        'role': context.properties['role']
      }
    }
  ]
  return {'resources': resources}
