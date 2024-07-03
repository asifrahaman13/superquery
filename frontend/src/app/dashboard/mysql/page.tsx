'use client';
import React, { useEffect, useRef, useState } from 'react';
import ConnectionSettings from '@/app/components/ConnectionSettings';
import useSettingsToggle from '@/app/hooks/toogle';
import BarChart from '@/app/components/BarChart';
import LineChart from '@/app/components/LineChart';
import { SiMysql } from 'react-icons/si';

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

  return (
    <>
      {settingsBar && <ConnectionSettings dbType="mysql" key={key} />}
      <div className="w-full flex flex-col">
        <div className="flex w-full justify-between items-center py-2 px-4">
          <div className=" font-semibold text-4xl text-Pri-Dark">MySQL</div>
          <div>
            <button
              className=" bg-Pri-Dark p-2 rounded-md px-4 text-white"
              onClick={toggleSettingsBar}
            >
              Settings
            </button>
          </div>
        </div>
        <div className="w-full flex flex-row h-full p-4 gap-4">
          <div className="w-1/2 flex flex-col gap-4  justify-between mb-12  p-6 bg-white rounded-2xl">
            <div className="overflow-y-scroll no-scrollbar h-full flex flex-col gap-2 text-justify bg-white">
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

              <div className=" w-full flex justify-center flex-col gap-2 h-full items-center">
                {history.length === 0 && (
                  <>
                    <SiMysql size={250} />
                    <div>Start conversation with our AI agent.</div>
                    <div className="flex gap-4 ">
                      <button className="bg-gray-100 w-1/4 p-4 rounded-lg">
                        I want line graph of the price of all the products in
                        the sales table. y axis should contain the qrantity, x
                        axis the sales data, labels will the the product names.
                        Fetch all the entries
                      </button>
                      <button className="bg-gray-100 w-1/4 p-4 rounded-lg">
                        I want bar graph on the users table to display the marks
                        of the users. The x axis should be the address Group it
                        by the address.
                      </button>
                      <button className="bg-gray-100 w-1/4 p-4 rounded-lg">
                        Lorem ipsum dolor sit amet consectetur, adipisicing
                        elit. Soluta maiores maxime ipsam fugit, impedit itaque.
                      </button>
                      <button className="bg-gray-100 w-1/4 p-4 rounded-lg">
                        Lorem ipsum, dolor sit amet consectetur adipisicing
                        elit. Eos, quidem?
                      </button>
                    </div>
                  </>
                )}
              </div>
            </div>
            <div className="mt-2 flex gap-2 ">
              <input
                type="text"
                name="query"
                id="query"
                className="block w-full rounded-md py-1.5 border-2 border-gray-200 outline-none focus:border-gray-200 text-gray-900 placeholder:text-gray-400  px-2"
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
          <div className="flex flex-col w-1/2 gap-8 border-2 p-6 mb-12 bg-white rounded-2xl">
            <div className="h-1/2 flex flex-col gap-6">
              {' '}
              <div className="flex  w-full justify-between">
                <div className="text-3xl font-semibold text-Pri-Dark">
                  🎉 Manual Query
                </div>
              </div>
              <p className="text-Pri-Dark text-md font-normal text-justify">
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
            <div className="h-1/2"></div>
          </div>
        </div>
      </div>
    </>
  );
};

export default Page;
