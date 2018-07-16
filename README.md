# resize-asset
Python script to resize an asset to multiple sizes

## Installation

Python 3 and Pillow are required for the script to work.

1. Install Pillow through PIP like so, `pip3 install pillow`
2. Copy the script in a safe place such as a hidden scripts folder in your home directory, `mkdir -p ~/.scripts/ && cp resize-asset ~/.scripts/`
3. Mark the newly copied script as executable, `chmod +x ~/.scripts/resize-asset`
3. Add the script folder to your PATH by placing the following line at the bottom of the your terminal profile, `export PATH=~/.scripts/:$PATH`
4. Reopen your terminal and try and run `resize-asset`

Alternatively if you don't want to install the script you can run it like so, `./resize-asset`.

## Usage

The script takes 3 required arguments,

* `-f`, the input image
* `-o`, the desired name of the output image, the file extension must NOT be included
* `-w` / `-h`, (width and height in pixels) either one or the other OR both can be used

Optional arguments include...

* `-c`, the amount of sizes outputted, e.g. `-c 3 -w 50 -h 50` will produce three images, one 50x50, one 100x100 and one 150x150. The files outputted have a `@[MULTIPLE]`extension given (e.g. `@2` or `@3`).

### Examples

#### Resizing an image

`resize-asset -f icon.png -o resized-icon -w 50 -c 3`

* `icon.png` is the input image
* `resized-icon` will be the output file
* A width of `50px` is desired
* `3` resized images will be outputted

The command will produce these three images.

```
├── resized-icon.png (50px x 50px)
├── resized-icon@2.png (100px x 100px)
└── resized-icon@3.png (150px x 150px)
```
