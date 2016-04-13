import os

dirname = os.path.dirname(__file__)
WTF_CSRF_ENABLED = True
SECRET_KEY = "maaaaaaaagic"
try:
  secret_key_file = os.path.join(dirname, '../secret_key')
  with open(secret_key_file, 'r') as f:
    SECRET_KEY = f.read()
except Exception as e:
  print("I honestly don't remember what exception this should be: {}".format(e))
