# sqlalchemy dmypy crash example

## How to trigger the crash

- Create and enable environment "env"
- Install requirements from requirements.txt
- Open up a console
- Run `dmypy start`
- Run `dmypy run app.py`
- No error should show up
- Go into the app.py file and edit a string (or anything meaningful)
- Run `dmypy run app.py`
- Now the following crash should appear:
```
Daemon crashed!
Traceback (most recent call last):
  File "mypy\dmypy_server.py", line 229, in serve
  File "mypy\dmypy_server.py", line 272, in run_command
  File "mypy\dmypy_server.py", line 331, in cmd_run
  File "mypy\dmypy_server.py", line 393, in check
  File "mypy\dmypy_server.py", line 568, in fine_grained_increment_follow_imports
  File "mypy\server\update.py", line 245, in update
  File "mypy\server\update.py", line 328, in update_one
  File "mypy\server\update.py", line 388, in update_module
  File "mypy\server\astdiff.py", line 164, in snapshot_symbol_table
  File "mypy\server\astdiff.py", line 224, in snapshot_definition
  File "mypy\server\astdiff.py", line 160, in snapshot_symbol_table
TypeError: str object expected; got None
```

Restarting the daemon works, then on the next edit and save it happens again.

## Fixing the issue

Go to `env\Lib\site-packages\sqlalchemy\ext\mypy\apply.py` and add in the function `_apply_placeholder_attr_to_class` (bottom of the file) the following line:
```
    var = Var(attrname)
    # this line 👇🏻
    var._fullname = cls.fullname + "." + attrname
    # this line ☝🏻
    var.info = cls.info
    var.type = type_
    cls.info.names[attrname] = SymbolTableNode(MDEF, var)
```

Now the error doesn't occur when repeating the protocol described above.

This process has been tested succesfully under Windows 10 (Powershell) and Linux (bash) through WSL.
