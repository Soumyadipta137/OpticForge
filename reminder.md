# OpticForge Roadmap (Resume-Oriented Version)

## Current Status ✅

Completed:

* Pillow wrapper (`Image` class)
* Internal NumPy storage
* Filter architecture
* Copy system
* Vignette filter
* NumPy vectorization
* Broadcasting fundamentals
* Git repository
* Basic backend abstraction (`xp`)

Major breakthrough achieved:

* Runtime reduced from ~40 seconds to ~1 second using vectorized NumPy operations.

---

# Phase 1 — Finish Core Architecture

Goal: Build a solid image-processing engine foundation.

## Implement

### Mask System

Support:

* Uniform opacity masks
* Gradient masks
* Image-based masks
* Generated masks

Functions:

* setMask()
* combineMask()
* invertMask()

---

### Layer System

Support:

* Foreground image
* Background image
* Opacity

Output:

finalImage = foreground × opacity + background × (1-opacity)

---

### Blend Modes

Implement:

* Normal
* Add
* Multiply
* Screen
* Overlay

---

### Backend Abstraction

Replace direct NumPy usage:

Instead of:

np.sqrt(...)
np.exp(...)
np.clip(...)

Use:

xp.sqrt(...)
xp.exp(...)
xp.clip(...)

through:

backend.py

Future:

NumPy ↔ CuPy switch by changing one file.

---

# Phase 2 — Real Image Processing

Goal: Learn industry-relevant image algorithms.

## Learn Convolution

Study:

* Kernel
* Sliding Window
* Convolution Matrix

Understand:

# Output(x,y)

Neighbourhood × Kernel

---

## Implement

### Blur

Box blur

### Gaussian Blur

Weighted blur

### Sharpen

Classic sharpening kernel

### Edge Detection

Sobel Operator

Very important.

Resume value: High.

---

### Bonus

Prewitt

Laplacian

Emboss

---

# Phase 3 — Performance Engineering

Goal: Learn optimization.

## Benchmark

Learn:

time.perf_counter()

cProfile

Compare:

* Pixel loops
* NumPy vectorization
* Future GPU implementation

Store benchmark results.

---

## Cache Expensive Computations

Example:

Vignette distance maps.

Compute once.

Reuse.

---

# Phase 4 — Professionalization

Goal: Make project resume-ready.

## Type Hints

Add everywhere.

Examples:

def copy(self) -> Image

pixelArray: np.ndarray

---

## Testing

Learn pytest.

Write tests for:

* copy()
* masks
* filters
* blending

---

## Documentation

Improve:

README.md

Add:

* Architecture diagram
* Examples
* Screenshots
* Benchmarks

---

# Phase 5 — GPU Path (Later)

Only after previous phases.

## Learn

CuPy

CUDA basics

GPU memory transfer

---

## Backend Upgrade

backend.py

CPU:

xp = numpy

GPU:

xp = cupy

---

## Benchmark

Compare:

CPU NumPy

vs

GPU CuPy

---

# Phase 6 — Advanced Effects

Only after convolution.

Interesting effects:

* Fisheye
* Polar Transform
* Swirl
* Ripple
* Kaleidoscope
* Domain Warping
* Distance Fields

These are more unique than standard filters.

---

# Separate Learning Track

Alongside OpticForge:

## Git

Learn:

* Branches
* Merge
* Revert
* Pull Requests
* Releases

---

## Linear Algebra

Focus on:

* Vectors
* Matrices
* Transformations

Useful for:

* Graphics
* Vision
* ML
* Image Processing

---

# Important Rule

Do NOT spend 100 hours making:

Brightness
Contrast
Grayscale
Filter #27

The return becomes very small.

After OpticForge reaches approximately 7.5/10 quality:

START A SECOND PROJECT.

A strong CV needs:

Project 1: Image Processing Engine
Project 2: Different Domain
Project 3: Different Domain

Not three image-processing projects.

---

# Immediate Next Step

1. Finish Mask System
2. Finish Layer System
3. Learn Convolution
4. Implement Sobel Edge Detection
5. Clean README
6. Move toward second project
