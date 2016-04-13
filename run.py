#!flask/bin/python
from argparse import ArgumentParser
from app import app

def get_argument_parser():
  ap = ArgumentParser(description="Run the dead-simple-analytics webapp")
  ap.add_argument("-p", "--port", type=int, default=48879,
                  help="Which port to serve the webapp on.")
  ap.add_argument("-e","--external", action="store_true",
                  help="Serve the webapp externally (host=0.0.0.0) or "\
                       "local-only (host=localhost)")
  ap.add_argument("-d", "--debug", action="store_true",
                  help="Very dangerously run with the Flask debugger. Note: "\
                       "very dangerous.")
  return ap

def main(argv=None):
  parser = get_argument_parser()
  args = parser.parse_args(argv)
  if args.external:
    HOST="0.0.0.0"
  else:
    HOST="localhost"
  PORT=args.port
  DEBUG=args.debug
  app.run(host=HOST, port=PORT, debug=DEBUG)

if __name__=="__main__":
  main(["-p", "48879", "-d"])
