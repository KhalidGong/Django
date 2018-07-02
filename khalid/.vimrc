"----------vundle configuration---------------" 

filetype off
set rtp+=/root/.vim/bundle/Vundle.vim
call vundle#begin()

Plugin 'VundleVim/Vundle.vim'
Plugin 'mattn/emmet-vim'
Plugin 'scrooloose/nerdtree'

call vundle#end()
filetype plugin indent on
let g:user_emmet_leader_key='<F2>'

"----------vundle configuration---------------"

"----------nerdtree configuration---------------"

"autocmd vimenter * NERDTree
map <F3> : NERDTreeToggle<CR>

"----------nerdtree configuration---------------"

"----------vim configuration---------------"

set tabstop=4
set expandtab
set autoindent
set nu!
syntax on
set nocompatible

"----------vim configuration---------------"
