from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/topfive')
def topfive():
    topfive = [
        {
            'scripture': 'John 3:16',
            'text': 'For God so loved the world, that he gave his only begotton Son, that whosoever believeth in him should not perish, but have eternal life.',
        },
        {
            'scripture': 'Jeremiah 29:11', 
            'text': 'For I know the thoughts that I think toward you, saith the LORD, thoughts of peace, and not of evil, to give you an expected end.'
        },
        {
            'scripture': 'Isaiah 40:31',
            'text': 'But they that wait upon the LORD shall renew their strength; they shall mount up with wings as eagles; they shall run, and not be weary; they shall walk and not faint.'
        }, 
        {
            'scripture': 'Deuteronomy 31:6',
            'text': 'Be strong and courageous. Do not be afraid or terrified because of them, for the Lord your God goes with you; he will never leave you nor forsake you.'
         
        },
        {
            'scripture': 'Psalm 96:4',
            'text': 'For great is the Lord, and greatly to be praised; he is to be feared above all gods.'
        }, 
        {
            'scripture': 'Romans 8:18',
            'text': 'For I consider that the sufferings of this present time are not worth comparing with the glory that is to be revealed to us.'
        }, 
    ]
    return render_template('topfive.html', verses=topfive)

app.run(debug=True)