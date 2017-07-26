#!/usr/bin/env bash


mkdir -p bin/
mkdir -p libexec/
cp src/tex2fig.py bin/tex2fig
cp src/tex2fig.sh libexec/tex2fig.sh
cp src/tex2fig.tmpl libexec/tex2fig.tmpl

if [ "$#" -eq "1" ]; then
    tex2fig_aux=$1
else
    tex2fig_aux=$PWD/libexec
fi

sed -i.bak2 's#=>replace-me<=#'"${tex2fig_aux}"'#' bin/tex2fig

