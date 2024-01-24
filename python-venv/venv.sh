#!/bin/bash


echo 'SYSTEM PYTHON3'
echo

python3 -m venv .venv

python3_path=$(which python3)
pip3_path=$(which pip3)

echo 'python3 →' $python3_path
echo 'pip3 →' $pip3_path

source .venv/bin/activate

echo
echo 'VENV ACTIVATED'
echo

python3_path=$(which python3)
pip3_path=$(which pip3)

echo 'python3 →' $python3_path
echo 'pip3 →' $pip3_path

deactivate

echo
echo 'VENV DEACTIVATED'
echo

python3_path=$(which python3)
pip3_path=$(which pip3)

echo 'python3 →' $python3_path
echo 'pip3 →' $pip3_path
