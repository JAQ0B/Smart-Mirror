#Activate the virtual environment
cd PythonMirror
source bin/activate

# Run the Main script for Clothing suggestions 
cd TechnologyProjekt-SmartMirror/Raspberry
python RpiMain.py &

# Run the Ai script only if useing better hardware than RPI3b
cd TechnologyProjekt-SmartMirror/PC/src
python PcMain.py &

# Run the MagicMirror application
cd
cd ./MagicMirror
DISPLAY=:0 npm start
