#!/bin/bash
function chkstr {
    if [[ -z "$calcfile1" ]]; 
    then
    echo "No input entered! exiting."
    exit 1
    fi
    while [[ $calcfile1 == *'simple'* || $calcfile1 == *'Simple'* ]]
    do
        chmod +x "$calcfile1"
        python3 "$calcfile1"
    done
    if [[ $calcfile1 == "Y" ]];
    then
        default
    fi
    if [[ $calcfile1 != *'simple'* || $calcfile1 != *'Simple'* ]]
    then
    echo "Invalid input, exiting."
    exit 1
    fi
}
function chkstr2 {
    if [[ -z "$calcfile2" ]]; 
    then
    echo "No input entered! exiting."
    exit 1
    fi
    while [[ $calcfile2 == *'Y'* ]]
    do
        default
    done
    while [[ $calcfile2 == *'simple'* || $calcfile2 == *'Simple'* ]]
    do
        chmod +x "$calcfile2"
        python3 "$calcfile2"
    done
    if [[ $calcfile2 != *'simple'* || $calcfile2 != *'Simple'* ]]
    then
    echo "Invalid input, exiting."
    exit 1
    fi
}
function run {
    echo "Please enter the location of the folder that the file is in
    (Exclude simplecalc1.x.x.py) (E.G: /home/johndoe/Documents (Exclude slash at end)):"
    read folder
    cd "$folder"
    echo "Please enter the name and version of Simplecalc (E.G: simplecalc1.0.14.py)"
    echo "If the python file name is the same as the example type 'Y': "
    read calcfile1
    chkstr
}
function default {
    chmod +x "simplecalc1.0.14.py"
    python3 "simplecalc1.0.14.py"
}
function notrun {
    echo "Please enter the name and version of Simplecalc (E.G: simplecalc1.0.14.py)"
    echo "If the python file name is the same as the example type 'Y': "
    read calcfile2
    chkstr2
}
echo "----(Bash Simplecalc launcher V1.0.14)----"
echo "(This script is compatible with any OS that uses bash, such as Linux.)"
echo "Please install python 3.x for simplecalc to run."
echo "Please type 'Y' if the folder is in a different location than"
echo "this script. ('N' if not.)"
read freq
if [[ $freq == "Y" ]];
then
    run
else
    notrun
fi