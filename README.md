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

## Known Issues
Bullet points are done badly at this point, instead of being added automatically in the HTML, they are added as unicode filled circles (•) at the beginning of each point.
Similarly, footnote numbering is done manually as well, and at the bottom of the document (ㅤ) should be placed before a number, then the reference. Note that (ㅤ) is not a space, it is a special invisible character, so it should be copy-pasted from within the brackets (ㅤ).

## Contributing
If you are a scholarly person who does not know how to use this newfangled technology such as GitHub and python, just shoot me an email at jamesaglynn10@gmail.com with your page following the styling guide below and I'll do my best to help add it to the website.

If you wish to contribute a new page for an emperor please follow these steps (this assumes you know how to use google and have a basic understanding of how git and github is used):
1. Fork the git repository
2. In the `static/markdown` directory add a new page with the emperor's name and the file extension `.md`. If you don't know what markdown is, ~~what are you doing here~~ [this website](https://www.markdownguide.org) may be of use to you. Try and follow this general scaffold:
```
# **EMPEROR NAME** [Bolded H1]
#### *EMPEROR LATIN NAME* [Italics H4]

## IN BREVI [H2]
#### *In Short* [Italics H4]
A short 2-5 sentence summary of the Emperor's life. Footnotes are generally not needed, so long as the same information is mentioned *with* footnotes in the longer summary.

## VITA ET FAMILIA [H2] (Be sure either to footnote the heading if all information below is from one source, or footnote each piece of info if from multiple sources)
#### *Life and Family* [Italics H2]
- DIES NATALIS: X
- PATER: X
- MATER: X
- LIBERI: X
- DIES MORTIS: X

## LUDIBUNDA VERA [H2]
#### *Fun Facts* [Italics H4]
 - • Fact 1[^1] [List] (Note the filled circle issue as mentioned above, and be sure to reference your source)
 - • Fact 2[^2]

## IN LONGUM [H2]
#### *In Long* [Italics H2]
A much longer summary of the emperor's life, generally 2-5 paragraphs in length. Be sure to[^3] reference[^4] your sources in the footnotes.

[^1]: ㅤ1. Be sure also to note the issue above with the footnotes needing an invisible character that **is not** a space, then a number, then the reference.
[^2]: ㅤ2. References are chicago style, although currently they are not perfect either, as I kind of mutilated it during the course of the project.
[^3]: ㅤ3. James Glynn, REP Style Guide (San Francisco: Github Publishing, 2025), 5:2 (BOOK)
[^4]: ㅤ5. Ibid, 5:4
```
3. Add a picture of a bust of the emperor, cropped to 250x250 pixels, preferably with the same background as the rest of them, `static/emperors-background.png`. Using remove.bg with the magic background function will also offer this photo as a background. Save this as `static/emperor-name.png`.
4. Edit `templates/index.jinja` to add the new emperor link.

```
<div class="flex justify-center items-center flex-col">
    <img src="{{url_for('static', filename='emperor-name.png')}}" alt="Emperor Name" class="emperor-button"  onclick="location.href='/emperor/name-of-md-file-without-extension'">
    <p>Emperor Name</p>
</div>
```
5. Add the new emperor to the `template/header.jinja` file
```
<div class="flex items-center flex-col">
    <img src="{{url_for('static', filename='emperor-name.png')}}" alt="Emperor Name" class="emperor-button-small"  onclick="location.href='/emperor/name-of-md-file-without-extension'">
    <p>Emperor Name</p>
</div>
```
6. Setup the development environment as mentioned above, and run `npm run build-css` and `npm run dev-server`, navigate to `http://127.0.0.1:4306` to make sure your page appears.
7. Open a new pull request (you can figure that out on your own) with your code.