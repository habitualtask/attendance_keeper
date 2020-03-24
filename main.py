from flaskapp import app

context = ('../server.crt', '../server.key')
app.run(host='0.0.0.0', port=443, ssl_context=context)
