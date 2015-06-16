#!/usr/bin/env python2
from __future__ import print_function
from fabric.api import env, run, settings, sudo, put
from nikola.settings import SERVER_DATA, SERVER_HOME, SERVER_LOG, SERVER_USER


# Enable SSH aliases
env.use_ssh_config = True


def install_mongo():
    """Install mongo."""
    put("mongodb", "{}/mongodb".format(SERVER_HOME))


def install_wemo():
    """Install and configure wemo software."""
    run("pip install ouimeaux")
    put("config.yml", "{}/.wemo/config.yml".format(SERVER_HOME))


def scaffold_directories():
    """
    Create required directories and configure permissions.
    """
    # Create code directory folder
    run("mkdir {}/code".format(SERVER_HOME))

    # Create log directory for all project logging
    sudo("mkdir -p {}".format(SERVER_LOG))
    sudo("chown {} {}".format(SERVER_USER, SERVER_LOG))

    # Create data directory where csv and db files are stored
    sudo("mkdir -p {}".format(SERVER_DATA))
    sudo("chown -R {} {}".format(SERVER_USER, SERVER_DATA))


def grep(text, file):
    with settings(warn_only=True):
        return run("grep {} {}".format(text, file))


def exists(path):
    with settings(warn_only=True):
        return run("test -e {}".format(path))


def check_server_config():
    """
    Determine which components are installed on the server.
    :rtype: bool
    :return: all tests passed
    """
    # Using ssh key?
    if 1 == exists("~/.ssh/authorized_keys").return_code:
        print("ssh: No authorized_keys file found. SSH may not be configured "
              "correctly")

    # Using static IP?
    if 1 == grep("static", "/etc/network/interfaces").return_code:
        print("network: No static keyword found in /etc/network/interfaces. "
              "Refer to https://github.com/project-nikola/hardware for more "
              "info")

    # Is Mongo installed?
    # Are basic directories created?
