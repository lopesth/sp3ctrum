# UV-Vis Sp3ctrum P4tronus

This program uses output files from the Gaussian quantum chemistry package and performs gaussian convolutions to simulate any UV-vis spectrum. This code aids molecular dynamics simulations to study the overall contribution to the UV-vis spectrum from the selected frames. It enables both overlaid and separated spectra.

Instructions:
Download the latest version released on and unzip the folder in the Home folder.

Linux or macOS:
If you do not have Python 3 installed.
Install, preferably by 'sudo apt install python3' (Ubuntu or another Debian-based), 'sudo yum install python3' (Fedora or Fedora-based) or 'brew install python3' (Homebrew in macOS).

After that, edit ~/.bash_rc (linux) or ~/.bash_profile (macOS) with the following line:
alias sp3ctrum_app='python3 ~/sp3ctrum_UV-Vis_P4tronus/sp3ctrum_app.py'

After that, just run the sp3ctrum_app command in terminal:
- Terminal with answer and friendly questions: 'sp3trum_app -friendly'
- Terminal with file with the parameters fed in execution: 'sp3trum_app -file file.in'
- Graphical User Interface: 'sp3trum_app'

Windows:
For Windows, you will need to install Python3, after that, add Python installation path to Windows PATH in ENVIRONMENT VARIABLE.
After that run sp3ctrum_app.py by double clicking.

Some python packages needed to run the application
- Tkinter
- Numpy
- Matplotlib
- Pillow

In most installations these packages are already installed, but if any are missing, it can be installed with: 
'pip3 install PACKAGE_NAME'
