from tomato import cmd_ext
from tomato import cmd_origin


def cmd_remote(cmd, username, password, ip, port=22):
    """
    执行远程命令
    :param str cmd: linux cmd
    :param str username: ssh username
    :param str password: ssh password
    :param str ip: ssh host
    :param int port: ssh port
    :return tuple of flag('success','failure'), message
    """
    cmd_origin.cmd_remote(cmd, username, password, ip, port)


def cmd_remote_args(cmd, username, password, ip, args, finish_match=None, port=22):
    """
    交互式执行远程命令; 注意：只有ubuntu 16测试过.
    :param str cmd: linux cmd
    :param str username: ssh username
    :param str password: ssh password
    :param str ip: ssh host
    :param list args: cmd args
    :param str finish_match: key word flag that cmd finish
    :param int port: ssh port
    :return tuple of flag('success','failure'), message
    """
    cmd_origin.cmd_remote_args(cmd, username, password, ip, args, finish_match, port)


def cmds_remote(cmds, username, password, ip, port=22):
    """
    执行远程命令
    :param list cmds: linux cmds
    :param str username: ssh username
    :param str password: ssh password
    :param str ip: ssh host
    :param int port: ssh port
    :return list of tuple of flag('success','failure'), message
    """
    cmd_origin.cmds_remote(cmds, username, password, ip, port)


def put_remote(username, password, ip, local_file, remote_file, port=22):
    """
    执行远程复制
    :param str username: ssh username
    :param str password: ssh password
    :param str ip: ssh host
    :param str local_file: local file abs path
    :param str remote_file: remote file abs path
    :param int port: ssh port
    :return tuple of flag('success','failure'), message
    """
    cmd_origin.put_remote(username, password, ip, local_file, remote_file, port)


def cmd_remotes(cmd, remotes):
    """
    执行远程命令
    :param str cmd: linux cmd
    :param list remotes: list for remote object
    :return list of tuple of flag
    """
    cmd_ext.cmd_remotes(cmd, remotes)


def cmd_remotes_args(cmd, remotes, args, finish_match=None):
    """
    执行远程命令
    :param str cmd: linux cmd
    :param list remotes: remote object
    :param list args: cmd args
    :param str finish_match: key word flag that cmd finish
    :return list of tuple of flag
    """
    cmd_ext.cmd_remotes_args(cmd, remotes, args, finish_match)


def cmds_remotes(cmds, remotes):
    """
    执行远程命令
    :param list cmds: linux cmds
    :param list remotes: list for remote object
    :return list of list of tuple of flag
    """
    cmd_ext.cmds_remotes(cmds, remotes)


def put_remotes(remotes, local_file, remote_file):
    """
    执行远程复制
    :param list remotes: list for remote object
    :param str local_file: local file abs path
    :param str remote_file: remote file abs path
    """
    cmd_ext.put_remotes(remotes, local_file, remote_file)


def cmd_remote_args_parallel1(remotes, cmd, args, finish_match, executor):
    """
    交互式执行命令 parallel模式
    :param list remotes: list for remote object
    :param str cmd: linux cmd
    :param list args: cmd args
    :param str finish_match: key word flag that cmd finish
    :param executor executor: execute pool
    """
    cmd_ext.cmd_remote_args_parallel1(remotes, cmd, args, finish_match, executor)


def cmd_remote_args_parallel2(remote_cmd_and_args, finish_match, executor):
    """
    交互式执行命令 parallel模式
    :param map remote_cmd_and_args: k:remote - v:list of cmd and args
    :param str finish_match: key word flag that cmd finish
    :param executor executor: execute pool
    """
    cmd_ext.cmd_remote_args_parallel2(remote_cmd_and_args, finish_match, executor)


def put_remote_parallel1(remotes, local_file, remote_file, executor):
    """
    执行远程复制 parallel模式
    :param list remotes: remote object
    :param str local_file: local file abs path
    :param str remote_file: remote file abs path
    :param executor executor: execute pool
    """
    cmd_ext.put_remote_parallel1(remotes, local_file, remote_file, executor)


def put_remote_parallel2(remote_to_local_and_remote_file, executor):
    """
    执行远程复制 parallel模式
    :param map remote_to_local_and_remote_file: remote object: k:rmeote - v:[local_file,remote_file]
    :param executor executor: execute pool
    """
    cmd_ext.put_remote_parallel2(remote_to_local_and_remote_file, executor)


def cmds_remote_parallel1(remotes, cmds, executor):
    """
    执行命令 parallel模式
    :param list remotes: remote object
    :param list cmds: linux cmds
    :param executor executor: execute pool
    """
    cmd_ext.cmds_remote_parallel1(remotes, cmds, executor)


def cmds_remote_parallel2(remote_to_cmds, executor):
    """
    执行命令 parallel模式
    :param map remote_to_cmds: k:remote - v:cmds
    :param executor executor: execute pool
    """
    cmd_ext.cmds_remote_parallel2(remote_to_cmds, executor)
