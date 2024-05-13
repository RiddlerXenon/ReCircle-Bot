import ssl

ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
ssl_context.load_cert_chain('ssl/cert.pem', keyfile='ssl/key.pem')
