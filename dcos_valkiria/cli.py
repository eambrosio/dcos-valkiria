"""Description:
    Administer and manage commands in DCOS cluster nodes.

Usage:
    dcos valkiria --info
    dcos valkiria install [--option SSHOPT=VAL ...]
            [--config-file=<path>]
            [--user=<user>]
            [--pem=<path>]
            (--ips=<"ip-or-iplist">)
    dcos valkiria install-agents [--option SSHOPT=VAL ...]
            [--config-file=<path>]
            [--user=<user>]
    dcos valkiria install-masters [--option SSHOPT=VAL ...]
            [--config-file=<path>]
            [--user=<user>]
    dcos valkiria install-all-nodes [--option SSHOPT=VAL ...]
            [--config-file=<path>]
            [--user=<user>]
    dcos valkiria uninstall [--option SSHOPT=VAL ...]
            [--config-file=<path>]
            [--user=<user>]
            (--ips=<"ip-or-iplist">)
    dcos valkiria uninstall-agents [--option SSHOPT=VAL ...]
            [--config-file=<path>]
            [--user=<user>]
    dcos valkiria uninstall-masters [--option SSHOPT=VAL ...]
            [--config-file=<path>]
            [--user=<user>]
    dcos valkiria uninstall-all-nodes [--option SSHOPT=VAL ...]
            [--config-file=<path>]
            [--user=<user>]
    dcos valkiria tasks [--option SSHOPT=VAL ...]
            [--config-file=<path>]
            [--user=<user>]
            [--pem=<path>]
            (--ips=<"ip-or-iplist">)
    dcos valkiria tasks-agents [--option SSHOPT=VAL ...]
            [--config-file=<path>]
            [--user=<user>]
    dcos valkiria tasks-masters [--option SSHOPT=VAL ...]
            [--config-file=<path>]
            [--user=<user>]
    dcos valkiria tasks-all-nodes [--option SSHOPT=VAL ...]
            [--config-file=<path>]
            [--user=<user>]
    dcos valkiria kill [--option SSHOPT=VAL ...]
            [--config-file=<path>]
            [--user=<user>]
            (--ip=<ip-or-hostname>)
            (--task-id=<task-id>)
            [--kill-executor=<kill-executor>]
    dcos valkiria start [--option SSHOPT=VAL ...]
            [--config-file=<path>]
            [--user=<user>]
            (--ips=<"ip-or-iplist">)
    dcos valkiria start-agents [--option SSHOPT=VAL ...]
            [--config-file=<path>]
            [--user=<user>]
    dcos valkiria start-masters [--option SSHOPT=VAL ...]
            [--config-file=<path>]
            [--user=<user>]
    dcos valkiria start-all-nodes [--option SSHOPT=VAL ...]
            [--config-file=<path>]
            [--user=<user>]
    dcos valkiria stop [--option SSHOPT=VAL ...]
            [--config-file=<path>]
            [--user=<user>]
            (--ips=<"ip-or-iplist">)
    dcos valkiria stop-agents [--option SSHOPT=VAL ...]
            [--config-file=<path>]
            [--user=<user>]
    dcos valkiria stop-masters [--option SSHOPT=VAL ...]
            [--config-file=<path>]
            [--user=<user>]
    dcos valkiria stop-all-nodes [--option SSHOPT=VAL ...]
            [--config-file=<path>]
            [--user=<user>]
            (--ips=<"ip-or-iplist">)
    dcos valkiria status [--option SSHOPT=VAL ...]
            [--config-file=<path>]
            [--user=<user>]
            (--ips=<"ip-or-iplist">)
    dcos valkiria status-agents [--option SSHOPT=VAL ...]
            [--config-file=<path>]
            [--user=<user>]
    dcos valkiria status-masters [--option SSHOPT=VAL ...]
            [--config-file=<path>]
            [--user=<user>]
    dcos valkiria status-all-nodes [--option SSHOPT=VAL ...]
            [--config-file=<path>]
            [--user=<user>]

Commands:
    install
        Establish an SSH connection to the master or agent nodes and install Valkiria on them.

    install-agents
        Establish an SSH connection to all agent nodes and install Valkiria on them.

    install-masters
        Establish an SSH connection to all master nodes and install Valkiria on them.

    install-all-nodes
        Establish an SSH connection to all nodes and install Valkiria on them.

    uninstall
        Establish an SSH connection to the master or agent nodes and uninstall Valkiria on them.

    uninstall-agents
        Establish an SSH connection to agent nodes and uninstall Valkiria on them.

    uninstall-agents
        Establish an SSH connection to all agent nodes and uninstall Valkiria on them.

    uninstall-masters
        Establish an SSH connection to all master nodes and uninstall Valkiria on them.

    uninstall-all-nodes
        Establish an SSH connection to all nodes and uninstall Valkiria on them.

    tasks
        Establish an SSH connection to the master or agent nodes and list the killables tasks.

    tasks-agents
        Establish an SSH connection to all agent nodes and list the killables tasks.

    tasks-masters
        Establish an SSH connection to all master nodes and list the killables tasks.

    tasks-all-nodes
        Establish an SSH connection to all nodes and list the killables tasks.

    kill
        Establish an SSH connection to the master or agent nodes and kill the task with a specific taskId.

    start
        Establish an SSH connection to the master or agent nodes and start the Valkiria agent process on them.

    start-agents
        Establish an SSH connection to all agent nodes and start the Valkiria agent process on them.

    start-masters
        Establish an SSH connection to all master nodes and start the Valkiria agent process on them.

    start-all-nodes
        Establish an SSH connection to all nodes and start the Valkiria agent process on them.

    stop
        Establish an SSH connection to the master or agent nodes and stop the Valkiria agent process on them.

    stop-agents
        Establish an SSH connection to all agents nodes and stop the Valkiria agent process on them.

    stop-masters
        Establish an SSH connection to all master nodes and stop the Valkiria agent process on them.

    stop-all-nodes
        Establish an SSH connection to all nodes and stop the Valkiria agent process on them.

    status
        Establish an SSH connection to the master or agent nodes and get the status of the Valkiria agent process on them.

    status-agents
        Establish an SSH connection to all agent nodes and get the status of the Valkiria agent process on them.

    status-masters
        Establish an SSH connection to all master nodes and get the status of the Valkiria agent process on them.

    status-all-nodes
        Establish an SSH connection to all nodes and get the status of the Valkiria agent process on them.


Options:
    -h, --help
        Show this screen.
    --info
        Show a short description of this subcommand.
    --option SSHOPT=VAL
        The SSH options. For information, enter `man ssh_config` in your
        terminal.
    --ips=<"ip-or-iplist">
        Required: The ip list string in format "IP1,IP2..."
    --kill-executor=<kill-executor>
        Select if you want kill the executor (1), their tasks (2) or both of them (0). [default: 0]
    --user=<user>
        The SSH user, where the default user [default: root].
    --pem=<path>
        The PEM path to connect to node(s).
    --ip=<ip-or-hostname>
        The ip where you want to kill the task
    --task-id=<task-id>
        The id of the task that you want to kill.
    --version
        Print version information.
"""
import json
import subprocess
import docopt
import time
from urlparse import urlparse
from dcos import cmds, emitting, util, mesos, http
from dcos.errors import DCOSException, DefaultError
from dcos_valkiria import constants
from prettytable import PrettyTable

logger = util.get_logger(__name__)
emitter = emitting.FlatEmitter()


def main():
    try:
        return _main()
    except DCOSException as e:
        emitter.publish(e)
        return 1


def _main():
    args = docopt.docopt(
        doc=__doc__,
        version="dcos-valkiria version {}".format(constants.version)
    )
    return cmds.execute(_cmds(), args)


def _cmds():
    """
    :returns: All of the supported commands
    :rtype: [Command]
    """
    return [
        cmds.Command(
            hierarchy=['valkiria', '--info'],
            arg_keys=[],
            function=_info),

        cmds.Command(
            hierarchy=['valkiria', 'install'],
            arg_keys=['--ips', '--user', '--option', '--pem', '--config-file'],
            function=_install),

        cmds.Command(
            hierarchy=['valkiria', 'install-agents'],
            arg_keys=['--user', '--option', '--pem', '--config-file'],
            function=_install_agents),

        cmds.Command(
            hierarchy=['valkiria', 'install-masters'],
            arg_keys=['--user', '--option', '--pem', '--config-file'],
            function=_install_masters),

        cmds.Command(
            hierarchy=['valkiria', 'install-all-nodes'],
            arg_keys=['--user', '--option', '--pem', '--config-file'],
            function=_install_all_nodes),

        cmds.Command(
            hierarchy=['valkiria', 'uninstall'],
            arg_keys=['--ips', '--user', '--option', '--pem', '--config-file'],
            function=_uninstall),

        cmds.Command(
            hierarchy=['valkiria', 'uninstall-agents'],
            arg_keys=['--user', '--option', '--pem', '--config-file'],
            function=_uninstall_agents),

        cmds.Command(
            hierarchy=['valkiria', 'uninstall-masters'],
            arg_keys=['--user', '--option', '--pem', '--config-file'],
            function=_uninstall_masters),

        cmds.Command(
            hierarchy=['valkiria', 'uninstall-all-nodes'],
            arg_keys=['--user', '--option', '--pem', '--config-file'],
            function=_uninstall_all_nodes),

        cmds.Command(
            hierarchy=['valkiria', 'tasks'],
            arg_keys=['--ips', '--user', '--option', '--pem', '--config-file'],
            function=_tasks),

        cmds.Command(
            hierarchy=['valkiria', 'tasks-agents'],
            arg_keys=['--user', '--option', '--pem', '--config-file'],
            function=_tasks_agents),

        cmds.Command(
            hierarchy=['valkiria', 'tasks-masters'],
            arg_keys=['--user', '--option', '--pem', '--config-file'],
            function=_tasks_masters),

        cmds.Command(
            hierarchy=['valkiria', 'tasks-all-nodes'],
            arg_keys=['--user', '--option', '--pem', '--config-file'],
            function=_tasks_all_nodes),

        cmds.Command(
            hierarchy=['valkiria', 'kill'],
            arg_keys=['--ip', '--user', '--option', '--pem', '--config-file', '--task-id', '--kill-executor'],
            function=_kill),

        cmds.Command(
            hierarchy=['valkiria', 'start'],
            arg_keys=['--ips', '--user', '--option', '--pem', '--config-file'],
            function=_start),

        cmds.Command(
            hierarchy=['valkiria', 'start-agents'],
            arg_keys=['--user', '--option', '--pem', '--config-file'],
            function=_start_agents),

        cmds.Command(
            hierarchy=['valkiria', 'start-masters'],
            arg_keys=['--user', '--option', '--pem', '--config-file'],
            function=_start_masters),

        cmds.Command(
            hierarchy=['valkiria', 'start-all-nodes'],
            arg_keys=['--user', '--option', '--pem', '--config-file'],
            function=_start_all_nodes),

        cmds.Command(
            hierarchy=['valkiria', 'stop'],
            arg_keys=['--ips', '--user', '--pem', '--option', '--config-file'],
            function=_stop),

        cmds.Command(
            hierarchy=['valkiria', 'stop-agents'],
            arg_keys=['--user', '--option', '--pem', '--config-file'],
            function=_stop_agents),

        cmds.Command(
            hierarchy=['valkiria', 'stop-masters'],
            arg_keys=['--user', '--option', '--pem', '--config-file'],
            function=_stop_masters),

        cmds.Command(
            hierarchy=['valkiria', 'stop-all-nodes'],
            arg_keys=['--user', '--option', '--pem', '--config-file'],
            function=_stop_all_nodes),

        cmds.Command(
            hierarchy=['valkiria', 'status'],
            arg_keys=['--ips', '--user', '--option', '--pem', '--config-file'],
            function=_status),

        cmds.Command(
            hierarchy=['valkiria', 'status-agents'],
            arg_keys=['--user', '--option', '--pem', '--config-file'],
            function=_status_agents),

        cmds.Command(
            hierarchy=['valkiria', 'status-masters'],
            arg_keys=['--user', '--option', '--pem', '--config-file'],
            function=_status_masters),

        cmds.Command(
            hierarchy=['valkiria', 'status-all-nodes'],
            arg_keys=['--user', '--option', '--pem', '--config-file'],
            function=_status_all_nodes)
    ]


def _info():
    """Print node cli information.
    :returns: process return code
    :rtype: int
    """
    emitter.publish("Administer and manage commands in DCOS cluster nodes.")
    return 0


def _install(ips, user, option, pem, config_file):
    """SSH into a DCOS node using the IP addresses to install valkiria
     :param ips: ip to connect
     :type ips: [str]
     :param option: SSH option
     :type option: [str]
     :param user: SSH user
     :type user: str | None
     :param pem: PEM file
     :type pem: [str]
     :rtype: int
     :returns: process return code
     """
    option = _set_default_timeout(option)
    pem_path = _get_pem_path(pem)
    ssh_options = util.get_ssh_options(config_file, option)
    for ip in _get_ips_list(ips):
        cmd = '''ssh {10}{2}{0}@{1} ' if [ ! -d {6} ]; then
                curl -O {3}; tar -xvf {4};
                mkdir -p {6}; cp {5} {6}; rm -rf {7}; rm {4};
                nohup {6}/valkiria a 2> {9} > /dev/null 2>&1 &
                echo $! > {8}
                echo Valkiria was installed successfully
                else
                echo Valkiria is already installed in {1}
                fi ' '''.format(
            user,
            ip,
            ssh_options,
            constants.url_install,
            constants.name,
            constants.previous_path,
            constants.end_path,
            constants.previous_path.split('/')[0],
            constants.pid,
            constants.log,
            pem_path)
        subprocess.call(cmd, shell=True)
    return 0


def _install_agents(user, option, pem, config_file):
    """SSH into all DCOS agent nodes to install valkiria
     :param option: SSH option
     :type option: [str]
     :param user: SSH user
     :type user: str | None
     :param pem: PEM file
     :type pem: [str]
     :rtype: int
     :returns: process return code
     """

    agents = _get_ips('agent')
    _install(ips=agents, user=user, option=option, pem=pem, config_file=config_file)


def _install_masters(user, option, pem, config_file):
    """SSH into all DCOS agent nodes to install valkiria
     :param option: SSH option
     :type option: [str]
     :param user: SSH user
     :type user: str | None
     :param pem: PEM file
     :type pem: [str]
     :rtype: int
     :returns: process return code
     """
    masters = _get_ips('master')
    _install(ips=masters, user=user, option=option, pem=pem, config_file=config_file)


def _install_all_nodes(user, option, pem, config_file):
    """SSH into all DCOS nodes to install valkiria
     :param option: SSH option
     :type option: [str]
     :param user: SSH user
     :type user: str | None
     :param pem: PEM file
     :type pem: [str]
     :rtype: int
     :returns: process return code
     """
    nodes = _get_ips(None)
    _install(ips=nodes, user=user, option=option, pem=pem, config_file=config_file)


def _uninstall(ips, user, option, pem, config_file):
    """SSH into a DCOS node using the IP addresses to uninstall valkiria
     :param ips: ip to connect
     :type ips: [str]
     :param option: SSH option
     :type option: [str]
     :param user: SSH user
     :type user: str | None
     :param pem: PEM file
     :type pem: [str]
     :rtype: int
     :returns: process return code
     """

    for ip in _get_ips_list(ips):
        option = _set_default_timeout(option)
        pem_path = _get_pem_path(pem)
        ssh_options = util.get_ssh_options(config_file, option)
        cmd = '''ssh {9}{2}{0}@{1} ' if [ -d {6} ]; then
                if [ -f ./{7} ]; then pkill -F {7}; rm -rf {7};
                fi
                rm -rf {6}; rm ./{8};
                fi
                echo Valkiria was uninstalled successfully ' '''.format(
            user,
            ip,
            ssh_options,
            constants.url_install,
            constants.name,
            constants.previous_path,
            constants.end_path,
            constants.pid,
            constants.log,
            pem_path)
        subprocess.call(cmd, shell=True)
    return 0


def _uninstall_agents(user, option, pem, config_file):
    """SSH into all DCOS agent nodes to uninstall valkiria
     :param option: SSH option
     :type option: [str]
     :param user: SSH user
     :type user: str | None
     :param pem: PEM file
     :type pem: [str]
     :rtype: int
     :returns: process return code
     """

    agents = _get_ips('agent')
    _uninstall(ips=agents, user=user, option=option, pem=pem, config_file=config_file)


def _uninstall_masters(user, option, pem, config_file):
    """SSH into all DCOS master nodes to uninstall valkiria
     :param option: SSH option
     :type option: [str]
     :param user: SSH user
     :type user: str | None
     :param pem: PEM file
     :type pem: [str]
     :rtype: int
     :returns: process return code
     """

    masters = _get_ips('master')
    _uninstall(ips=masters, user=user, option=option, pem=pem, config_file=config_file)


def _uninstall_all_nodes(user, option, pem, config_file):
    """SSH into all DCOS nodes to uninstall valkiria
     :param option: SSH option
     :type option: [str]
     :param user: SSH user
     :type user: str | None
     :param pem: PEM file
     :type pem: [str]
     :rtype: int
     :returns: process return code
     """

    nodes = _get_ips(None)
    _uninstall(ips=nodes, user=user, option=option, pem=pem, config_file=config_file)


def _start(ips, user, option, pem, config_file):
    """SSH into a DCOS node using the IP addresses to start valkiria agent
    :param ips: ip to connect
    :type ips: [str]
    :param option: SSH option
    :type option: [str]
    :param user: SSH user
    :type user: str | None
    :param pem: PEM file
    :type pem: [str]
    :rtype: int
    :returns: process return code
    """
    option = _set_default_timeout(option)
    pem_path = _get_pem_path(pem)
    ssh_options = util.get_ssh_options(config_file, option)
    for ip in _get_ips_list(ips):
        cmd = '''ssh {6}{2}{0}@{1} 'if [ -f ./{4} ]; then
            echo Valkiria is currently running in {1}
            elif [ ! -f {3} ]; then
                echo Valkiria is currently not installed in {1}
            else
                nohup {3}/valkiria a 2> {5} > /dev/null 2>&1
                echo $! > {4}
            fi' '''.format(
            user,
            ip,
            ssh_options,
            constants.end_path,
            constants.pid,
            constants.log,
            pem_path)
        subprocess.call(cmd, shell=True)
    return 0


def _start_agents(user, option, pem, config_file):
    """SSH into all DCOS agent nodes to start valkiria agent
    :param option: SSH option
    :type option: [str]
    :param user: SSH user
    :type user: str | None
    :param pem: PEM file
    :type pem: [str]
    :rtype: int
    :returns: process return code
    """
    agents = _get_ips('agent')
    _start(ips=agents, user=user, option=option, pem=pem, config_file=config_file)


def _start_masters(user, option, pem, config_file):
    """SSH into all DCOS master nodes to start valkiria agent
    :param option: SSH option
    :type option: [str]
    :param user: SSH user
    :type user: str | None
    :param pem: PEM file
    :type pem: [str]
    :rtype: int
    :returns: process return code
    """
    masters = _get_ips('master')
    _start(ips=masters, user=user, option=option, pem=pem, config_file=config_file)


def _start_all_nodes(user, option, pem, config_file):
    """SSH into all DCOS master nodes to start valkiria agent
    :param option: SSH option
    :type option: [str]
    :param user: SSH user
    :type user: str | None
    :param pem: PEM file
    :type pem: [str]
    :rtype: int
    :returns: process return code
    """
    nodes = _get_ips(None)
    _start(ips=nodes, user=user, option=option, pem=pem, config_file=config_file)


def _stop(ips, user, option, pem, config_file):
    """SSH into a DCOS node using the IP addresses to stop valkiria agent
    :param ips: ip to connect
    :type ips: [str]
    :param option: SSH option
    :type option: [str]
    :param user: SSH user
    :type user: str | None
    :param pem: PEM file
    :type pem: [str]
    :rtype: int
    :returns: process return code
    """
    option = _set_default_timeout(option)
    pem_path = _get_pem_path(pem)
    ssh_options = util.get_ssh_options(config_file, option)
    for ip in _get_ips_list(ips):
        cmd = '''ssh {4}{2}{0}@{1} 'if [ -f ./{3} ]; then pkill -F {3}; rm -rf {3};
            else
                echo Valkiria is currently not running in {1}.
            fi' '''.format(
            user,
            ip,
            ssh_options,
            constants.pid,
            pem_path)
        subprocess.call(cmd, shell=True)
    return 0


def _stop_agents(user, option, pem, config_file):
    """SSH into all DCOS agent nodes to stop valkiria agent
    :param option: SSH option
    :type option: [str]
    :param user: SSH user
    :type user: str | None
    :param pem: PEM file
    :type pem: [str]
    :rtype: int
    :returns: process return code
    """
    agents = _get_ips('agent')
    _stop(ips=agents, user=user, option=option, pem=pem, config_file=config_file)


def _stop_masters(user, option, pem, config_file):
    """SSH into all DCOS master nodes to stop valkiria agent
    :param option: SSH option
    :type option: [str]
    :param user: SSH user
    :type user: str | None
    :param pem: PEM file
    :type pem: [str]
    :rtype: int
    :returns: process return code
    """
    masters = _get_ips('master')
    _stop(ips=masters, user=user, option=option, pem=pem, config_file=config_file)


def _stop_all_nodes(user, option, pem, config_file):
    """SSH into all DCOS nodes to stop valkiria agent
    :param option: SSH option
    :type option: [str]
    :param user: SSH user
    :type user: str | None
    :param pem: PEM file
    :type pem: [str]
    :rtype: int
    :returns: process return code
    """
    nodes = _get_ips(None)
    _stop(ips=nodes, user=user, option=option, pem=pem, config_file=config_file)


def _status(ips, user, option, pem, config_file):
    """SSH into a DCOS node using the IP addresses to check valkiria agent status
    :param ips: ip to connect
    :type ips: [str]
    :param option: SSH option
    :type option: [str]
    :param user: SSH user
    :type user: str | None
    :param pem: PEM file
    :type pem: [str]
    :rtype: int
    :returns: process return code
    """
    option = _set_default_timeout(option)
    pem_path = _get_pem_path(pem)
    ssh_options = util.get_ssh_options(config_file, option)
    for ip in _get_ips_list(ips):
        cmd = '''ssh {5}{2}{0}@{1} 'if [ ! -f ./{4} ]; then
            echo Valkiria is currently stopped in {1}
            else
            echo Valkiria is currently running in {1}
            fi' '''.format(
            user,
            ip,
            ssh_options,
            constants.end_path,
            constants.pid,
            pem_path)
        subprocess.call(cmd, shell=True)
    return 0


def _status_agents(user, option, pem, config_file):
    """SSH into all DCOS agent nodes to check valkiria agent status
    :param option: SSH option
    :type option: [str]
    :param user: SSH user
    :type user: str | None
    :param pem: PEM file
    :type pem: [str]
    :rtype: int
    :returns: process return code
    """
    agents = _get_ips('agent')
    _status(ips=agents, user=user, option=option, pem=pem, config_file=config_file)


def _status_masters(user, option, pem, config_file):
    """SSH into all DCOS master nodes to check valkiria agent status
    :param option: SSH option
    :type option: [str]
    :param user: SSH user
    :type user: str | None
    :param pem: PEM file
    :type pem: [str]
    :rtype: int
    :returns: process return code
    """
    masters = _get_ips('master')
    _status(ips=masters, user=user, option=option, pem=pem, config_file=config_file)


def _status_all_nodes(user, option, pem, config_file):
    """SSH into all DCOS nodes to check valkiria agent status
    :param option: SSH option
    :type option: [str]
    :param user: SSH user
    :type user: str | None
    :param pem: PEM file
    :type pem: [str]
    :rtype: int
    :returns: process return code
    """
    nodes = _get_ips(None)
    _status(ips=nodes, user=user, option=option, pem=pem, config_file=config_file)


def _tasks(ips, user, option, pem, config_file):
    """SSH into a DCOS node using the IP addresses to list all tasks
    :param ips: ip to connect
    :type ips: [str]
    :param option: SSH option
    :type option: [str]
    :param user: SSH user
    :type user: str | None
    :param pem: PEM file
    :type pem: [str]
    :param pem: PEM file
    :type pem: [str]
    :rtype: int
    :returns: process return code
    """
    option = _set_default_timeout(option)
    pem_path = _get_pem_path(pem)
    ssh_options = util.get_ssh_options(config_file, option)
    table = PrettyTable(['Ip', 'TaskId', 'ServiceType', 'FrameWork'])
    for ip in _get_ips_list(ips):
        cmd = '''ssh {4}{2}{0}@{1} 'curl -sb -H {3}' '''.format(
            user,
            ip,
            ssh_options,
            constants.url_list,
            pem_path)
        try:
            resp = json.loads(subprocess.check_output(cmd, shell=True).decode('utf-8'))
            services_type_without_tasks = 0
            for service_type in constants.services_type:
                try:
                    xs = resp[service_type]
                    for x in xs:
                        if service_type == 'daemon':
                            table.add_row([ip, x['Name'], service_type, '----'])
                        elif service_type == 'service':
                            table.add_row([ip, x['TaskName'], service_type, x['FrameWorkId']])
                        elif service_type == 'docker':
                            table.add_row([ip, x['TaskName'], service_type, x['FrameWorkName']])
                except KeyError:
                    if services_type_without_tasks == 2:
                        table.add_row([ip, 'No tasks running', '----', '----'])
                    else:
                        services_type_without_tasks += 1
        except subprocess.CalledProcessError:
            table.add_row([ip, 'IP not valid', '----', '----'])
    return table


def _tasks_agents(user, option, pem, config_file):
    """SSH into all DCOS agent nodes to list all tasks
     :param option: SSH option
     :type option: [str]
     :param user: SSH user
     :type user: str | None
     :param pem: PEM file
     :type pem: [str]
     :rtype: int
     :returns: process return code
    """
    agents = _get_ips('agent')
    _tasks(ips=agents, user=user, option=option, pem=pem, config_file=config_file)


def _tasks_masters(user, option, pem, config_file):
    """SSH into all DCOS master nodes to list all tasks
     :param option: SSH option
     :type option: [str]
     :param user: SSH user
     :type user: str | None
     :param pem: PEM file
     :type pem: [str]
     :rtype: int
     :returns: process return code
    """
    masters = _get_ips('master')
    _tasks(ips=masters, user=user, option=option, pem=pem, config_file=config_file)


def _tasks_all_nodes(user, option, pem, config_file):
    """SSH into all DCOS nodes to list all tasks
     :param option: SSH option
     :type option: [str]
     :param user: SSH user
     :type user: str | None
     :param pem: PEM file
     :type pem: [str]
     :rtype: int
     :returns: process return code
    """
    nodes = _get_ips(None)
    _tasks(ips=nodes, user=user, option=option, pem=pem, config_file=config_file)


def _kill(ip, user, option, pem, config_file, task_id, kill_executor):
    """SSH into a DCOS node using the IP addresses to kill a given task
     :param ip: ip to connect
     :type ip: [str]
     :param option: SSH option
     :type option: [str]
     :param user: SSH user
     :type user: str | None
     :param pem: PEM file
     :type pem: [str]
     :rtype: int
     :returns: process return code
    """
    option = _set_default_timeout(option)
    pem_path = _get_pem_path(pem)
    ssh_options = util.get_ssh_options(config_file, option)
    table = PrettyTable(header=False)
    kill_options = "'{" + ''' "name":"{0}","killExecutor":{1},"serviceType":0 '''.format(task_id,
                                                                                         kill_executor).replace(
        "\"", "\\\"") + "}'"
    if _valid_ip_format(ip):
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


def _set_default_timeout(option):
    if not option:
        return constants.default_timeout
    else:
        return option


def _get_ips_list(ips):
    """
    Convert argument ips in a iterable list of ips.
    :param ips: ip to connect
    :rtype: ips: str
    """
    if type(ips) is list:
        return ips
    else:
        try:
            ip_list = ips.replace(" ", "").split(",")
            valid_ips = []
            for ip in ip_list:
                if _valid_ip_format(ip):
                    valid_ips.append(ip)
                elif ip == '':
                    emitter.publish(DefaultError("--ips requires argument"))
                else:
                    emitter.publish("[[{}]] invalid ip format.".format(ip))
            return valid_ips
        except AttributeError:
            emitter.publish(DefaultError("--ips requires argument"))
            return 1


def _valid_ip_format(addr):
    try:
        addr = addr.strip().split(".")
    except AttributeError:
        return False
    try:
        return len(addr) == 4 and all(octet.isdigit() and int(octet) < 256 for octet in addr)
    except ValueError:
        return False


# def _get_agents_ips():
#     return [slave['hostname'] for slave in mesos.DCOSClient().get_state_summary()['slaves']]
#


def _get_ips(role):
    url = urlparse(mesos.DCOSClient().get_dcos_url('system/health/v1/nodes')).geturl()
    params = {'_timestamp': int(round(time.time() * 1000))}
    headers = {'Content-Type': 'application/json'}

    # if role:
    return [node['host_ip'] for node in http.get(url, params=params, headers=headers, timeout=5).json()['nodes']
            if node['role'] == role] if role else \
        [node['host_ip'] for node in http.get(url, params=params, headers=headers, timeout=5).json()['nodes']]
    # else:
    #     return [node['host_ip'] for node in http.get(url, params=params, headers=headers, timeout=5).json()['nodes']]


# def _get_masters_ips():
#     client = mesos.DCOSClient()
#     parse_url = urlparse(client.get_dcos_url('cluster/latest'))
#     url = parse_url._replace(netloc=parse_url.hostname + ':4443').geturl()
#     params = {'_timestamp': int(round(time.time() * 1000))}
#     headers = {'Content-Type': 'application/json'}
#
#     return [master['hostname'] for master in http.get(url, params=params, headers=headers, timeout=5).json()['nodes']
#             if master['role'] == 'master']


def _get_pem_path(pem):
    pem_path = ' '

    if pem:
        pem_path += '-i {} '.format(pem)

    return pem_path


if __name__ == "__main__":
    main()
