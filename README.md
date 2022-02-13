# SHUTUP - Stop python warnings, no matter what!

Sometimes you just can't mute python warnings. Use this library to solve this.

## Installation

```bash
pip install shutup
```

## Basic Use

On the beginning of your code (before you import other things), add this line:

```python
import shutup; shutup.please()
```

That's it. Enjoy the silence :)

---

## Contributions

If your warnings were not silenced, please open an issue. PRs, ideas and other contributions are also welcome.

---

## Other features

### Unmutting
You can use:

```python
shutup.jk()
```

to re-enable warnings if you need them.

### Clean aliases
You can also use:

```python
shutup.mute_warnings()
shutup.unmute_warnings()
```

They are the same as the functions above, but they have cleaner (but arguably less funny) names.

### Context Managers
Context managers are also supported:

```python
import shutup
shutup.mute_warnings()
# Annoying code

with shutup.unmute_warnings:
    # code that doesn't cry wolf
```

Note that you shouldn't use `()` in a context manager:

```python
with shutup.mute_warnings: # correct
with shutup.mute_warnings(): # wrong
```

At the end of the context manager warnings 'muteness' will return to the state before entering.

### Finally, this package needs its own warning! 🤦

Warning: Note that muting and unmutting is not a thread safe operation.
