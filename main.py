import argparse
import sys
import os
import compressor

def main():
    parser = argparse.ArgumentParser(description="Compress or decompress text using word-to-int binary encoding.")
    parser.add_argument("mode", choices=["compress", "decompress"], help="Mode of operation.")
    parser.add_argument("input", help="Input file path.")
    parser.add_argument("output", help="Output file path (compressed .bin or decompressed .txt).")

    args = parser.parse_args()

    if args.mode == "compress":
        with open(args.input, "r", encoding="utf-8") as f:
            text = f.read()

        counter_dict = compressor.word_counter(text)
        sorted_dict = compressor.sort_dict_by_values(counter_dict)
        code = compressor.create_code(sorted_dict)

        compressor.compress_to_binary_file(text, code, args.output)

        print("Compression complete.")
        print("Original size:", os.path.getsize(args.input), "bytes")
        print("Compressed size:", os.path.getsize(args.output), "bytes")

    elif args.mode == "decompress":
        decompressed = compressor.decompress_from_binary_file(args.input)
        with open(args.output, "w", encoding="utf-8") as f:
            f.write(decompressed)

        print("Decompression complete.")
        print("Decompressed output saved to:", args.output)

if __name__ == "__main__":
    main()