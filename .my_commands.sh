#!/usr/bin/env bash



function repo() {
    cd
    python C:/Users/wsm/PycharmProjects/GitAutomation/create.py $1
    cd C:/Users/wsm/$1
    start .
    git init
    git remote add origin https://github.com/hedgarbezerra/$1.git
    touch README.md
    git add .
    git commit -m "Initial commit"
    git push -u origin master
    code .
}