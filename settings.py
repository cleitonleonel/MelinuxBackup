#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
from datetime import datetime, date
import os

today = date.today()


def switch(argument):
    switcher = {
        1: "jan",
        2: "fev",
        3: "mar",
        4: "abr",
        5: "mai",
        6: "jun",
        7: "jul",
        8: "ago",
        9: "set",
        10: "out",
        11: "nov",
        12: "dez"
    }
    return switcher.get(argument, "")


def get_file_name():
    dias = ('seg', 'ter', 'qua', 'qui', 'sex', 'sab', 'dom')
    dia = dias[today.weekday()]
    final_name = f'bkup_{dia}.zip'
    return final_name


def rename_backup():
    time = datetime.now()
    now = time.strftime("%p")
    if now == 'AM':
        now = 'mat'
    elif now == 'PM':
        now = 'vesp'
    dias = ('seg', 'ter', 'qua', 'qui', 'sex', 'sab', 'dom')
    dia = dias[today.weekday()]
    final_name = dia + "_" + now
    return final_name


root_path = "backup"
backup_name = get_file_name()
dynamic_path = f"{str(today.month).zfill(2) if len(str(today.month)) < 2 else str(today.month)}" \
               f"-{switch(today.month)}"
dynamic_file_path = f"{today.year}/{dynamic_path}"
sub_folder = f"{root_path}/{dynamic_file_path}"
melinux_path = None

BASE_DIR = os.getcwd()
HOME_PATH = os.path.join(os.path.expanduser('~'), '') if not melinux_path else melinux_path
GOOGLE_EMAIL = ""
GOOGLE_PASSWORD = ""
GDRIVE_CLIENT_SECRETS_JSON = os.path.join(BASE_DIR, "credenciais/client_secrets.json")
GDRIVE_CREDENTIALS_JSON = os.path.join(BASE_DIR, "credenciais/credentials.json")
GDRIVE_ROOT = {
    "backups": [
        {
            "folder_path": root_path,
            "files": [f'/home/util/{backup_name}']
        },
        {
            "folder_path": sub_folder,
            "files": [f'{HOME_PATH}/01/governo/{dynamic_file_path}/nfce_emitidas.zip',
                      f'{HOME_PATH}/01/governo/{dynamic_file_path}/nfe_emitidas.zip',
                      f'{HOME_PATH}/01/governo/{dynamic_file_path}/xml_fornecedor.zip'
                      ]
        }
    ]
}
