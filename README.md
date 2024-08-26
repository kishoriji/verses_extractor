# VerseExtractor
Automated Segmentation of Sanskrit and Hindi Verses from Lectures by Jagadguru Shri Kripalu Maharaj

## Repository Content

This repository contains code designed to automatically segment and extract Sanskrit and Hindi verses from lectures. The tool focuses on identifying and isolating verses from sacred texts such as the Ramayana, Bhagavad Gita, Bhagwat Purana, and various Shastras, creating smaller MP3 files for each verse.

## Features

    Targeted Verse Extraction: Identifies and extracts verses from the Ramayana, Gita, Bhagwat, Shastra, and other sacred texts during lectures based on a txt file provided with start end of verses.
    Language-Specific Segmentation: Focuses on Sanskrit and Hindi verses, ensuring accurate and meaningful segmentation.
    Output in MP3 Format: Each extracted verse is saved as a separate MP3 file, preserving the original audio quality.
    Customizable Parameters: Allows users to fine-tune the extraction criteria, such as silence detection thresholds and minimum verse length.

## Purpose

The primary purpose of this tool is to facilitate the extraction and preservation of key verses from lectures, making it easier to study, share, and reflect upon the teachings contained within these sacred texts. This tool is particularly useful for educators, students, and spiritual practitioners.
Usage

Clone the Repository:
```bash
git clone https://github.com/kishoriji/verses_extractor.git
```
Install Dependencies: Ensure the required dependencies are installed via pip or another package manager.

```bash
pip install -r requirements.txt
```
Run the Script: Execute the script with the desired parameters to extract verses from your lecture audio files.

```bash
    python slokas_audio_extractor.py
```

## Contributing

Contributions are welcome! If you have suggestions for new features, optimizations, or bug fixes, please submit a pull request. Ensure your contributions align with the goals and standards of the project.
