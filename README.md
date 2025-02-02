# Clone and added Pure python implementation.

This is a fork of https://github.com/openai/tiktoken with the tokenizer available as a pure python implementation. 
You can use it locally like this (after pip install -e .) 

```
import tiktoken.registry as registry
from tiktoken.registry import _find_constructors
from tiktoken.core import Encoding

_find_constructors()
constructor = registry.ENCODING_CONSTRUCTORS['cl100k_base']
params = constructor()
enc = Encoding(**params, use_pure_python=True)
enc.encode("hello world")
```

The port to python (from Rust) is 99% done with the help of GPT4 and these are the tests I did
(so use it at your own risk but it should be trivial to compare both across a much diverse charset and
phrases)

```
Encoding for 'a': [64]
Encoding for '!': [0]
Encoding for '1': [16]
Encoding for '&': [5]
Encoding for 'hello': [15339]
Encoding for 'world': [14957]
Encoding for 'python': [12958]
Encoding for 'rust': [36888]
Encoding for 'hello world': [15339, 1917]
Encoding for 'rust is fast': [36888, 374, 5043]
Encoding for '.': [13]
Encoding for ',': [11]
Encoding for '?': [30]
Encoding for '!': [0]
Encoding for 'Hello, world!': [9906, 11, 1917, 0]
Encoding for 'How's it going?': [4438, 596, 433, 2133, 30]
Encoding for '
': [198]
Encoding for '	': [197]
Encoding for '0': [15]
Encoding for '1': [16]
Encoding for '9': [24]
Encoding for '10': [605]
Encoding for '100': [1041]
Encoding for '12345': [4513, 1774]
Encoding for '0.1': [15, 13, 16]
Encoding for '3.14': [18, 13, 975]
Encoding for '10.001': [605, 13, 4119]
Encoding for 'abc123': [13997, 4513]
Encoding for '42rocks': [2983, 299, 14895]
Encoding for 'HELLO': [51812, 1623]
Encoding for 'World': [10343]
Encoding for 'Python': [31380]
Encoding for 'helloWorld': [15339, 10343]
Encoding for 'rust_rocks': [36888, 27706, 14895]
Encoding for '✓': [38798, 241]
Encoding for '❤️': [49633, 97, 31643]
Encoding for '©': [20644]
Encoding for 'hola': [71, 8083]
Encoding for 'こんにちは': [90115]
Encoding for 'Привет': [54745, 28089, 8341]
Encoding for 'The quick brown fox jumps over the lazy dog.': [791, 4062, 14198, 39935, 35308, 927, 279, 16053, 5679, 13]
Encoding for '': []
Encoding for ' ': [220]
Encoding for '	': [197]
Encoding for '
': [198]
Encoding for '@@@': [19741, 31]
Encoding for '###': [14711]
```


