from flask import Flask, render_template, render_template_string, request, redirect
import os
import markdown
from markdown_it import MarkdownIt

app = Flask(__name__)
md = MarkdownIt("commonmark").enable('table')

def save_markdown_page(markdown_file_path: str, output_file: str):
    """
    Takes the name of a markdown file, and returns a template to render on the page

    Args:
        markdown_name str: The name of the markdown file, without .md suffix
    """

    markdown_name = markdown_file_path.split("/")[-1].replace(".md", "")

    mrkdown = md.render(open(f'{markdown_file_path}', 'r').read())
    html_page = """
           <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <link href="{{{{url_for('static',filename='css/output.css')}}}}" rel="stylesheet">
            </head>
            <body>
                {{% include 'header.jinja' with context %}}
                <!-- Start of {0}.jinja -->
            <article class="prose prose-slate m-6 p-2 mx-auto max-w-7xl text-center">{2}</article>

            <!-- End of {0}.jinja -->
            {{% include 'footer.jinja' with context %}}
            </body>
            </html>
           """.format(markdown_name, markdown_name.title().replace('-', ' ').replace('_', ' '), mrkdown)
    
    with open(output_file, "w") as f:
        f.write(html_page)

@app.route('/')
def index():
    source = request.args.get('source') # Only set if redirected from a NFC tag or in other very specific circumstances
    return render_template('index.jinja', source=source)

@app.route('/emperor/<emperor>')
def emperor(emperor):
    files = os.listdir("templates/emperors/")
    for file in files:
        if file == emperor + ".html" or file == emperor + ".htm" or file == emperor + ".jinja":
            return render_template("emperors/" + file)
    return render_template("404.jinja", reason=f"Emperor page for '{emperor}' not found"), 404

@app.route('/easter-egg')
def easter_egg():
    return redirect("https://www.youtube.com/watch?v=v8enlTBXR5Y", code=302)

if __name__ == "__main__":
    for md_page in os.listdir("./static/markdown/"):
        if md_page.endswith(".md"):
            save_markdown_page(f"./static/markdown/{md_page}", f"./templates/emperors/{md_page.replace(".md", ".html")}")

    app.run(debug=True, port=4305)