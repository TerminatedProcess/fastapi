#set prompt
PS1='\u \w $'

# some aliases
alias kk='clear'
function k() { clear;ls -al1 $1 | more; }
alias sn='shutdown now'
alias sr='shutdown -r now'
