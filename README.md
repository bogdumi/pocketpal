# PocketPal

## Introduction

PocketPal is a microcontroller application that detects falling over using a MicroBit and sends a signal over serial (to be upgraded to radio/bluetooth in the future). If no cancellation is initiated within the countdown, the receiever then broadcasts a call and SMS request to Twilio in order to call emergency services and text closed ones.

## Usage

- Flash the MicroBit by dropping the ```accel_logging.py``` file on the microcontroller itself.

- Start the Python3 application by running ```python3 host.py``` in the terminal where the file is located.
