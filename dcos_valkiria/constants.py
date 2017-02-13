version = '0.1.1-RC1-SNAPSHOT'
valkiria_version = '0.1.1-RC1-SNAPSHOT'
"""DCOS valkiria version"""
url_install = 'http://sodio.stratio.com/nexus/content/sites/paas/valkiria/{0}/valkiria-{0}.tar.gz'.format(valkiria_version)
url_list = 'http://127.0.0.1:9050/api/v1/list'
name = 'valkiria-{0}.tar.gz'.format(valkiria_version)
previous_path = 'valkiria'
end_path = '/opt/stratio/valkiria'
services_type = ['daemon', 'docker', 'service']
default_timeout = ['ConnectTimeout=10']
killed_message = 'TASK_KILLED'
task_not_found = 'TASK NOT FOUND'
pid = 'valkiria.pid'
log = 'valkiria.log'

dcos_nodes_url = 'system/health/v1/nodes'
dcos_nodes_headers = {'Content-Type': 'application/json'}
dcos_nodes_host_ip = 'host_ip'
dcos_nodes_nodes = 'nodes'
dcos_nodes_role = 'role'
