#! /usr/bin/env python
"""
Establish an SSH connection to the master or agent nodes and kill the task with a specific taskId.

usage: valkiria kill [options] (--ip=<ip-or-hostname>) (--task-id=<task-id>)
                    [--kill-executor=<kill-executor>]

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
    --ip=<ip-or-hostname>
        IP address or hostname to connect


Specific tasks actions:
    --kill-executor=<kill-executor> Select if you want kill the executor (1),
                                    their tasks (2)
                                    or both of them (0). [default: 0]
    --task-id=<task-id>             The id of the task that you want to kill.

See 'valkiria kill help' for more information.

"""

import json
import subprocess

from dcos import util, emitting
from dcos.errors import DefaultError
from docopt import docopt
from prettytable import PrettyTable

from dcos_valkiria import constants
from dcos_valkiria.utils import set_default_timeout, get_pem_path, valid_ip_format

logger = util.get_logger(__name__)
emitter = emitting.FlatEmitter()


def _kill(ip, user, option, pem, config_file, task_id, kill_executor):
    """SSH into a DCOS node using the IP addresses to kill a given task
    """
    option = set_default_timeout(option)
    pem_path = get_pem_path(pem)
    ssh_options = util.get_ssh_options(config_file, option)
    table = PrettyTable(header=False)
    kill_options = "'{" + ''' "name":"{0}","killExecutor":{1},"serviceType":0 '''. \
        format(task_id, kill_executor).replace("\"", "\\\"") + "}'"
    if valid_ip_format(ip):
        cmd = '''ssh {4}{2}{0}@{1} "curl  -sb -H -X POST -d {3} http://127.0.0.1:9050/api/v1/valkiria " '''.format(
            user,
            ip,
            ssh_options,
            kill_options,
            pem_path)
        try:
            resp = json.loads(subprocess.check_output(cmd, shell=True).decode('utf-8'))
            if resp['status'] == 'Success':
                table.add_row([ip, task_id, constants.killed_message, resp['process'][0]['ChaosTimeStamp']])
            elif task_id == '':
                emitter.publish(DefaultError("--task-id parameter is required"))
                return 1
            else:
                table.add_row([ip, task_id, constants.task_not_found, '----'])
        except subprocess.CalledProcessError:
            emitter.publish(DefaultError('There is no such IP in the cluster'))
            return 1
        return table
    else:
        emitter.publish("[[{}]] invalid ip format.".format(ip))


def main():
    args = docopt(
        __doc__,
        version='valkiria kill')

    nodes = args['--ips']
    user = args['--user']
    option = args['--option']
    pem = args['--pem']
    config_file = args['--config-file']
    task_id = args['--task-id']
    kill_executor = args['--kill-executor']

    return _kill(ips=nodes, user=user, option=option, pem=pem, config_file=config_file, task_id=task_id,
                 kill_executor=kill_executor)


    # else:
    #     print(__doc__)


if __name__ == '__main__':
    main()
