import os
import shutil

for file in os.listdir("./templates"):
    if file.endswith('.html') or file.endswith('.jinja'):
        shutil.copy(f"./templates/{file}", f"./static-website/{file}")

try:
    os.mkdir('./static-website/emperors')
except FileExistsError:
    pass

for file in os.listdir('./templates/emperors/'):
    if file.endswith('.html') or file.endswith('.jinja'):
        shutil.copy(f"./templates/emperors/{file}", f"./static-website/emperors/{file}")
try:
    os.mkdir('./static-website/static')
except FileExistsError:
    pass

try:
    os.mkdir('./static-website/static/css')      
except FileExistsError:
    pass
  
shutil.copy('./static/css/output.css', './static-website/static/css/output.css')