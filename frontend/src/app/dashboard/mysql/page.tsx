'use client';
import React, { useEffect, useRef, useState } from 'react';
import ConnectionSettings from '@/app/components/ConnectionSettings';
import useSettingsToggle from '@/app/hooks/toogle';
import BarChart from '@/app/components/BarChart';
import LineChart from '@/app/components/LineChart';

interface History {
  message: string;
  messageFrom: string;
  answer_type?: string;
}

const Page = () => {
  const websocketRef = useRef<WebSocket | null>(null);
  const [history, setHistory] = useState<History[]>([]);
  const [query, setQuery] = useState<string>('');
  useEffect(() => {
    const backendUrl = process.env.NEXT_PUBLIC_BACKEND_SOCKET || '';
    const accessToken = localStorage.getItem('accessToken');
    const websocket = new WebSocket(
      `${backendUrl}/query/mysql-query/${accessToken}`
    );
    websocketRef.current = websocket;
    websocket.onopen = () => {
      console.log('Connected to websocket');
    };

    websocket.onmessage = (event) => {
      console.log(event.data);
      const parsedData = JSON.parse(event.data);
      console.log(parsedData);
      const chatResponse = { ...parsedData, messageFrom: 'chatbot' };
      setHistory((prev) => [...prev, chatResponse]);
    };

    websocket.onclose = () => {
      console.log('Disconnected from websocket');
    };

    return () => {
      websocket.close();
    };
  }, []);

  const handleChange = (e: {
    target: {
      value: React.SetStateAction<string>;
    };
  }) => {
    setQuery(e.target.value);
  };

  const handleSubmit = (e: { preventDefault: () => void }) => {
    e.preventDefault();
    if (websocketRef.current) {
      const queryJson = JSON.stringify({ query });

      websocketRef.current.send(queryJson);
      setQuery('');
      const userResonse = { message: query, messageFrom: 'user' };
      setHistory((prev) => [...prev, userResonse]);
      console.log(history);
    }
  };

  const { settingsBar, toggleSettingsBar, key } = useSettingsToggle(false);
  const jsonData = {
    message:
      '[\n    {\n        "Product A": [\n            {"x": "2024-06-01", "y": 150.0},\n            {"x": "2024-06-04", "y": 45.0},\n            {"x": "2024-06-07", "y": 60.0},\n            {"x": "2024-06-10", "y": 15.0},\n            {"x": "2024-06-11", "y": 75.0},\n            {"x": "2024-06-14", "y": 30.0},\n            {"x": "2024-06-17", "y": 45.0},\n            {"x": "2024-06-20", "y": 15.0},\n            {"x": "2024-06-23", "y": 60.0},\n            {"x": "2024-06-26", "y": 30.0},\n            {"x": "2024-06-29", "y": 45.0},\n            {"x": "2024-07-02", "y": 30.0},\n            {"x": "2024-07-05", "y": 45.0},\n            {"x": "2024-07-08", "y": 60.0},\n            {"x": "2024-07-11", "y": 30.0},\n            {"x": "2024-07-14", "y": 75.0},\n            {"x": "2024-07-17", "y": 105.0},\n            {"x": "2024-07-20", "y": 60.0},\n            {"x": "2024-07-23", "y": 45.0},\n            {"x": "2024-07-26", "y": 30.0},\n            {"x": "2024-07-29", "y": 75.0}\n        ]\n    },\n    {\n        "Product B": [\n            {"x": "2024-06-02", "y": 100.0},\n            {"x": "2024-06-05", "y": 160.0},\n            {"x": "2024-06-08", "y": 40.0},\n            {"x": "2024-06-12", "y": 60.0},\n            {"x": "2024-06-15", "y": 80.0},\n            {"x": "2024-06-18", "y": 100.0},\n            {"x": "2024-06-21", "y": 40.0},\n            {"x": "2024-06-24", "y": 120.0},\n            {"x": "2024-06-27", "y": 100.0},\n            {"x": "2024-06-30", "y": 140.0},\n            {"x": "2024-07-03", "y": 100.0},\n            {"x": "2024-07-06", "y": 120.0},\n            {"x": "2024-07-09", "y": 100.0},\n            {"x": "2024-07-12", "y": 60.0},\n            {"x": "2024-07-15", "y": 80.0},\n            {"x": "2024-07-18", "y": 60.0},\n            {"x": "2024-07-21", "y": 120.0},\n            {"x": "2024-07-24", "y": 100.0},\n            {"x": "2024-07-27", "y": 80.0},\n            {"x": "2024-07-30", "y": 60.0}\n        ]\n    },\n    {\n        "Product C": [\n            {"x": "2024-06-03", "y": 175.0},\n            {"x": "2024-06-06", "y": 150.0},\n            {"x": "2024-06-09", "y": 225.0},\n            {"x": "2024-06-13", "y": 175.0},\n            {"x": "2024-06-16", "y": 150.0},\n            {"x": "2024-06-19", "y": 200.0},\n            {"x": "2024-06-22", "y": 175.0},\n            {"x": "2024-06-25", "y": 75.0},\n            {"x": "2024-06-28", "y": 100.0},\n            {"x": "2024-07-01", "y": 150.0},\n            {"x": "2024-07-04", "y": 100.0},\n            {"x": "2024-07-07", "y": 50.0},\n            {"x": "2024-07-10", "y": 175.0},\n            {"x": "2024-07-13", "y": 150.0},\n            {"x": "2024-07-16", "y": 50.0},\n            {"x": "2024-07-19", "y": 125.0},\n            {"x": "2024-07-22", "y": 50.0},\n            {"x": "2024-07-25", "y": 175.0},\n            {"x": "2024-07-28", "y": 150.0},\n            {"x": "2024-07-31", "y": 50.0}\n        ]\n    }\n]',
  };
  return (
    <>
      {settingsBar && <ConnectionSettings dbType="mysql" key={key} />}
      <div className="w-full flex flex-col ">
        <div className="w-full flex flex-row h-full">
          <div className="w-1/2 flex flex-col gap-4 h-full justify-between  p-6">
            <label
              htmlFor="email"
              className="block font-semibold leading-6 text-3xl text-Pri-Dark"
            >
              MySQL Query
            </label>

            <div className="overflow-y-scroll no-scrollbar h-full flex flex-col gap-2 text-justify">
              {history.length > 0 && (
                <>
                  {history.map((item, index) => (
                    <>
                      {item?.messageFrom === 'chatbot' && (
                        <>
                          {item.answer_type === 'bar_chart' && (
                            <BarChart data={{ message: item.message }} />
                          )}
                          {item.answer_type == 'line_chart' && (
                            <LineChart data={{ message: item.message }} />
                          )}
                          {item.answer_type === 'plain_answer' && (
                            <>
                              <div className="bg-indigo-400 w-3/4 max-w-3/4 rounded-md p-2 text-white">
                                {item?.message}
                              </div>
                            </>
                          )}
                        </>
                      )}

                      {item?.messageFrom === 'user' && (
                        <>
                          {' '}
                          <div className=" w-3/4 max-w-3/4  ml-auto flex justify-end ">
                            <p className="bg-gray-200 p-2  rounded-md">
                              {' '}
                              {item.message}
                            </p>
                          </div>
                        </>
                      )}
                    </>
                  ))}
                </>
              )}
            </div>
            <div className="mt-2 flex gap-2 ">
              <input
                type="text"
                name="query"
                id="query"
                className="block w-full rounded-md py-1.5 border-2 border-gray-200 outline-none focus:border-gray-200 text-gray-900 placeholder:text-gray-400 sm:text-sm sm:leading-6 placeholder:px-2 p-2"
                placeholder="Enter your query"
                value={query}
                onChange={handleChange}
              />
              <button
                onClick={handleSubmit}
                className="bg-Pri-Dark rounded-lg  p-3 px-5 text-white"
              >
                Submit
              </button>
            </div>
          </div>
          <div className="flex flex-col w-1/2 gap-8 border-2 p-6">
            <div className="h-1/2 flex flex-col gap-6">
              {' '}
              <div className="flex  w-full justify-between">
                <div className="text-3xl font-semibold text-Pri-Dark">
                  🎉 Manual Query
                </div>{' '}
                <div>
                  <button
                    className=" bg-Pri-Dark p-2 rounded-md px-4 text-white"
                    onClick={toggleSettingsBar}
                  >
                    Settings
                  </button>
                </div>
              </div>
              <p className="text-Pri-Dark text-lg font-medium text-justify">
                MySQL is a widely-used open-source relational database
                management system known for its scalability, performance, and
                robust feature set. It organizes data into tables linked by
                relationships, supporting multi-platform deployment and offering
                high availability through features like replication and
                clustering. MySQL excels in handling both small-scale
                applications and large-scale systems with efficient data
                management and query execution. Security features include access
                control and encryption, while its active community ensures
                continuous development and support. Commonly used in web
                applications, data warehousing, and online transaction
                processing (OLTP), MySQL remains a cornerstone for developers
                and businesses seeking a reliable, flexible database solution.{' '}
              </p>
              <textarea
                name="query"
                className="w-full h-20 border-2"
                id=""
              ></textarea>
              <div className="flex justify-end">
                <button className="bg-Pri-Dark rounded-lg w-1/5 text-righ p-3 px-5 text-white">
                  Submit
                </button>
              </div>
            </div>
            <div className="text-2xl font-semibold text-Pri-Dark">
              {' '}
              🚀My Result
            </div>
            <div className="h-1/2 border-2"></div>
          </div>
        </div>
      </div>
    </>
  );
};

export default Page;
