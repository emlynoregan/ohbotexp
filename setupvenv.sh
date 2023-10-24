# need to invoke this file from the root of the project, using "source"
sudo chmod 666 /dev/ttyACM0
sudo chmod 666 /dev/ttyACM1
sudo chmod 666 /dev/ttyACM2
sudo chmod 666 /dev/ttyACM3
python3 -m venv ./venv
source ./venv/bin/activate
python -m pip install --upgrade pip
python -m pip install --upgrade wheel
python -m pip install -r requirements.txt
