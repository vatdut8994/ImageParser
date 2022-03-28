from flask import Flask, render_template, request
from bs4 import BeautifulSoup
import requests

app = Flask(__name__)
count = 0

@app.route('/')
def asdf():
    return render_template('index.html')

@app.route('/images', methods=['GET', 'POST'])
def asdlfkj():
    global count
    if request.method == 'POST':
        inp = request.form['search']
        if inp == '':
            count = int(open('count.txt', 'r').read())
            inp = open('search.txt', 'r').read()
        else:
            open('count.txt', 'w').write('0')
            open('search.txt', 'w').write(inp)
            count = int(open('count.txt', 'r').read())
        next_button = request.form.get('next_btn', False)
        back_button = request.form.get('back_btn', False)
        # back_button = request.form['back_btn']
        source = requests.get(f"https://www.google.com/search?tbm=isch&q={inp.replace(' ', '+')}").text
        soup = BeautifulSoup(source, 'html.parser')
        images = soup.find_all('img')
        images = images[4:-1]
        try:
            if next_button == 'Next':
                count += 1
                open('count.txt', 'w').write(str(count))
            elif back_button == 'Back':
                count -= 1
                open('count.txt', 'w').write(str(count))
        except:
            pass
        imgUrl = images[count].get('src')
        print(imgUrl)
        return render_template('index.html', image_link=imgUrl)

if __name__ == "__main__":
    app.run(debug=True)
