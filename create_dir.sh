#!/bin/bash

SOURCE_DIR="/Users/kishoriji/code/kripaluji-audio/slokas_location_in_lecture/Radha Tattva"
DEST_DIR="/Users/kishoriji/code/kripaluji-audio/slokas/Radha Tattva"

for file in "$SOURCE_DIR"/*.txt
do
  # Get the base name of the file
  BASENAME=$(basename "$file" .txt)

  # Create a new directory with the base name
  mkdir -p "$DEST_DIR/$BASENAME"
done