# m2x
Sample upconverter program using waifu2x, ffmpeg.

## Dependencies

* OS : Windows
* GPU : NVIDIA / AMD
* Python 3<br>
  https://www.python.org/downloads/windows/

## Test environment
* OS : Windows 10 64bit
* CPU : AMD Ryzen™ 5 2600X   
* GPU : AMD Radeon™ RX 580 (VRAM 8GB)
* RAM : 16GB
* Python 3.7.3

Procesing Speed

| Format | Length | Conversion  | Time   |
|:-------|:-------|:------------|:-------|
| mp4    | 60sec  | 480p → 720p | 17m32s |

## Usage
1. Put a video in "/res/input" folder.
2. Run "m2x.py" file.
3. The "res/tmp" folder stores files being processed.
4. The upconverted video is output to "res/output" folder.

## Configuration
* config.json
```
"waifu2x": {
    ...
    "--noise-level": 2,
    "--scale-ratio": 2
    ...
}
```

## Need fix
* Considering frame rate
* Refactor and comment

## Demo
![Elizabeth](https://raw.githubusercontent.com/ybs32/m2x/images/Elizabeth.jpg)