#!/usr/bin/env bash


mkdir -p bin/
mkdir -p script_dir/
cp src/tex2fig.py bin/tex2fig
cp src/tex2fig.sh script_dir/tex2fig.sh
cp src/tex2fig.tmpl script_dir/tex2fig.tmpl

if [ "$#" -eq "1" ]; then
    tex2fig_aux=$1
else
    tex2fig_aux=$PWD/script_dir
fi

sed -i 's#"=>replace-me<="#'"${tex2fig_aux}"'#' bin/tex2fig

