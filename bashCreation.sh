#!/bin/bash
###### Start each bash file with the above #########


##### Custom bash file should be name XXXX.sh
##### To include this custom bash in your defaults, add source cmd (below) to the bottom of your .bashrc.
source ~/.bashrc_custom.sh


####### Add personal aliases and functions below #############

## Updating bash
alias editbash='nano ~/.bashrc_custom.sh'
alias catbash='cat ~/.bashrc_custom.sh'
alias srcbash='source ~/.bashrc_custom.sh'

alias cddev='cd ~/Dev'

### prints the input
alias lq='ls -lahrt --color=auto'

function print_my_input() {
  echo 'Your input: ' $1
}