#!/usr/bin/env python
# -=-<[ Bismillahirrahmanirrahim ]>-=-
# -*- coding: utf-8 -*-
# @Date    : 2021-06-27 01:07:23
# @Author  : Dahir Muhammad Dahir
# @Description : something cool


from helpers import none_validator
from typing import List, Optional
from pydantic import BaseModel, validator
from pydantic.fields import Field


class Server(BaseModel):
    username: str
    host_address: str
    password: Optional[str] = None
    ssh_key: Optional[str] = None
    ssh_key_file: Optional[str] = None
    port: Optional[int] = Field(22, gt=0, le=65535)

    _password_val = none_validator("password")
    _ssh_key_val = none_validator("ssh_key")
    _ssh_key_file_val = none_validator("ssh_key_file")


class ServerCommands(BaseModel):
    command_list: List[str]

    @validator("command_list")
    def commands_val(cls, command_list):
        command_list.append("exit")
        return command_list


class NoServersFile(Exception):
    pass


class CriticalError(Exception):
    pass

