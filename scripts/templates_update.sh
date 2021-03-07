#!/bin/bash

INDIR=${1:-/mnt/c/Users/ktmea/AppData/Roaming/krita/templates}
OUTDIR=${2:-.}
MODE=$3

echo
echo "Copying templates from $INDIR to $OUTDIR."
echo "rsync -u -a ${INDIR} $OUTDIR";
rsync -u -a ${INDIR} $OUTDIR;
