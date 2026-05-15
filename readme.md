# Mathematical Image Transformation Engine

## Core Idea

A graphics and image-processing sandbox focused on:

* mathematical transformations
* coordinate remapping
* optics simulation
* procedural filters
* signal-processing-inspired image effects

NOT a generic photo editor.

The goal is:

* math-heavy visuals
* procedural graphics
* graphics programming practice
* future bridge toward rendering engines/shaders/OpenGL

---

# Current Features Implemented

## Basic Filters

* Grayscale
* Negative
* Vignette

## Experimental Effects

* Edge Glow / Local Contrast Enhancement
* Physically-inspired FishEye Lens Distortion

## Concepts Already Learned

* Pixel access using Pillow
* Coordinate remapping
* Radial distance fields
* Image-space transformations
* Implicit vs explicit equations
* Geometric optics derivation
* Branch extraction from quadratics
* Radial projection systems
* Continuous distortion fields

---

# Project Direction

## DO NOT TURN THIS INTO:

* generic photo editor
* sticker app
* meme generator
* GUI-heavy Photoshop clone

That direction becomes cliché and less technical.

---

# Intended Direction

## Procedural Mathematical Graphics Engine

Focus Areas:

* coordinate transformations
* optical distortions
* procedural image manipulation
* mathematically-derived effects
* signal-processing filters
* experimental rendering techniques

---

# Architecture Plan

## 1. Core Image Engine

Responsible for:

* image loading
* pixel buffers
* coordinate sampling
* image export
* filter pipeline

---

## 2. Modular Filter Pipeline

Example:

image = fisheye(image)
image = vignette(image)
image = bloom(image)

Goal:

* stackable effects
* modular architecture
* reusable functions

---

## 3. Spatial Transformation System

Core abstraction idea:

applySpatialTransform(image, func)

Where:
func(x,y) -> (X,Y)

This becomes the foundation for:

* fisheye
* swirl
* kaleidoscope
* warping
* tunnel effects
* future shaders

---

# Features To Implement Next

## Coordinate Distortions (Highest Priority)

### Swirl / Vortex

Rotate coordinates based on radial distance.

### Wave Distortion

Sinusoidal displacement:
X = x + A*sin(y/f)

### Bulge / Pinch

Radial scaling field.

### Kaleidoscope

Angular symmetry mapping.

### Polar Transform

Cartesian <-> Polar remapping.

### Tunnel Effect

Radial logarithmic mapping.

### Mirror Symmetry Modes

Reflection-based recursive visuals.

### Recursive Distortion

Distort output repeatedly into itself.

---

# Image Processing / Signal Processing

## Sobel Edge Detection

Directional edge extraction using kernels.

## Emboss Filter

Relief-style shading effect.

## Sharpen Filter

Local contrast amplification.

## Gaussian Blur

Weighted convolution blur.

## Bloom

Spread bright pixels outward.

## Chromatic Aberration

RGB channels sampled at shifted coordinates.

## Motion Blur

Directional averaging.

## Noise Systems

Random displacement/grain/static.

---

# Advanced Mathematical Modes

## Mandelbrot Overlay

Use complex-plane iteration counts.

## Complex Number Mapping

Map pixels through:

* z²
* exp(z)
* log(z)
* Möbius transforms

## Logarithmic Image Warping

Recursive rotational transforms.

## Fourier-Based Experiments

Frequency-domain image modifications.

## Conformal Mappings

Angle-preserving coordinate transforms.

## Stereographic Projection

Sphere-plane mappings.

---

# Long-Term Evolution

## Phase 1

CPU-based image manipulation
(Current)

## Phase 2

Realtime preview system

## Phase 3

GPU/OpenGL shaders

## Phase 4

Procedural rendering engine

## Phase 5

Physics + rendering integration

---

# GUI Philosophy

Minimal technical interface:

* dark theme
* live preview
* sliders
* parameter stack
* transformation pipeline

Avoid:

* clutter
* stickers
* social-media style UI

---

# Important Mathematical Concepts To Explore

* Coordinate Spaces
* Polar Coordinates
* Complex Numbers
* Convolutions
* Distance Fields
* Projection Geometry
* Signal Processing
* Fourier Transform
* Ray Mapping
* Sampling Theory
* Distortion Fields

---

# Potential Final Project Names

* Mathematical Image Transformation Engine
* Procedural Optics Sandbox
* Coordinate Space Renderer
* Procedural Distortion Engine
* Mathematical Graphics Playground
* Optics and Image Transformation Sandbox

---

# Most Important Realization

Most graphics effects are:

1. Coordinate manipulation
2. Color-space manipulation

Understanding those two deeply leads naturally toward:

* shaders
* rendering
* game engines
* procedural graphics
* computer vision
* physics visualization

---

# Current Status

The project already contains:

* custom math
* geometric derivations
* physically-inspired mapping
* procedural rendering logic

This is already significantly more interesting than a basic filter app.
