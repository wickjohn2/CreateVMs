URL_BASE = 'https://www.googleapis.com/'

def GenerateConfig(context):

  resources = [{
      'type': 'storage.v1.bucket',
      'name': bucket('name'),
      'properties': {
        'storageClass': 'regional',
        'region': bucket(region),
        'acl': [owner.example@googlegroups.com, writer.test@googlegroups.com]
      }
  }]
  return {'resources': resources}
