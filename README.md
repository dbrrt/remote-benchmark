# Remote Benchmark

## Laconic

This project has been created to retrieve running time (s) of multiple bash commands executed on a remote server using Python3/Paramiko.

## Get Started

### Prepare credentials / hostname

- `cp .env.tpl .env`

### Installing dependencies

- `make install`

### Update execution instruction (from app.py)

```python
instructions = [
    './myProgram.sh',
    './anotherProgram.sh',
    'python3 app.py'
]
```

### Start benchmark (silent mode `-s`)

`make -s start`


### Output sample

`{'lines_cnt': 15, 'execution_cmd': 'ls -l', 'execution_time': 0.527428150177002}`

## License

MIT License

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

## Credits

@dbrrt - David Barrat