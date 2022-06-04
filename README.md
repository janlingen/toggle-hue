# toggle-hue

simple python script to toggle your Philips hue lights with speech recognition

## how to get the script running:

- install needed packages
  - `pip install -r requirements.txt`
- get the of your Philips Hue Bridge and export it as enviroment variable
  - example: `export IP=127.0.0.1`
- get a Philips hue bridger user and export it as enviroment variable
  - guide on how to get a user: https://developers.meethue.com/develop/get-started-2/
  - example: `export HUE_USER=1028d66426293e821ecfd9ef1a0731df"`
- run `python hue.py`
- the default trigger name is called `sarah`
  - example call: `sarah light` to toggle your lights on/off

## customizing the script

- if you would like to add or remove lights, edit the function run_sarah
- if you would like to change the trigger name, edit the function take_command
