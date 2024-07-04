import React from 'react';

const Skeleton = () => {
  return (
    <React.Fragment>
      <div className="w-full  justify-start flex">
        <div className="border border-gray-300 shadow rounded-md p-4 w-3/4">
          <div className="animate-pulse flex space-x-4">
            <div className="rounded-full bg-gray-400 h-10 w-10"></div>
            <div className="flex-1 space-y-6 py-1">
              <div className="h-2 bg-gray-400 rounded"></div>
              <div className="space-y-3">
                <div className="grid grid-cols-3 gap-4">
                  <div className="h-2 bg-gray-400 rounded col-span-2"></div>
                  <div className="h-2 bg-gray-400 rounded col-span-1"></div>
                </div>
                <div className="h-2 bg-gray-400 rounded"></div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </React.Fragment>
  );
};

export default Skeleton;
