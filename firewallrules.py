#!/usr/bin/env python3
import subprocess


def enable_ufw():
    #This enables the firewall if it is not enabled
    subprocess.run(['sudo', 'ufw', 'enable'])


def add_allow_rule(port, proto='tcp'):
    #this is to add rules to tcp ports
    subprocess.run(['sudo', 'ufw', 'allow', str(port) + '/' + proto])


def add_deny_rule(port, proto='tcp'):
    #this is to deny rules to tcp ports
    subprocess.run(['sudo', 'ufw', 'deny', str(port) + '/' + proto])


def reload_ufw():
    #this is to reload the firewall to confirm the new changes
    subprocess.run(['sudo', 'ufw', 'reload'])


def show_ufw_status():
    #this will show the status of the ufw firewall
    subprocess.run(['sudo', 'ufw', 'status', 'verbose'])


def main():

    enable_ufw()

    # Use this to add rules to the firewall
    add_allow_rule(22)
    add_allow_rule(80)
    add_allow_rule(443)

    # Reloads the firewall after new settings have been added
    reload_ufw()

    # After reloading the firewall this displays the new status.
    show_ufw_status()


if __name__ == "__main__":
    main()
