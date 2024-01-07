[![codecov](https://codecov.io/gh/DAtek/life-of-photo/branch/master/graph/badge.svg?token=L26G7G8CIW)](https://codecov.io/gh/DAtek/life-of-photo)
<a href="https://github.com/psf/black"><img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>
<a href="https://github.com/psf/black/blob/main/LICENSE"><img alt="License: MIT" src="https://black.readthedocs.io/en/stable/_static/license.svg"></a>

# Life Of Photo

This little app runs _Game Of Life_ simulation on black and white images.

![tree.gif](https://github.com/DAtek/life-of-photo/blob/master/tree.gif)

### Usage

1. Resize a photo / image so the biggest size becomes ~600 px (otherwise the simulation will be slow)
2. Make the image greyscale
3. Turn the contrast to maximum until only white and black pixels exist
4. Run `life-of-photo <path_of_your_image>`
5. Hold down any button but `s` or `q` to keep the simulation running
