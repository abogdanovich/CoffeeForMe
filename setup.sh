#!/usr/bin/env bash

# setup instructions
cd ~/
mkdir abogdanovich_test
cd ~/abogdanovich_test
virtualenv --no-site-packages coffee_project
source coffee_project/bin/activate
cd ~/abogdanovich_test/coffee_project/
git clone https://github.com/abogdanovich/CoffeeForMe.git
~/abogdanovich_test/coffee_project/bin/pip install -r CoffeeForMe/requirements.txt 
~/abogdanovich_test/coffee_project/bin/python CoffeeForMe/src/main.py -h

