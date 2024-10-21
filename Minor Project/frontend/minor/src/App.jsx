import React, { useRef } from 'react';
import Header from './components/Header';
import Footer from './components/Footer';
import PresentationControlSection from './components/PresentationControlSection';
import InteractiveGestureWindow from './components/InteractiveGestureWindow';

function App() {
  const gestureSectionRef = useRef(null);

  const handleGetStarted = () => {
    if (gestureSectionRef.current) {
      gestureSectionRef.current.scrollIntoView({ behavior: 'smooth' });
    }
  };

  const handleTryPresentationControl = async () => {
    try {
      await doHeavyTask();
      alert('Presentation control started!');
    } catch (error) {
      console.error('Error:', error);
    }
  };

  const doHeavyTask = () => {
    return new Promise((resolve) => {
      setTimeout(() => {
        resolve();
      }, 2000);
    });
  };

  const handlePreviousSlide = () => {
    alert('Previous Slide');
  };

  const handleNextSlide = () => {
    alert('Next Slide');
  };

  const handleStartNow = () => {
    alert('Gesture control activated!');
  };

  return (
    <div className="bg-gray-100 min-h-screen">
      <Header onGetStarted={handleGetStarted} />
      <PresentationControlSection
        onPreviousSlide={handlePreviousSlide}
        onNextSlide={handleNextSlide}
        onTryPresentationControl={handleTryPresentationControl}
      />
      <InteractiveGestureWindow ref={gestureSectionRef} />
      <Footer onStartNow={handleStartNow} />
    </div>
  );
}

export default App;



