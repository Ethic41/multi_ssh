#!/usr/bin/env python
# -=-<[ Bismillahirrahmanirrahim ]>-=-
# -*- coding: utf-8 -*-
# @Date    : 2021-06-27 00:47:56
# @Author  : Dahir Muhammad Dahir
# @Description : A simple tool that allow connecting
#                to multiple ssh servers and executing
#                commands on the various servers


from threading import Thread
from typing import Dict, List
from models import CriticalError, NoServersFile, Server, ServerCommands
from pwn import *
import os


def main():
    server_list = get_ssh_servers()
    servers_command = get_server_commands()
    create_server_workers(server_list, servers_command)


def get_ssh_servers() -> List[Server]:
    servers_list: List[Server] = []

    servers_list_file = input("{x} Enter the ssh servers filename, [sample_servers_list.dmd]:\n").strip("\n")
    
    if not servers_list_file:
        print("No ssh servers file was specified, falling back to default: sample_servers_list.dmd\n")
        servers_list_file = "sample_files/sample_servers_list.dmd"
    
    try:
        with open(servers_list_file) as f:
            server_lines = f.readlines()
        
        if not server_lines:
            raise CriticalError("servers list file is empty")
        
        for line in server_lines:
            line: str = line.strip().strip("\r\n").strip("\r").strip("\n")
            line_entries: List[str] = line.split(",")

            server_dict: Dict[str, str] = {}

            for line_entry in line_entries:
                key, value = line_entry.split("=")
                server_dict[key] = value
            
            server = Server(**server_dict)
            servers_list.append(server)
        
        return servers_list

    except FileNotFoundError:
        raise CriticalError("servers list file not found, please provide full file path")


def get_server_commands() -> ServerCommands:
    command_list_file = input("{x} Enter the server commands filename, [ sample_commands_list.dmd ]:\n").strip("\n")

    if not command_list_file:
        print("No command list file provided, falling back to default: sample_commands_list.dmd")
        command_list_file = "sample_files/sample_commands_list.dmd"
    
    try:
        with open(command_list_file) as f:
            command_lines = f.readlines()
        
        if not command_lines:
            raise CriticalError("command list file is empty")
        
        command_list: List[str] = []

        for command in command_lines:
            command: str = command.strip().strip("\r\n").strip("\n").strip("\r")
            command_list.append(command)
        
        return ServerCommands(command_list=command_list)

    except FileNotFoundError:
        raise CriticalError("command list file not found, please provide full file path")


def execute_server_commands(server: Server, commands: ServerCommands):
    print(f"Establishing connection with {server.host_address} on {server.port}...\n")
    ssh_conn = ssh(user=server.username, host=server.host_address, port=server.port, password=server.password, \
        key=server.ssh_key, keyfile=server.ssh_key_file)
    
    print(f"connection established with {server.host_address}, create a new shell...")
    
    ssh_shell = ssh_conn.shell()

    print(f"shell created...executing server commands on {server.host_address}...")
    ssh_shell.sendlines(lines=commands.command_list)
    command_response_list = ssh_shell.recvall().decode().split("\r\n")

    for command_response in command_response_list:
        print(command_response)
    
    print(f"commands execution completed successfully on {server.host_address}")


def create_server_workers(server_list: List[Server], commands: ServerCommands):
    workers: List[Thread] = []

    print(f"creating {len(server_list)} server workers...")
    for server in server_list:
        server_worker = Thread(target=execute_server_commands, args=(server, commands))
        workers.append(server_worker)
    
    for worker in workers:
        worker.start()
    
    for worker in workers:
        worker.join()
    
    print("All server jobs have been completed successfully")


if __name__ == "__main__":
    main()

