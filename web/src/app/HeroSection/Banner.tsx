/* eslint-disable @next/next/no-img-element */
import React from 'react';

const Banner = () => {
  return (
    <React.Fragment>
      <div className="w-full  flex flex-row items-center justify-center py-16 text-Pri-Dark">
        <div className="w-1/2 flex flex-col items-center justify-center gap-6">
          <h1 className="text-4xl font-bold">Enhance Your Data Analysis</h1>
          <p className="text-md font-medium text-center text-black">
            LLM powered data analytics platform. Have conversation with our
            agent in natural language to get detailed insights on your data.
            Take decision much faster. Debug customer issues much faster.
          </p>
        </div>
      </div>
    </React.Fragment>
  );
};

export default Banner;
