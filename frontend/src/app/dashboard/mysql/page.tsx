'use client';
import React, { useEffect, useRef, useState } from 'react';
import ConnectionSettings from '@/app/components/ConnectionSettings';
import useSettingsToggle from '@/app/hooks/toogle';
import BarChart from '@/app/components/Charts/BarChart';
import LineChart from '@/app/components/Charts/LineChart';
import { SiMysql } from 'react-icons/si';
import { History, Status } from '@/constants/types/type.query';
import { raw_query_interface } from '@/exports/exports';
import { mysqlTexts } from '@/constants/static/myssql/mysqlTexts';
import Skeleton from '@/app/components/ui/Skeleton';
import ButtonStatus from '@/app/components/ui/ButtonStatus';
import TableView from '@/app/components/TableView';
import PieChart from '@/app/components/Charts/pieChart';

const Page = () => {
  const websocketRef = useRef<WebSocket | null>(null);
  const [history, setHistory] = useState<History[]>([]);
  const [query, setQuery] = useState<string>('');
  const [status, setStatus] = useState<Status>({
    message: '',
    status: false,
  });
  const { settingsBar, toggleSettingsBar, key } = useSettingsToggle(false);
  const [tableData, setTableData] = useState([]);

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
      const parsedData = JSON.parse(event.data);
      console.log(parsedData);
      if (parsedData.status === true) {
        setStatus({
          message: parsedData.message,
          status: true,
        });
        return;
      } else {
        setStatus({
          message: 'Error in the query',
          status: false,
        });
      }
      console.log('##########################', status);
      const chatResponse = { ...parsedData, messageFrom: 'chatbot' };
      setHistory((prev) => [...prev, chatResponse]);
    };

    websocket.onclose = () => {
      console.log('Disconnected from websocket');
    };

    return () => {
      websocket.close();
    };
    // eslint-disable-next-line react-hooks/exhaustive-deps
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

  const [rawQuery, setRawQuery] = useState<string>('');

  const handleRawQuery = (e: {
    target: {
      value: React.SetStateAction<string>;
    };
  }) => {
    setRawQuery(e.target.value);
  };

  async function handleRawQuerySubmit() {
    try {
      const accessToken = localStorage.getItem('accessToken') || '';
      const response = await raw_query_interface.rawQuery(
        rawQuery,
        accessToken,
        'mysql'
      );
      if (response?.code === 200) {
        console.log(response);
        setTableData(response.data);
      }
    } catch (e) {
      throw new Error("Couldn't get raw query");
    }
  }

  return (
    <React.Fragment>
      {settingsBar && <ConnectionSettings dbType="mysql" key={key} />}
      <div className="w-full my-6 flex flex-col">
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
                    <div key={index}>
                      {item?.messageFrom === 'chatbot' && (
                        <div>
                          {item.answer_type === 'bar_chart' && (
                            <BarChart data={{ message: item.message }} />
                          )}
                          {item.answer_type == 'line_chart' && (
                            <LineChart data={{ message: item.message }} />
                          )}
                          {item.answer_type === 'pie_chart' && (
                            <>
                              <PieChart data={{ message: item.message }} />
                            </>
                          )}
                          {item.answer_type === 'plain_answer' && (
                            <div className="max-w-3/4  ml-auto flex justify-start ">
                              <p className="bg-indigo-500 max-w-3/4 text-white p-2  rounded-md">
                                {item.message}
                              </p>
                            </div>
                          )}
                        </div>
                      )}

                      {item?.messageFrom === 'user' && (
                        <>
                          <div className=" w-3/4 max-w-3/4  ml-auto flex justify-end ">
                            <p className="bg-gray-200 p-2  rounded-md">
                              {item.message}
                            </p>
                          </div>
                        </>
                      )}
                    </div>
                  ))}
                </>
              )}

              {status.status && <Skeleton />}
              <div className=" w-full flex justify-center flex-col gap-2 h-full items-center">
                {history.length === 0 && (
                  <>
                    <SiMysql size={250} />
                    <div>Start conversation with our AI agent.</div>
                    <div className="flex gap-4  ">
                      {mysqlTexts.map((text, index) => (
                        <>
                          <div
                            className="bg-gray-100 w-1/4 p-4 rounded-lg"
                            key={index}
                          >
                            {text}
                          </div>
                        </>
                      ))}
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

              {!status.status ? (
                <>
                  <button
                    onClick={handleSubmit}
                    className="bg-Pri-Dark rounded-lg  p-3 px-5 font-semibold text-white"
                  >
                    Submit
                  </button>
                </>
              ) : (
                <ButtonStatus message={status.message} />
              )}
            </div>
          </div>
          <div className="flex flex-col w-1/2  border-2 p-6 mb-12 bg-white rounded-2xl">
            <div className="h-1/2 flex flex-col gap-6">
              <div className="flex  w-full justify-between">
                <div className="text-3xl font-semibold text-Pri-Dark">
                  🎉 Manual Query
                </div>
              </div>
              <textarea
                name="query"
                rows={5}
                className="w-full h-50 border-2 p-2 rounded-lg outline-none focus:border-2 focus:border-indigo-400 "
                id=""
                placeholder="Enter your SQL query"
                value={rawQuery}
                onChange={handleRawQuery}
              ></textarea>
              <div className="flex justify-end">
                <button
                  className="bg-Pri-Dark rounded-lg text-righ p-3 px-5 font-semibold text-white"
                  onClick={handleRawQuerySubmit}
                >
                  Submit
                </button>
              </div>
            </div>
            <TableView tableData={tableData} />
          </div>
        </div>
      </div>
    </React.Fragment>
  );
};

export default Page;
