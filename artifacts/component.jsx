import React from 'react';

const Chatbot = () => {
  return (
    <div className="flex flex-col items-center justify-center min-h-screen bg-gray-100">
      <h1 className="text-3xl font-bold text-gray-800 mb-2">
        CUDA Documentation Chatbot
      </h1>
      <p className="text-gray-600 mb-6">Ask questions about CUDA</p>
      <div className="bg-white shadow-md rounded-lg p-4 w-full max-w-xl">
        <div className="bg-gray-200 rounded-md p-3 mb-4">
          <p className="text-gray-800">
            Hello! I am your CUDA documentation assistant. Ask me anything about CUDA programming.
          </p>
        </div>
        <div className="flex items-center">
          <input
            type="text"
            className="flex-1 p-3 bg-gray-100 rounded-full border border-gray-300 focus:outline-none focus:ring focus:ring-blue-200"
            placeholder="Type your CUDA question..."
          />
          <button className="ml-2 px-4 py-2 bg-blue-500 text-white rounded-full hover:bg-blue-600 focus:outline-none">
            Send
          </button>
        </div>
      </div>
    </div>
  );
};

export default Chatbot;