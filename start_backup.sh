#!/bin/bash

remote_version=$(curl --silent "https://api.github.com/repos/cleitonleonel/MelinuxBackup/releases/latest" | grep -Po '"tag_name": "\K.*?(?=")')
local_version=$(./backupy --version)

credentials_dir="credenciais/"

if which google-chrome-stable > /dev/null 2>&1;
then
    echo 'Google Chrome já está instalado.'
else
    echo 'Instalando Google Chrome...'
    #sudo wget http://dl.google.com/linux/chrome/deb/pool/main/g/google-chrome-stable/google-chrome-stable_96.0.4664.45-1_amd64.deb
    sudo wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
    sudo chmod 777 ./google-chrome-stable_current_amd64.deb
    sudo apt install -y ./google-chrome-stable_current_amd64.deb
    sudo rm ./google-chrome-stable_current_amd64.deb
    sudo apt autoremove -y
fi

if [ ! -d "$credentials_dir" ]
then
    echo "${credentials_dir} não existe. Criando agora..."
    mkdir ./$credentials_dir
    echo "Pasta criada com sucesso!"
else
    echo "${credentials_dir} já existe."
fi


if [[ "$remote_version" > "$local_version" ]]
then
  echo "Atualização disponível, instalando versão ${remote_version}"
  wget "https://github.com/cleitonleonel/MelinuxBackup/raw/${remote_version}/src/backupy" -O /home/util/pybackup/backupy
  sudo chmod 777 -R /home/util/pybackup
fi

cd /home/util/pybackup && ./backupy
