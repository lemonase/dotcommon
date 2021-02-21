dotcommon is a crawler that is built to answer questions
*What are the most common Bash aliases?*,
*What are the most common Vundle plugins for Vim?*, etc.
It searches GitHub for 1000 most recently edited configs
(to follow trends) and counts such things.

    Disclaimer: the project isn't run by a data scientist
    and the numbers below should be interpreted in the context
    provided above: *1000 most recently edited configs hosted on
    GitHub*. Make any further assumptions on your own risk.
    See `these slides`_ if you look for a serious research.

.. _these slides: http://bit.ly/2NVyiXu

.. contents:: Here are top-tens of various things:

Bash
----


Aliases
~~~~~~~


========================================================================================================================================================================  ===
``alias la='ls -A'``                                                                                                                                                      173
``alias l='ls -CF'``                                                                                                                                                      171
``alias ll='ls -alF'``                                                                                                                                                    160
``alias alert='notify-send --urgency=low -i "$([ $? = 0 ] && echo terminal || echo error)" "$(history|tail -n1|sed -e '\''s/^\s*[0-9]\+\s*//;s/[;&|]\s*alert$//'\'')"'``  152
``alias ls='ls --color=auto'``                                                                                                                                             75
``alias mv='mv -i'``                                                                                                                                                       66
``alias rm='rm -i'``                                                                                                                                                       62
``alias cp='cp -i'``                                                                                                                                                       62
``alias grep='grep --color=auto'``                                                                                                                                         61
``alias ..='cd ..'``                                                                                                                                                       51
========================================================================================================================================================================  ===


Exports
~~~~~~~


==========================================================================================  ==
``export NVM_DIR="$HOME/.nvm"``                                                             53
``export EDITOR=vim``                                                                       44
``export HISTCONTROL=ignoreboth``                                                           31
``export TERM=xterm-256color``                                                              31
``export VISUAL=vim``                                                                       24
``export MYNAME``                                                                           24
``export LESS='-M'``                                                                        24
``export CLICOLOR=1``                                                                       23
``export GCC_COLORS='error=01;31:warning=01;35:note=01;36:caret=01;32:locus=01:quote=01'``  22
``export PATH``                                                                             21
==========================================================================================  ==


PS1
~~~


=========================================================================================================================================  ==
``PS1='[\u@\h \W]\$ '``                                                                                                                    30
``PS1="$"``                                                                                                                                27
``PS1='\[\033[1;31m\]$ >\[\033[00m\] '``                                                                                                    5
``PS1='${debian_chroot:+($debian_chroot)}\u@\h:\w\$ '``                                                                                     3
``PS1='\$ '``                                                                                                                               2
``PS1=''``                                                                                                                                  2
``PS1="\n \[\033[0;34m\]┌─────(\[\033[1;35m\]\u\[\033[0;34m\])─────(\[\033[1;32m\]\w\[\033[0;34m\]) \n └> \[\033[1;36m\]\$ \[\033[0m\]"``   2
``PS1='[\u@\h \W$(__git_ps1 " (%s)")]\$ '``                                                                                                 2
``PS1='``                                                                                                                                   2
``PS1="$PS1"'\[\e[0m\]'                          # reset all``                                                                              2
=========================================================================================================================================  ==


PS2
~~~


==============================================  =
``PS2="\[${yellow}\]→ \[${reset}\]";``          2
``PS2="$> "``                                   1
``PS2='> '``                                    1
``PS2="\\ "``                                   1
``PS2=" "``                                    1
``PS2="${COLOR_BOLD_PURPLE}>${COLOR_RESET} "``  1
``PS2='$> '``                                   1
==============================================  =


Radline macros
~~~~~~~~~~~~~~


==========================================  ==
``bind "set completion-ignore-case on"``    12
``bind '"\e[A": history-search-backward'``  10
``bind '"\e[B": history-search-forward'``   10
``bind "set show-all-if-ambiguous on"``     10
``bind 'set show-all-if-ambiguous on'``      6
``bind 'set completion-ignore-case on'``     5
``bind 'TAB:menu-complete'``                 5
``bind "set completion-map-case on"``        5
``bind '"\e[A":history-search-backward'``    4
``bind '"\e[B":history-search-forward'``     4
==========================================  ==


Bspwm
-----


Window rules
~~~~~~~~~~~~


===========================================================  ===
``bspc rule -a Screenkey manage=off``                        260
``bspc rule -a Kupfer.py focus=on``                          209
``bspc rule -a mplayer2 state=floating``                     195
``bspc rule -a Gimp desktop='^8' state=floating follow=on``  182
``bspc rule -a Chromium desktop='^2'``                       162
``bspc rule -a Zathura state=tiled``                         140
``bspc rule -r "*"``                                         126
``bspc rule -a Emacs state=tiled``                            75
``bspc rule -a feh state=floating``                           59
``bspc rule -a Galculator state=floating``                    40
===========================================================  ===


Window gap/border width
~~~~~~~~~~~~~~~~~~~~~~~


===============  ===
``12/2``         151
``unset/unset``   76
``10/2``          66
``15/3``          35
``0/1``           27
``0/2``           26
``8/2``           26
``0/0``           18
``5/2``           18
``10/1``          18
===============  ===


Fish
----


Aliases
~~~~~~~


=========================  ==
``alias vim="nvim"``       29
``alias g='git'``          14
``alias vim='nvim'``       13
``alias gs="git status"``  13
``alias ls="exa"``         13
``alias g="git"``          13
``alias vi="nvim"``        12
``alias gd='git diff'``    11
``alias vim "nvim"``       10
``alias gs='git status'``  10
=========================  ==


Exports
~~~~~~~


================================================================================  ==
``set -x EDITOR nvim``                                                            71
``set -x NNN_BMS 'd:~/Downloads;p:~/pics;D:~/Dropbox/;s:~/Dropbox/screenshots'``  54
``set -x PATH /usr/local/bin $PATH``                                              50
``set -x PAGER less``                                                             49
``set -x VISUAL nvim``                                                            48
``set -x TERMINAL alacritty``                                                     43
``set -x NNN_SHOW_HIDDEN 1``                                                      43
``set -x LESS -R``                                                                43
``set -x BIB $HOME/uni.bib``                                                      42
``set -x TERM alacritty``                                                         42
================================================================================  ==


i3wm
----


Modkey
~~~~~~


================================  ===
``set $mod Mod4``                 732
``set $mod Mod1``                 118
``set $mod mod4``                   4
``set $mod Mod3``                   3
``set $mod = Mod1``                 1
``set $mod Ctrl``                   1
``set $mod mod1``                   1
``set $mod   Mod1``                 1
``set $mod                Mod4``    1
================================  ===


Font
~~~~


==================================================================  ===
``font pango:monospace 8``                                          200
``font xft:URWGothic-Book 11``                                       46
``font pango:DejaVu Sans Mono 8``                                    40
``font -misc-fixed-medium-r-normal--13-120-75-75-C-70-iso10646-1``   40
``font pango:monospace 10``                                          23
``font pango:monospace 9``                                           15
``font pango:Noto Mono Regular 13``                                  13
``font pango:DejaVu Sans Mono 10``                                   12
``font pango:monospace 12``                                          10
``font pango:DejaVu Sans Mono 12``                                    9
==================================================================  ===


Keybindings
~~~~~~~~~~~


============================================  ===
``bindsym $mod+Shift+r restart``              768
``bindsym $mod+Shift+space floating toggle``  730
``bindsym $mod+Shift+c reload``               723
``bindsym $mod+f fullscreen toggle``          719
``bindsym $mod+r mode "resize"``              713
``bindsym $mod+space focus mode_toggle``      684
``bindsym $mod+Right focus right``            683
``bindsym $mod+Shift+Right move right``       675
``bindsym $mod+Down focus down``              671
``bindsym $mod+Up focus up``                  671
============================================  ===


Modes
~~~~~


=============================  ===
``mode "resize" {``            791
``mode "$mode_system" {``      201
``mode "$mode_gaps" {``        152
``mode "$mode_gaps_inner" {``  152
``mode "$mode_gaps_outer" {``  152
``mode "$mode_launcher" {``     15
``mode "$mode_display" {``      12
``mode "Resize Mode" {``        11
``mode "$mode_gaps_horiz" {``   10
``mode "$mode_gaps_verti" {``   10
=============================  ===


Inner gaps
~~~~~~~~~~


=================  ===
``gaps inner 10``  117
``gaps inner 5``    73
``gaps inner 14``   48
``gaps inner 15``   45
``gaps inner 0``    26
``gaps inner 8``    26
``gaps inner 20``   26
``gaps inner 6``    24
``gaps inner 12``   16
``gaps inner 7``    15
=================  ===


Outer gaps
~~~~~~~~~~


=================  ===
``gaps outer 0``   123
``gaps outer 5``    63
``gaps outer -2``   59
``gaps outer 10``   30
``gaps outer 2``    22
``gaps outer 15``   13
``gaps outer 1``    13
``gaps outer -4``   12
``gaps outer 20``   10
``gaps outer 12``    8
=================  ===


exec
~~~~


==================================================================================  ===
``exec --no-startup-id nm-applet``                                                  352
``exec --no-startup-id xss-lock --transfer-sleep-lock -- i3lock --nofork``          127
``exec --no-startup-id /usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1``   91
``exec --no-startup-id pamac-tray``                                                  85
``exec --no-startup-id xfce4-power-manager``                                         84
``exec --no-startup-id volumeicon``                                                  77
``exec --no-startup-id clipit``                                                      65
``exec --no-startup-id nitrogen --restore; sleep 1; compton -b``                     52
``exec --no-startup-id dunst``                                                       49
``exec --no-startup-id blueman-applet``                                              44
==================================================================================  ===


Neovim
------


Set statements
~~~~~~~~~~~~~~


=======================  ===
``set number``           399
``set expandtab``        387
``set hidden``           355
``set ignorecase``       322
``set smartcase``        293
``set termguicolors``    260
``set mouse=a``          252
``set nobackup``         252
``set background=dark``  250
``set shiftwidth=4``     249
=======================  ===


Colorschemes
~~~~~~~~~~~~


============================  ==
``colorscheme gruvbox``       98
``colorscheme onedark``       36
``colorscheme dracula``       27
``colorscheme nord``          25
``colorscheme molokai``       21
``colorscheme one``           18
``colorscheme wal``           13
``colorscheme PaperColor``    11
``colorscheme NeoSolarized``  10
``colorscheme ayu``            9
============================  ==


Vundle plugins
~~~~~~~~~~~~~~


===========================================  ==
``Plugin 'VundleVim/Vundle.vim'``            20
``Plugin 'scrooloose/nerdtree'``             15
``Plugin 'tpope/vim-surround'``              14
``Plugin 'tpope/vim-fugitive'``              13
``Plugin 'vim-airline/vim-airline'``          9
``Plugin 'scrooloose/nerdcommenter'``         9
``Plugin 'ryanoasis/vim-devicons'``           9
``Plugin 'itchyny/lightline.vim'``            8
``Plugin 'vim-airline/vim-airline-themes'``   6
``Plugin 'majutsushi/tagbar'``                6
===========================================  ==


Vim-plug plugins
~~~~~~~~~~~~~~~~


===================================================  ===
``Plug 'tpope/vim-fugitive'``                        312
``Plug 'tpope/vim-surround'``                        281
``Plug 'junegunn/fzf.vim'``                          267
``Plug 'vim-airline/vim-airline'``                   241
``Plug 'neoclide/coc.nvim', {'branch': 'release'}``  209
``Plug 'scrooloose/nerdtree'``                       201
``Plug 'airblade/vim-gitgutter'``                    198
``Plug 'tpope/vim-commentary'``                      194
``Plug 'vim-airline/vim-airline-themes'``            191
``Plug 'itchyny/lightline.vim'``                     150
===================================================  ===


Sxhkd
-----


Commands bound to keybinds
~~~~~~~~~~~~~~~~~~~~~~~~~~


==============================================================  ===
``pkill -USR1 -x sxhkd``                                        118
``bspc node -{f,s} {west,south,north,east}``                     83
``bspc desktop -l next``                                         78
``bspc node -{c,k}``                                             77
``bspc node -p cancel``                                          76
``bspc node -p {west,south,north,east}``                         74
``bspc node -f {next,prev}.local``                               71
``bspc node -o 0.{1-9}``                                         69
``bspc node -z {left -20 0,bottom 0 20,top 0 -20,right 20 0}``   69
``firefox``                                                      69
==============================================================  ===


Commands bound to keybinds (except bspc)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


========================  ===
``pkill -USR1 -x sxhkd``  118
``firefox``                69
``termite``                62
``playerctl play-pause``   59
``thunar``                 59
``pavucontrol``            56
``rofi -show run``         54
``oblogout``               53
``playerctl previous``     52
``playerctl next``         51
========================  ===


Termite
-------


Font
~~~~


=============================  ==
``font = monospace 9``         55
``font = monospace 12``        53
``font = monospace 11``        36
``font = monospace 10``        22
``font = hack 10``             18
``font = hack 11``             16
``font = source code pro 10``  16
``font = source code pro 11``  13
``font = hack 12``             12
``font = hack 9``              11
=============================  ==


Vim
---


Set statements
~~~~~~~~~~~~~~


======================  ===
``set expandtab``       469
``set number``          417
``set hlsearch``        351
``set incsearch``       337
``set nocompatible``    319
``set laststatus=2``    305
``set autoindent``      302
``set ignorecase``      284
``set shiftwidth=4``    283
``set encoding=utf-8``  270
======================  ===


Colorschemes
~~~~~~~~~~~~


==========================  ==
``colorscheme gruvbox``     70
``colorscheme molokai``     37
``colorscheme solarized``   34
``colorscheme desert``      22
``colorscheme onedark``     18
``colorscheme jellybeans``  15
``colorscheme nord``        13
``colorscheme dracula``     12
``colorscheme slate``       10
``colorscheme solarized8``   8
==========================  ==


Vundle plugins
~~~~~~~~~~~~~~


===========================================  ===
``Plugin 'VundleVim/Vundle.vim'``            106
``Plugin 'scrooloose/nerdtree'``              76
``Plugin 'tpope/vim-fugitive'``               68
``Plugin 'vim-airline/vim-airline'``          45
``Plugin 'vim-airline/vim-airline-themes'``   40
``Plugin 'tpope/vim-surround'``               34
``Plugin 'gmarik/Vundle.vim'``                27
``Plugin 'morhetz/gruvbox'``                  24
``Plugin 'kien/ctrlp.vim'``                   24
``Plugin 'airblade/vim-gitgutter'``           23
===========================================  ===


Vim-plug plugins
~~~~~~~~~~~~~~~~


=========================================  ===
``Plug 'tpope/vim-fugitive'``              160
``Plug 'tpope/vim-surround'``              152
``Plug 'vim-airline/vim-airline'``         135
``Plug 'junegunn/fzf.vim'``                123
``Plug 'vim-airline/vim-airline-themes'``  115
``Plug 'airblade/vim-gitgutter'``          109
``Plug 'scrooloose/nerdtree'``             100
``Plug 'tpope/vim-commentary'``             96
``Plug 'tpope/vim-repeat'``                 88
``Plug 'sheerun/vim-polyglot'``             73
=========================================  ===


Xorg
----


Window managers
~~~~~~~~~~~~~~~


========================  ===
``exec i3``               216
``exec bspwm``            128
``exec dwm``               98
``exec awesome``           27
``exec xmonad``            23
``exec $(get_session)``    22
``exec openbox-session``   14
``exec startplasma-x11``    7
``exec emacs``              7
``exec sowm``               6
========================  ===


Daemons
~~~~~~~


====================================  ==
``sxhkd &``                           87
``dunst &``                           85
``xsetroot -cursor_name left_ptr &``  36
``unclutter &``                       30
``numlockx &``                        29
``nm-applet &``                       26
``picom &``                           23
``~/.fehbg &``                        22
``compton &``                         21
``redshift &``                        17
====================================  ==


Zsh
---


Aliases
~~~~~~~


==================================  ==
``alias vim="nvim"``                47
``alias gs='git status'``           34
``alias grep='grep --color=auto'``  34
``alias vim='nvim'``                33
``alias rm='rm -i'``                29
``alias g='git'``                   29
``alias gs="git status"``           28
``alias ..='cd ..'``                26
``alias mv='mv -i'``                25
``alias vi="nvim"``                 24
==================================  ==


Exports
~~~~~~~


==============================================  ===
``export ZSH=$HOME/.oh-my-zsh``                 107
``export LANG=en_US.UTF-8``                     106
``export NVM_DIR="$HOME/.nvm"``                  94
``export ZSH="$HOME/.oh-my-zsh"``                66
``export LC_ALL=en_US.UTF-8``                    66
``export KEYTIMEOUT=1``                          65
``export EDITOR=vim``                            48
``export GPG_TTY=$(tty)``                        46
``export GOPATH=$HOME/go``                       40
``export PATH=$HOME/bin:/usr/local/bin:$PATH``   38
==============================================  ===


Theme
~~~~~


===========================================  ==
``ZSH_THEME="robbyrussell"``                 89
``ZSH_THEME="powerlevel10k/powerlevel10k"``  65
``ZSH_THEME="agnoster"``                     52
``ZSH_THEME="spaceship"``                    26
``ZSH_THEME="powerlevel9k/powerlevel9k"``    25
``ZSH_THEME="ys"``                           13
``ZSH_THEME="bira"``                         12
``ZSH_THEME=""``                             11
``ZSH_THEME=powerlevel10k/powerlevel10k``     8
``ZSH_THEME="random"``                        8
===========================================  ==


Keybindings
~~~~~~~~~~~


=====================================================  ===
``bindkey -v``                                         145
``bindkey -e``                                          75
``bindkey -M menuselect 'l' vi-forward-char``           38
``bindkey -M menuselect 'j' vi-down-line-or-history``   38
``bindkey -M menuselect 'h' vi-backward-char``          37
``bindkey -M menuselect 'k' vi-up-line-or-history``     37
``bindkey -v '^?' backward-delete-char``                27
``bindkey '^[[A' history-substring-search-up``          24
``bindkey '^[[B' history-substring-search-down``        24
``bindkey '^e' edit-command-line``                      19
=====================================================  ===

