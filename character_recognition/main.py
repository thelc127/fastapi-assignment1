from fastapi import FastAPI, File, UploadFile
from ocr import process_image
from flask import flash, url_for, redirect, request, render_template
from requests import request
from werkzeug.utils import secure_filename
from fastapi.responses import HTMLResponse
import os
import connexion

app = FastAPI()


@app.route('/upload')
def upload_file():
    return render_template('upload.html')

content = """
<body>
<form action="/file/" enctype="multipart/form-data" method="post">
<input name="file" type="file" multiple>
<input type="submit">
</form>
</body>
    """


@app.route('/process', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        f.save(secure_filename(f.filename))
        return 'file uploaded successfully'


if __name__ == '__main__':
    app.run(debug=True)




# from fastapi import FastAPI, File, UploadFile
# from ocr import process_image
# from flask import flash, url_for, redirect, request
# from requests import request
# from werkzeug.utils import secure_filename
# from fastapi.responses import HTMLResponse
# import os
# import connexion
#
# app = FastAPI()
#
# # app = connexion.App(app)
# # app.add_api('swagger.yaml')
# # # app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
#
# UPLOAD_FOLDER = '/home/thelc127/Pictures'
# # app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
#
# def allowed_file(filename):
#     return '.' in filename and \
#            filename.rsplit('.', 1)[1].lower() in {'png', 'jpeg', 'jpg'}
#
# print(request.__module__)
#
#
# @app.route('/', methods=['GET', 'POST'])
# def upload_file(method):
#     if request.method == 'POST':
#         # check if the post request has the file part
#         if 'file' not in request.files:
#             flash('No file part')
#             return redirect(request.url)
#         file = request.files['file']
#         # if user does not select file, browser also
#         # submit an empty part without filename
#         if file.filename == '':
#             flash('No selected file')
#             return redirect(request.url)
#         if file and allowed_file(file.filename):
#             filename = secure_filename(file.filename)
#             file.save(os.path.join(UPLOAD_FOLDER, filename))
#             return redirect(url_for('uploaded_file',
#                                     filename=filename))
#     return '''
#     <!doctype html>
#     <title>Upload new File</title>
#     <h1>Upload new File</h1>
#     <form method=post enctype=multipart/form-data>
#       <input type="file" name= "file">
#       <input type=submit value=Upload>
#     </form>
#     '''
#     return HTMLResponse(content=content)
# # def main():
# #     content = """
# #     <body>
# #     <form action = /file/ method="post" enctype="multipart/form-data" >
# #     <input name="file" type="file" >
# #     <input type="submit" value=Upload>
# #     </form>
# #     </body>
# #         """
# #     return HTMLResponse(content=content)
#
