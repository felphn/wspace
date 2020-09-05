#!/bin/bash

CL='\033[1;33m'
NC='\033[0m'
echo -e "\n${CL}================================"
echo -e "${NC}Ubuntu Autoconfig // Started ..."
echo -e "${CL}================================${NC}\n"
echo -e "${CL}[1]-${NC} Ubuntu for Windows Subsystems Linux"
echo -e "${CL}[2]-${NC} Ubuntu 20.xx"
read -p "// Which config you would like to run? " usrOpt

sudo apt-get update &&
sudo apt-get upgrade -y &&

echo -e "\n${CL}Configuring 'git' ...${NC}"
git config --global user.name "Felipe Lara"
git config --global user.email 68015575+felpshn@users.noreply.github.com
git config --global core.editor vim
## store git login:
## git config --global credential.helper store

echo -e "\n${CL}Installing 'curl' ...${NC}\n"
sudo apt install curl -y &&

echo -e "\n${CL}Installing 'vim' ...${NC}\n"
sudo apt install vim -y &&
curl -fLo ~/.vim/autoload/plug.vim --create-dirs \
        https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim

echo -e "\n${CL}Cloning my repos on GitHub ...${NC}\n"
mkdir GitHub
cd GitHub
git clone https://github.com/felpshn/workspace.git
git clone https://github.com/felpshn/container.git
git clone https://github.com/felpshn/insta-watch.git
git clone https://github.com/felpshn/proffy-discovery.git
git clone https://github.com/felpshn/proffy-omnistack.git
git clone https://github.com/felpshn/soundflix-imreact.git
git clone https://github.com/felpshn/amdgpu-fancontrol.git
git clone https://github.com/felpshn/python-basic.git
git clone https://github.com/felpshn/c-basic.git
git clone https://github.com/felpshn/html-css-basic.git

if [ $usrOpt == 1 ]
then
    echo -e "\n${CL}Configuring 'vim' ...${NC}\n"
    echo "syntax on" >> ~/.vimrc
    echo "set noerrorbells" >> ~/.vimrc
    echo "set tabstop=4 softtabstop=4" >> ~/.vimrc
    echo "set shiftwidth=4" >> ~/.vimrc
    echo "set expandtab" >> ~/.vimrc
    echo "set smartindent" >> ~/.vimrc
    echo "set nu" >> ~/.vimrc
    echo "set mouse=a" >> ~/.vimrc
    echo "set smartcase" >> ~/.vimrc
    echo "set nobackup" >> ~/.vimrc
    echo "set incsearch" >> ~/.vimrc
    echo "inoremap < <><left>" >> ~/.vimrc
    echo "call plug#begin('~/.vim/plugged')" >> ~/.vimrc
    echo "Plug 'sheerun/vim-polyglot'" >> ~/.vimrc
    echo "Plug 'jiangmiao/auto-pairs'" >> ~/.vimrc
    echo "call plug#end()" >> ~/.vimrc

    echo -e "\n${CL}Installing 'zsh' ...${NC}\n"
    sudo apt install zsh -y &&
    echo -e "\n${CL}Cloning 'zsh-autosuggestions' ...${NC}\n"
    git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions
    echo -e "\n${CL}Configuring 'zsh' ...${NC}\n"
    sed -i 's/^ZSH_THEME=.*/ZSH_THEME="'steeef'"/' ~/.zshrc
    echo "alias cd..='cd ..'" >> ~/.zshrc
    echo "alias cls='clear'" >> ~/.zshrc
    echo "alias explorer='explorer.exe'" >> ~/.zshrc
    echo "alias node='powershell.exe node'" >> ~/.zshrc
    echo "alias npm='powershell.exe npm'" >> ~/.zshrc
    echo "alias npx='powershell.exe npx'" >> ~/.zshrc
    echo "alias py='powershell.exe py'" >> ~/.zshrc
    echo "alias pip='powershell.exe pip'" >> ~/.zshrc
    echo "alias g++='powershell.exe g++'" >> ~/.zshrc
    echo "export EDITOR=/usr/bin/vim" >> ~/.zshrc
    echo "export VISUAL=/usr/bin/vim" >> ~/.zshrc
    echo -e "\n${CL}Installing 'oh my zsh' ...${NC}\n"
    sh -c "$(curl -fsSL https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
fi

if [ $usrOpt == 2 ]
then
    echo -e "\n${CL}Installing 'pip3' ...${NC}\n"
    sudo apt install python3-pip -y &&

    echo -e "\n${CL}Installing 'python-tkinter' ...${NC}\n"
    sudo apt-get install python3-tk -y &&

    echo -e "\n${CL}Installing 'nodejs' ...${NC}\n"
    sudo apt install nodejs -y &&

    echo -e "\n${CL}Installing 'pulseaudio' and 'pulseeffects' ...${NC}\n"
    sudo apt install pavucontrol -y &&
    sudo apt install pulseeffects -y &&

    echo -e "\n${CL}Installing 'vlc' ...${NC}\n"
    sudo snap install vlc &&

    echo -e "\n${CL}Installing 'spotify' ...${NC}\n"
    sudo snap install spotify &&

    echo -e "\n${CL}Installing 'discord' ...${NC}\n"
    sudo snap install discord &&

    echo -e "\n${CL}Installing 'thunderbird' ...${NC}\n"
    sudo snap install thunderbird &&
fi

sudo apt autoremove -y &&
sudo apt autoclean &&
sudo apt-get clean &&

echo -e "\n\n==================================="
echo -e "              ${NC}All done!              "
echo -e "${CL}===================================${NC}\n"
