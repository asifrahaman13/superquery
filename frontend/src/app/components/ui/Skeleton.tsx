import React from 'react';

const Skeleton = () => {
  return (
    <React.Fragment>
      <div className="w-full h-full flex justify-start">
        <div className="border border-gray-300 shadow-lg rounded-lg p-6  w-full ">
          <div className="animate-pulse flex space-x-6">
            <div className="rounded-full bg-gray-400 h-16 w-16"></div>
            <div className="flex-1 space-y-4 py-2">
              <div className="h-4 bg-gray-400 rounded w-3/4"></div>
              <div className="space-y-4">
                <div className="grid grid-cols-3 gap-6">
                  <div className="h-4 bg-gray-400 rounded col-span-2"></div>
                  <div className="h-4 bg-gray-400 rounded col-span-1"></div>
                </div>
                <div className="h-4 bg-gray-400 rounded w-5/6"></div>
              </div>
            </div>
          </div>
          <div className="flex-1 space-y-4 py-2">
            <div className="h-4 bg-gray-400 rounded w-3/4"></div>
            <div className="space-y-4">
              <div className="grid grid-cols-3 gap-6">
                <div className="h-4 bg-gray-400 rounded col-span-2"></div>
                <div className="h-4 bg-gray-400 rounded col-span-1"></div>
              </div>
              <div className="h-4 bg-gray-400 rounded w-5/6"></div>
            </div>
          </div>
          <div className="flex-1 space-y-4 py-2">
            <div className="h-4 bg-gray-400 rounded w-3/4"></div>
            <div className="space-y-4">
              <div className="grid grid-cols-3 gap-6">
                <div className="h-4 bg-gray-400 rounded col-span-2"></div>
                <div className="h-4 bg-gray-400 rounded col-span-2"></div>
                <div className="h-4 bg-gray-400 rounded col-span-1"></div>
                <div className="h-4 bg-gray-400 rounded col-span-2"></div>
              </div>
              <div className="h-4 bg-gray-400 rounded w-5/6"></div>
            </div>
          </div>
        </div>
      </div>
    </React.Fragment>
  );
};

export default Skeleton;
