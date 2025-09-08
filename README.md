# roman-emperors-website
## Running
*Assumes you have `python3` and `pip` installed.*
To run the server with the pre-built website just run `pip install -r requirements.txt`, `python3 principale.py`. The webserver runs on 0.0.0.0 on port 4305, so it's available on `127.0.0.1:4305` and to other computers on the same network.

## Development
*Assumes you have `python3`, `pip` and `npm` installed.*
For development, run `pip install -r requirements.txt`, `npm i`. Then run `npm run build-css` in one terminal, and have `npm run dev-server` in another. `build-css` will watch the html and jinja files for any changes and regenerate the css source files automatically. The `dev-server` will restart the server, regenerating the html files from the markdown source whenever it is detected that they change.

## Docker
*Assumes you have `docker` and `docker compose` installed.*
If it's easier for you to run it in a docker container, I have a dev version setup in docker-compose, to run it, run `docker compose up` then head to `127.0.0.1:4306` to see the website.