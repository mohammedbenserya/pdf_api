import PyPDF2
from flask import Flask
from flask import request
import requests,io

app = Flask(__name__)
@app.route('/api', methods=['POST'])

def handle_request():
    print(request.json)
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
    pdf = PyPDF2.PdfFileReader(io.BytesIO(response.content))

    # Iterate over every page
    for page in range(pdf.getNumPages()):
    # Extract the text from the page
        text += pdf.getPage(page).extractText()

        # Print the text
    return text

if __name__ == '__main__':
    app.run(debug=False)