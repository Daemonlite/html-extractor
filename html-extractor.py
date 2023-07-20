from flask import Flask, render_template, request
from bs4 import BeautifulSoup
import requests

app = Flask(__name__)

# Route to display the input form
@app.route('/')
def index():
    return render_template('index.html')

# Route to handle form submission and display the extracted HTML
@app.route('/extract', methods=['POST'])
def extract_html():
    url = request.form['url']
    try:
        response = requests.get(url)
        response.raise_for_status()
        html_content = response.text

        # Parse the HTML content using Beautiful Soup
        soup = BeautifulSoup(html_content, 'html.parser')
        extracted_html = soup.prettify()  # If you want to prettify the output

        return render_template('result.html', extracted_html=extracted_html)
    except requests.exceptions.RequestException as e:
        return f"Error: {e}"

if __name__ == '__main__':
    # Specify the desired port number here (e.g., 8000)
    port = 8000
    app.run(port=port,debug=True)
    app.run()

