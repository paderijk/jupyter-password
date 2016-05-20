# Jupyter Password

## About

This script adds a hashed password to protect your [Jupyter](http://jupyter.org/) notebooks.

## Prerequisites

* [Jupyter installation](http://jupyter.readthedocs.io/en/latest/install.html)

## How to use it

### Create initial jupyter config

You need to create a initial jupyter config:

```bash
jupyter notebook --generate-config
```

### Create password
```bash
python jupyter-password.py
```

So for example:
```
$ jupyter notebook --generate-config
Writing default config to: /home/pieter/.jupyter/jupyter_notebook_config.py
$ python jupyter-password.py
===========================================================================
Setting Jupyter additional configuration
===========================================================================
Please set a strong password
Enter password:
Verify password:
===========================================================================
Following will be added to /home/pieter/.jupyter/jupyter_notebook_config.py

  # Start of lines added by jupyter-password.py
  c.NotebookApp.password = u'sha1:e6a963af99fd:2c87c08ebb674db3a68c57726d30be929f240e5f'
  c.NotebookApp.open_browser = False
  # End lines added by jupyter-passwordd.py
===========================================================================
```
