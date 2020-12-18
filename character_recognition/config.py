
self.config = None
app = connexion.App(app)
app.add_api('swagger.yaml')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER