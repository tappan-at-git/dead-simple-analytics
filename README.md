# dead-simple-analytics
Dead simple analytics app for tracking and comparing shared metrics

To set up:
`cd dead-simple-analytics`
`./scripts/pkg_setup`
`workon dsa`
`./scripts/venv_setup`

Afterwards add these lines to your .bashrc to set up virtualenvwrapper automatically:
```
export WORKON_HOME=$HOME/.virtualenvs
source /usr/local/bin/virtualenvwrapper.sh
```

Instead of a direct path to the virtualenv's python (flask/bin/python, or
flask/bin/pip), you can also use `workon dsa` and then execute commands as
normal (so just python and just pip)
