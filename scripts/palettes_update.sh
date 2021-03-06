#!/bin/bash

INDIR=${1:-/mnt/c/Users/ktmea/AppData/Roaming/krita/palettes}
OUTDIR=${2:-.}
MODE=$3

echo
echo "Copying palettes from $INDIR to $OUTDIR."
echo "rsync -u -a ${INDIR} $OUTDIR";
rsync -u -a ${INDIR} $OUTDIR;
