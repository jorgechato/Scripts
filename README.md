# Scripts
In this repo I'm going to add my personal scripts, the ones I build and I
use. At the end this are useful scripts to make your life easier.

### Number.py
| arguments  | description  |
|:-:|:-:|
|   | Add 0 into filenames, only files named with number  |
| -r  | Replace the current filename to a number |
| -rf  | Replace the current folder name to a number |

##### <>
| before | after |
|:-:|:-:|
| 1.jpg  | 01.jpg  |
| 15.jpg | 15.jpg  |

##### <-r>
| before | after |
|:-:|:-:|
| 1-test.jpg  | 01.jpg  |
| 15.jpg | 02.jpg  |

##### <-rf>
| before | after |
|:-:|:-:|
| /git-folder | /0 |
| /test-folder  | /1 |

### Name.py
| arguments  | description  |
|:-:|:-:|
| -b [old name] -a [new name] | Change part of the filename to another |
| -r [old name] | Delete part of the filename |

##### <-r test>
| before | after |
|:-:|:-:|
| 1-test.jpg  | 1-.jpg  |
| test15.pdf | 15.pdf  |

##### <-b "hello world" -a github>
| before | after |
|:-:|:-:|
| test hello world.md  | test github.md  |
| hello world by jorge chato.mov | github by jorge chato.mov |
