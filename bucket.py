COMPUTE_URL_BASE = 'https://www.googleapis.com/compute/v1/'


def GenerateConfig(context):
  """Create instance with disks."""

  datadisk = 'datadisk-'+ context.env['deployment']
  resources = [{
      'type': 'compute.v1.disk',
      'name': datadisk,
      'properties': {
          'zone': context.properties['zone'],
          'sizeGb': 10,
          # Disk type is a full URI.  Example uses pd-standard
          # but pd-ssd can be used as well
          'type': ''.join([COMPUTE_URL_BASE, 'projects/',
                           context.env['project'], '/zones/',
                           context.properties['zone'],
                           '/diskTypes/pd-standard'])
      }
  }, {
      'type': 'compute.v1.instance',
      'name': 'operations-sql-' + context.env['deployment'],
      'properties': {
          'zone': context.properties['zone'],
          'machineType': ''.join([COMPUTE_URL_BASE, 'projects/',
                                  context.env['project'], '/zones/',
                                  context.properties['zone'],
                                  '/machineTypes/n1-standard-4']),
        
          'disks': [{
              'deviceName': 'boot',
              'type': 'PERSISTENT',
              'boot': True,
              'autoDelete': True,
              'initializeParams': {
                  'diskName': 'disk-' + context.env['deployment'],
                  'sourceImage': ''.join([COMPUTE_URL_BASE, 'projects/',
                                          'albatross-keving-sandbox/global/images/adlib-management-sql-image'])}
          }, {
              # Specify the data disk to mount. The deviceName can be anything,
              # but by convention is typically set to the same name.
              # This is the value is used in
              # /dev/disk/by-id/google-<deviceName>.
              # If not set, it will be
              # /dev/disk/by-id/google-persisent-disk-<number>.
              'deviceName': 'datadisk',
              'type': 'PERSISTENT',
              'source': '$(ref.' + datadisk + '.selfLink)',
              'autoDelete': True
          }],
          'networkInterfaces': [{
              'network': ''.join([COMPUTE_URL_BASE, 'projects/',
                                  context.env['project'],
                                  '/global/networks/default']),
              'accessConfigs': [{
                  'name': 'External NAT',
                  'type': 'ONE_TO_ONE_NAT'
              }]
          }]
      }
  }]
  return {'resources': resources}
