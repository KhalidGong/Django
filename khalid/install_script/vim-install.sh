#!/bin/bash

"this script suitable for centos"

"install the latest version vim"
yum install nucrses-devel
cd ~ && git clone https://github.com/vim/vim.git
cd vim/src && make && make install

"install vundle,emmet,nerdtree"
git clone https://github.com/VundleVim/Vundle.vim.git ~/.vim/bundle/Vundle.vim

