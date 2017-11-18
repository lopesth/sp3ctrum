# UV-Vis Sp3ctrum P4tronus

This program uses output files from the Gaussian quantum chemistry package and performs gaussian convolutions to simulate any UV-vis spectrum. This code aids molecular dynamics simulations to study the overall contribution to the UV-vis spectrum from the selected frames. It enables both overlaid and separated spectra.<br><br>

<h1>Instructions:</h1>
<br>
Download the latest version released on <a href="https://github.com/lopesth/https://github.com/lopesth/UV-Vis-Sp3ctrum-P4tronus/archive/2.0.1.zip"> here </a> and unzip the folder in the Home folder.
<h4>Linux or mscOS:</h4>
If you do not have Python 3 installed, install, preferably by <i>apt-get install python3.6</i> (Ubuntu or another Debian-based), <i>yum install python3.6</i> (Fedora or Fedora-based) or Homebrew or Macports (macOS).
and edit .bash_rc (linux) or .bash_profile (macOS) with the following line:<br>
<small>```alias sp3ctrum_app='python3 ~/sp3ctrum_UV-Vis_P4tronus/sp3ctrum_app.py'```</small><br><br>
After that, just run the sp3ctrum_app command in the folder where the .log files are located.
<br><br><br>

<b>Modes:</b>

- Terminal with answer and friendly questions:
```
sp3trum_app -friendly
```

- Terminal with file with the parameters fed in execution:
```
sp3trum_app -file file.in
```

- Graphical User Interface:
```
sp3trum_app -gui
```
 
<b><i>Powered by:</i></b><br>
 * Thiago Oliveira Lopes ( <a href="http://lattes.cnpq.br/8870631835172791"> Currículo Lattes</a> / <a href="https://twitter.com/thiago_o_lopes"> Twitter </a> / <a href="https://www.linkedin.com/in/thiago-lopes-1972b270"> Linkedin </a> / <a href="https://www.researchgate.net/profile/Thiago_Lopes2"> Research Gate</a>)
 * Daniel Francsico Scalabrini Machado ( <a href="http://lattes.cnpq.br/9791047274773689"> Currículo Lattes</a> / <a href="https://www.researchgate.net/profile/Daniel_Francisco_Machado">Research Gate</a>)
 * Professor Dr. Heibbe C. B. de Oliveira (<a href="http://lattes.cnpq.br/5995553993631378"> Currículo Lattes</a>  / <a href="https://www.researchgate.net/profile/Heibbe_De_Oliveira2">Research Gate</a>)
 * LEEDMOL Group (<a href="https://www.facebook.com/leedmol/" > Facebook </a>).
