Source: https://hex-rays.com/blog/igors-tip-of-the-week-33-idas-user-directory-idausr/

# `$IDAUSR` / `%IDAUSR%`

* On Windows: `%APPDATA%/Hex-Rays/IDA Pro`
* On Linux and Mac: `$HOME/.idapro`

See [here](https://hex-rays.com/blog/igors-tip-of-the-week-33-idas-user-directory-idausr/) and [here](https://www.hex-rays.com/products/ida/support/idadoc/1375.shtml).

> NB: Multiple entries are allowed, separated by `;` on Windows and `:` on Linux/Mac.

## `$IDAUSR`

* Cache files (ignored):
  * `proccache.lst` and `proccache64.lst`
  * `trusted_i64_list.bin` and `trusted_idb_list.bin`
* `ida.reg` (not on Windows)
* `idapythonrc.py` will be parsed _after_ IDAPython initialization
* [`shortcuts.cfg`](https://www.hex-rays.com/blog/igor-tip-of-the-week-02-ida-ui-actions-and-where-to-find-them/)

## `$IDAUSR/cfg`

* `ida.cfg`
* `hexrays.cfg`c

## `$IDAUSR/plugins`

### Caveats

* The basename is relevant for the plugin (i.e. extension stripped)
* Native extensions take precedence over `.idc` and `.py` ones

## Other locations inside `$IDAUSR`

* `$IDAUSR/ids/<platform-name>`
* `$IDAUSR/loaders`
* `$IDAUSR/procs`
* `$IDAUSR/sig/<arch>`
* `$IDAUSR/themes`
* `$IDAUSR/til/<arch>`

# Troubleshooting

Command line option `-zFC` should help to see the files/folders and order in which they get searched.