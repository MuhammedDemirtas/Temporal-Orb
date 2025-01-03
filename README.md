# Temporal Orb: The Multi-Functional Timepiece

## Overview

Welcome to **Temporal Orb**, an innovative application blending the charm of an analog clock with modern features like weather updates and an interactive timer. Whether you're a tech enthusiast or someone who simply appreciates a good timekeeping tool, **Temporal Orb** offers something for everyone.

This application can be used in two ways:

1. **Executable Mode:** Simply double-click the provided `Temporal_Orb.exe` file to launch the application instantly.
2. **Source Code Exploration:** Dive into the Python code to understand how it works and customize it to your liking.

## Features

1. **Analog Clock:**

   - Displays a classic analog clock with real-time updates.
   - Hour, minute, and second hands are dynamically rendered for precise timekeeping.

2. **Digital Date and Time:**

   - Displays the current date and time in a clear, digital format.

3. **Weather Information:**

   - Fetches and displays weather updates using the `wttr.in` API.
   - Automatically hides weather info if no internet connection is detected.

4. **Interactive Timer:**

   - Set a custom countdown timer with just a few clicks.
   - A visual yellow line rotates around the clock face during the countdown.
   - Plays a cheerful sound and displays a notification when the timer ends.

## How to Use

### Executable Mode

1. Locate the `Temporal_Orb.exe` file provided in the project folder.
2. Double-click the file to launch the application instantly.
3. Enjoy all the features without needing to install Python or additional libraries.

### Source Code Exploration

If you'd like to explore or modify the source code:

1. Ensure you have Python installed on your system.
2. Install the required dependencies by running:
   ```bash
   pip install requests
   ```
3. Save the provided script as `Temporal_Orb.py`.
4. Run the script:
   ```bash
   python Temporal_Orb.py
   ```

## Detailed Features Walkthrough

### Analog Clock

- The analog clock is the centerpiece of **Temporal Orb**.
- It dynamically updates to reflect the current time.
- The hands are styled for clarity, with the second hand in red for easy identification.

### Digital Date and Time

- Positioned below the clock, the date and time are displayed in a legible digital format.
- The time updates every second, ensuring accuracy.

### Weather Updates

- At the top of the application, you’ll find the current weather conditions for your location.
- This feature relies on an internet connection. If none is available, the section remains hidden to maintain a clean interface.

### Timer

- Enter your desired countdown duration in seconds and click "Start Timer."
- A yellow line visually tracks the timer's progress around the clock face.
- When the timer concludes, a notification appears, and a series of cheerful beeps play.

## Files and Folder Structure

- `Temporal_Orb.py`: The main Python script for the application.
- `Temporal_Orb.exe`: Precompiled executable for instant use.
- `README.md`: Comprehensive documentation for the project.

## Notes

- The application is designed for Windows platforms due to the use of `winsound` for audio notifications.
- Feel free to extend the functionality or customize the design to suit your needs.

## Author

M. Demirtas

GitHub: [https://github.com/MuhammedDemirtas/Temporal-Orb-Python]

## License

This project is released under the MIT License. Feel free to use and modify it as you see fit!

