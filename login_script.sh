#set prompt
PS1='\u \w $'

# some aliases
alias kk='clear'
function k() { clear;ls -al1 $1 | more; }
alias sn='shutdown now'
alias sr='shutdown -r now'
alias hgrep='history 1000 | grep -i $1 '
alias ipaddress='ip addr show'
alias rmdirf='rm -rf $1'
function c() { cd $1; k; }
alias c.='cd ..;k'
alias home='cd ~;k'
