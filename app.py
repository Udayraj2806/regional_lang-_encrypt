from flask import *
from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import AESencrypt as E
import AESdecrypt as D

app = Flask(__name__)


@app.route('/home')
def index():
    return render_template('index.html')


@app.route('/encrypt')
def encrypt():
    return render_template('encryption.html')


@app.route('/getText', methods=['GET', 'POST'])
def getText():
    # response = make_response('', 204)
    # final_out = open("output.txt", "r", encoding='utf-8')
    # encry=final_out.read()
    if (request.method == "POST"):
        data = request.form.get("text")
        # print(request.data)
        # print(type(data))
        file1 = open("plaintext1.txt", "w", encoding="utf-8")
        file1.write(data)
        file1.close()
        print('data updated')
        E.encrypt()
        print("Encrypted")
        # D.decrypt()
    final_out = open("ciphertext.txt", "r", encoding='utf-8')
    encry = final_out.read()
    return render_template('encryption.html', encryptText=encry)


@app.route('/getDeText', methods=['GET', 'POST'])
def getDeText():
    if (request.method == "POST"):
        data = request.form.get("text")
        print(data)
        print(type(data))
        file1 = open("ciphertext.txt", "w", encoding="utf-8")
        file1.write(data)
        file1.close()
        print("Unable")
        D.decrypt()
        print("Dencrypted")
    final_out = open("output.txt", "r", encoding='utf-8')
    encry = final_out.read()
    return render_template('encryption.html', decryptText=encry)


@app.route('/upload')
def upload():
    return render_template('encryption.html')


@app.route('/uploader', methods=['GET', 'POST'])
def uploader():
    if request.method == 'POST':
        f = request.files['file']
        f.save(secure_filename(f.filename))
        print(f.filename)
        f12 = open(f.filename, "r", encoding="utf-8")
        data=f12.read()
        f12.close()
        file1 = open("plaintext1.txt", "w", encoding="utf-8")
        file1.write(data)
        file1.close()
        print('data updated')
        E.encrypt()
        print("Encrypted")
    final_out = open("ciphertext.txt", "r", encoding='utf-8')
    encry = final_out.read()
    return render_template('encryption.html', encryptText=encry)
    

# @app.route('/getfileText', methods=['GET', 'POST'])
# def getfileText():
#     # response = make_response('', 204)
#     # final_out = open("output.txt", "r", encoding='utf-8')
#     # encry=final_out.read()
#     if (request.method == "POST"):
#         f = request.files['file']
#         f.save(secure_filename(f.filename))
#         return render_template('encryption.html', encryptText="Text")
#         # print(f)
#     #     file1 = open("plaintext1.txt", "w", encoding="utf-8")
#     #     file1.write(data)
#     #     file1.close()
#     #     print('data updated')
#     #     E.encrypt()
#     #     print("Encrypted")
#     #     # D.decrypt()
#     # final_out = open("ciphertext.txt", "r", encoding='utf-8')
#     # encry = final_out.read()
    return render_template('encryption.html', encryptText="Text")

    # need posted data here


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


if __name__ == '__main__':
    app.run(debug=True)
