# decode-non-injective-bit-matrix-encoding
A PyPy entry to a fastest-code contest: [Decoding a non injective bit matrix encoding](https://codegolf.codidact.com/posts/287925).

## Install
The PyPy documentation has [instructions on installing PyPy](https://doc.pypy.org/en/latest/install.html).

## PyPy version
This entry was developed using PyPy 7.3.11, corresponding to Python 3.9.16. This can be checked from the terminal using:

```text
pypy3 -V
```

## Run
An encoded matrix can be decoded by running `pypy3 decode.py` followed by space separated integers corresponding to the inputs described in the [contest post](https://codegolf.codidact.com/posts/287925).

### Example
The example from the contest post has the following input:

```text
4
1 1 1 1
1 1 1 1
0 2
0 2 2 0
1 2 2 1
1 2 2 1
```

This is run using:

```text
pypy3 decode.py 4 1 1 1 1 1 1 1 1 0 2 0 2 2 0 1 2 2 1 1 2 2 1
```

This results in output:

```text
1
0001
0010
0100
1000
```