# need to invoke this file from the root of the project, using "source"
sudo chmod 666 /dev/ttyACM1
python3 -m venv ./venv
source ./venv/bin/activate
python -m pip install --upgrade pip
python -m pip install --upgrade wheel
python -m pip install -r requirements.txt
