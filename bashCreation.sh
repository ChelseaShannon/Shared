#!/bin/bash
###### Start each bash file with the above #########


##### Custom bash file should be name XXXX.sh
##### To include this custom bash in your defaults, add source cmd (below) to the bottom of your .bashrc.
source ~/.bashrc_custom.sh


####### Add personal aliases and functions below #############

# prints the input
function print_my_input() {
  echo 'Your input: ' $1
}