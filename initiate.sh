python -m pip install -r requirements.txt --break-system-packages
mkdir static
mkdir static/css
touch static/css/input.css
echo '@import "tailwindcss";' >> static/css/input.css
touch static/css/output.css
touch templates/index.html
mkdir templates
npm init -y
npm install tailwindcss @tailwindcss/cli
npx @tailwindcss/cli -i ./static/css/input.css -o ./static/css/output.css --watch