import React, { useEffect, useState } from "react";

function Timer() {
  const [time, setTime] = useState(0); // Time in seconds
  const [isRunning, setisRunning] = useState(false);

  useEffect(() => {
    let timer;
    if (isRunning) {
      timer = setInterval(() => {
        setTime((prevTime) => prevTime + 1);
      }, 1000);
    } else {
      clearInterval(timer);
    }

    return () => clearInterval(timer);
  }, [isRunning]);

  const startTime = () => setisRunning(true);
  const stopTime = () => setisRunning(false);
  const resetTime = () => {
    setisRunning(false);
    setTime(0);
  };

  // Calculate hours, minutes, and seconds
  const hours = Math.floor(time / 3600);
  const minutes = Math.floor((time % 3600) / 60);
  const seconds = time % 60;

  // Format the display
  const formatTime = (unit) => String(unit).padStart(2, "0");

  return (
    <div>
      <h2>
        {formatTime(hours)}:{formatTime(minutes)}:{formatTime(seconds)}
      </h2>
      <button onClick={startTime} disabled={isRunning}>
        Start
      </button>
      <button onClick={stopTime} disabled={!isRunning}>
        Stop
      </button>
      <button onClick={resetTime}>Reset</button>
    </div>
  );
}

export default Timer;
