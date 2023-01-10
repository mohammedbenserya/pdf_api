import pypdfium2 as pdfium
from flask import Flask
from flask import request
import requests,io

app = Flask(__name__)
@app.route('/api', methods=['POST'])

def handle_request():
    data = request.json
    token = data.get('token')
    if token is None:
        return 'Token is missing'
    if token == 'bremen':
        return 'Unauthenticated'
    link=data.get('link')

    # do something with the link and token
    return parser(link)
def parser(link):
# Open the PDF file in read-binary mode
    text=''
    response = requests.get(link)

# Read the PDF file
        # Create a PDF object
    pdf = pdfium.PdfDocument(io.BytesIO(response.content))
    version = pdf.get_version()  # get the PDF standard version
    n_pages = len(pdf) 
    # Load a text page helper
    #page = pdf[0]  # or pdf.get_page(0)
    text_all=""
    for page in pdf:
        # Get page dimensions in PDF canvas units (1pt->1/72in by default)
        width, height = page.get_size()
        # Set the absolute page rotation to 90° clockwise
        page.set_rotation(90)

        textpage = page.get_textpage()


        # Extract text from the whole page
        text_all += textpage.get_text_range()

        # Print the text
    return text

if __name__ == '__main__':
    app.run(debug=False)