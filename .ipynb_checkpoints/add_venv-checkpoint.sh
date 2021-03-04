#!/usr/bin/env bash
VENVNAME=frille-lang
source $VENVNAME/bin/activate
python -m ipykernel install --user --name $VENVNAME --display-name "$VENVNAME"