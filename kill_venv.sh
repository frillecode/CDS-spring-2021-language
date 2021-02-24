#!/usr/bin/env bash

VENVNAME=frille-lang
jupyter kernelspec uninstall $VENVNAME
rm -r $VENVNAME