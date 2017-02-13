#! /usr/bin/env python
"""
Establish an SSH connection to the master or agent nodes and list all killable tasks.

usage: valkiria tasks [options] [-a|--agents] [-m|--masters] [--all] [--ips=<ip-or-list>]

Generic options:
    --pem=<path>
        The PEM path to connect to node(s).
    --user=<user>
        The SSH user, where the default user [default: root].
    --option <ssh-opt=value>
        The SSH options. For information, enter `man ssh_config` in your terminal.
    --help, -h
        Show command help.
    --config-file=<path>
        Path to config file for ssh connection.
    --ips=<ip-iplist>
        List of IP addresses to connect
    --filter=<framework-id>
        FrameworkId or Name to filter by

Specific tasks actions:
    -a, --agents    list all killable tasks in all agent nodes.
    -m, --masters   list all killable tasks in all master nodes.
    --all           list all killable tasks in all nodes.

See 'valkiria tasks help' for more information.

"""

import json
import re
import subprocess

from dcos import util
from docopt import docopt
from prettytable import PrettyTable

from dcos_valkiria import constants
from dcos_valkiria.utils import set_default_timeout, get_pem_path, get_ips_list, get_ips


def _tasks(ips, user, option, pem, config_file):
    """SSH into a DCOS node using the IP addresses to list all tasks
    """
    option = set_default_timeout(option)
    pem_path = get_pem_path(pem)
    ssh_options = util.get_ssh_options(config_file, option)
    nodes_info = list()
    for ip in get_ips_list(ips):
        cmd = '''ssh {4}{2}{0}@{1} 'curl -sb -H {3}' '''.format(
            user,
            ip,
            ssh_options,
            constants.url_list,
            pem_path)
        try:
            resp = json.loads(subprocess.check_output(cmd, shell=True).decode('utf-8'))
            nodes_info.append((True, ip, resp))
        except subprocess.CalledProcessError:
            nodes_info.append((False, ip, None))
    return nodes_info


def _print_table(nodes_info, _filter):
    table = PrettyTable(['Ip', 'TaskId', 'ServiceType', 'FrameWork'])
    services_type_without_tasks = 0
    for node_info in nodes_info:
        for service_type in constants.services_type:
            try:
                if node_info[0]:
                    _add_row(node_info, service_type, table, _filter)
                else:
                    table.add_row([node_info[1], 'IP not valid', '----', '----'])
            except KeyError:
                if services_type_without_tasks == 2:
                    table.add_row([node_info[1], 'No tasks running', service_type, '----'])
                else:
                    services_type_without_tasks += 1
    return table


def _add_row(node, service_type, table, _filter):
    tasks = node[2][service_type]
    for task in tasks:
        _filter_info(node[1], service_type, table, task, _filter)


def _filter_info(ip, service_type, table, task, _filter):
    regex = re.compile('%s' % _filter)

    if service_type == 'daemon':
        if (not _filter) or (_filter and regex.search(task['Name'])):
            table.add_row([ip, task['Name'], service_type, '----'])
    elif service_type == 'service':
        if (not _filter) or (_filter and (regex.search(task['TaskName']) or regex.search(
                task['FrameWorkId']))):
            table.add_row([ip, task['TaskName'], service_type, task['FrameWorkId']])
    elif service_type == 'docker':
        if (not _filter) or (_filter and (regex.search(task['TaskName']) or regex.search(task['FrameWorkName']))):
            table.add_row([ip, task['TaskName'], service_type, task['FrameWorkName']])


def _tasks_agents(user, option, pem, config_file):
    agents = get_ips('agent')
    return _tasks(ips=agents, user=user, option=option, pem=pem, config_file=config_file)


def _tasks_masters(user, option, pem, config_file):
    masters = get_ips('master')
    return _tasks(ips=masters, user=user, option=option, pem=pem, config_file=config_file)


def _tasks_all_nodes(user, option, pem, config_file):
    nodes = get_ips(None)
    return _tasks(ips=nodes, user=user, option=option, pem=pem, config_file=config_file)


def main():
    args = docopt(
        __doc__,
        version='valkiria task')

    nodes = args['--ips']
    user = args['--user']
    option = args['--option']
    pem = args['--pem']
    config_file = args['--config-file']
    filter_by = args['--filter']

    if nodes:
        nodes_info = _tasks(ips=nodes, user=user, option=option, pem=pem, config_file=config_file)
        return _print_table(nodes_info, _filter=filter_by)
    elif args['--agents']:
        nodes_info = _tasks_agents(user=user, option=option, pem=pem, config_file=config_file)
        return _print_table(nodes_info, _filter=filter_by)
    elif args['--masters']:
        nodes_info = _tasks_masters(user=user, option=option, pem=pem, config_file=config_file)
        return _print_table(nodes_info, _filter=filter_by)
    elif args['--all']:
        nodes_info = _tasks_all_nodes(user=user, option=option, pem=pem, config_file=config_file)
        return _print_table(nodes_info, _filter=filter_by)
    else:
        print(__doc__)


if __name__ == '__main__':
    main()
