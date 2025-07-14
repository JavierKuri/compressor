# compressor

An attempt to create a text file compressor in Python. The idea is to create variable length codes for each word and to give the shortest ones to the most frequent words in order to hopefully encode everything while saving space and without losing information.

## Usage

The file compressor and decompressor can be used via CLI directly in the root directory of the project. The syntax for usage is:

```bash
#For compressing a file
python main.py compress "path to input file" "path to output file"

#For decompressing a file (only works for files compressed with this compressor)
python main.py decompress "path to compressed file" "path to output file"
```