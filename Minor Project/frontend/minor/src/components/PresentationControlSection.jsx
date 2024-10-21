import React from 'react';

function PresentationControlSection ({ onPreviousSlide, onNextSlide, onTryPresentationControl })  {
  return (
    <section className="container mx-auto py-16 px-4 text-center">
      <h2 className="text-3xl font-bold mb-4">Gesture-Controlled Presentation System</h2>
      <p className="text-lg text-gray-600 max-w-xxl mx-auto mb-6">
        Navigate through slides seamlessly using hand gestures. Control your presentations without touching your device.
      </p>
      <div className="flex justify-center space-x-4 mb-4">
        <button
          onClick={onPreviousSlide}
          className="px-8 py-3 bg-blue-600 text-white rounded-lg hover:bg-blue-700"
        >
          Previous Slide
        </button>
        <button
          onClick={onNextSlide}
          className="px-8 py-3 bg-green-500 text-white rounded-lg hover:bg-green-600"
        >
          Next Slide
        </button>
      </div>
      <div className="flex justify-center">
        <button
          onClick={onTryPresentationControl}
          className="mt-4 mb-8 bg-blue-600 text-white px-6 py-3 rounded-full shadow-lg hover:bg-blue-700"
        >
          Try Presentation Control
        </button>
      </div>
      <img className="mx-auto w-96 mb-8" 
           src="https://via.placeholder.com/400" 
           alt="Presentation Control" 
      />
    </section>
  );
};

export default PresentationControlSection;
