import time
import urllib

from dcos import emitting, util, mesos, http
from dcos.errors import DefaultError, DCOSException

from dcos_valkiria import constants

logger = util.get_logger(__name__)
emitter = emitting.FlatEmitter()


def set_default_timeout(option):
    if not option:
        return constants.default_timeout
    else:
        return option


def get_ips_list(ips):
    if type(ips) is list:
        return ips
    else:
        try:
            ip_list = ips.replace(" ", "").split(",")
            valid_ips = []
            for ip in ip_list:
                if valid_ip_format(ip):
                    valid_ips.append(ip)
                elif ip == '':
                    emitter.publish(DefaultError("--ips requires argument"))
                else:
                    emitter.publish("[[{}]] invalid ip format.".format(ip))
            return valid_ips
        except AttributeError:
            emitter.publish(DefaultError("--ips requires argument"))
            return 1


def valid_ip_format(addr):
    try:
        address = addr.strip().split(".")
    except AttributeError:
        return False
    try:
        return len(address) == 4 and all(octet.isdigit() and int(octet) < 256 for octet in address)
    except ValueError:
        return False


def get_ips(role):
    try:
        params = {'_timestamp': int(round(time.time() * 1000))}

        return [node[constants.dcos_nodes_host_ip] for node in
                get_url(constants.dcos_nodes_url, params)[constants.dcos_nodes_nodes]
                if node[constants.dcos_nodes_role] == role] if role else \
            [node[constants.dcos_nodes_host_ip] for node in
             get_url(constants.dcos_nodes_url, params)[constants.dcos_nodes_nodes]]

    except DCOSException as e:
        emitter.publish(e)
        return []


def get_url(url, params):
    url = mesos.DCOSClient().get_dcos_url(url)
    return http.get(url, params=params, headers=constants.dcos_nodes_headers, timeout=5).json()


def get_pem_path(pem):
    return '-i {} '.format(pem) if pem else str()
