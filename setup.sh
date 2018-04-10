#!/usr/bin/env bash

# setup instructions
cd ~/
mkdir abogdanovich_test
cd ~/abogdanovich_test
virtualenv --no-site-packages coffee_project
cd ~/abogdanovich_test/coffee_project/
source bin/activate

git clone https://github.com/abogdanovich/CoffeeForMe.git
cd ~/abogdanovich_test/coffee_project/CoffeeForMe
~/abogdanovich_test/coffee_project/bin/pip install -r requirements.txt 
# run pytest
cd ~/abogdanovich_test/coffee_project/CoffeeForMe/src
pytest ~/abogdanovich_test/coffee_project/CoffeeForMe/src/test/test_coffeeTeam.py
pytest ~/abogdanovich_test/coffee_project/CoffeeForMe/src/test/test_coffeeBarista.py
pytest ~/abogdanovich_test/coffee_project/CoffeeForMe/src/test/test_coffeeManager.py
# run main script
~/abogdanovich_test/coffee_project/bin/python main.py -h

