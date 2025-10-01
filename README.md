# ⏱️Stopwatch Application

## Overview
This is a simple stopwatch application built using React. The app demonstrates the use of React hooks like `useState` and `useEffect` to manage state and side effects. The stopwatch tracks hours, minutes, and seconds and provides options to start, stop, and reset the timer.

## Features
- Display elapsed time in `hh:mm:ss` format.
- Buttons to:
  - **Start**: Begin the stopwatch.
  - **Stop**: Pause the stopwatch.
  - **Reset**: Reset the time to `00:00:00`.
- Proper button state management to avoid redundant actions.

## Technologies Used
- React
- JavaScript (ES6+)
- CSS 

## How It Works:-
1. **State Management**:
   - `time`: Tracks the total elapsed time in seconds.
   - `isRunning`: Boolean to indicate whether the stopwatch is running.

2. **Time Calculation**:
   - Hours, minutes, and seconds are calculated from the `time` state using basic arithmetic.

3. **Side Effects**:
   - The `useEffect` hook is used to start and clear a timer (`setInterval`) based on the `isRunning` state.

4. **Button Actions**:
   - `Start`: Sets `isRunning` to `true`, starting the interval.
   - `Stop`: Sets `isRunning` to `false`, stopping the interval.
   - `Reset`: Stops the timer and resets `time` to `0`.

## File Structure
```
src/
|-- components/
|   |-- Heading.jsx       # Displays the header of the app
|   |-- Timer.jsx         # Core stopwatch functionality
|
|-- App.jsx               # Main application component
|-- index.js              # Entry point of the application
|-- styles.css            # Basic styling
```

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/stopwatch-app.git
   ```

2. Navigate to the project directory:
   ```bash
   cd stopwatch-app
   ```

3. Install dependencies:
   ```bash
   npm install
   ```

4. Start the development server:
   ```bash
   npm start
   ```

5. Open the app in your browser at `http://localhost:3000`.

## Usage
- Press the **Start** button to begin the stopwatch.
- Press the **Stop** button to pause the stopwatch.
- Press the **Reset** button to reset the timer to `00:00:00`.

## Example Output
```
00:00:00
[Start] [Stop] [Reset]
```

## Future Enhancements
- Add a Lap feature to record intermediate times.
- Add a countdown timer mode.
- Improve UI with a styled interface.
- Add sound or visual notifications when certain milestones are reached.
