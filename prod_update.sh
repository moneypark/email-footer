#!/bin/bash
set -ex

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
VENV=venv
RESTRICT_USER=omega

if [ "$(whoami)" != "$RESTRICT_USER" ]; then
    echo "Invalid user. Are you '$RESTRICT_USER'?"
    exit 1
fi

cd "$SCRIPT_DIR"
[ ! -d $VENV ] && virtualenv -p python2 $VENV
source "$VENV/bin/activate"
pip install -r requirements.txt

git fetch
git checkout -f master
git reset --hard origin/master

make collect
