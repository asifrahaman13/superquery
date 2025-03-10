'use client';
import React, { useEffect, useRef, useState } from 'react';
import ConnectionSettings from '@/app/components/ConnectionSettings/ConnectionSettings';
import useSettingsToggle from '@/app/hooks/toogle';
import { conversationStaticTexts } from '@/constants/static/staticTexts/staticTexts';
import TableView from '@/app/components/TableView';
import { raw_query_interface } from '@/exports/exports';
import { Status } from '@/constants/types/type.query';
import JSONRenderer from '@/app/components/JsonView';
import RenderConversation from '@/app/components/RenderConversation';
import { useDispatch } from 'react-redux';
import { setHistory } from '@/lib/conversation/conversationSlice';
import { TitleKeys, TITLE } from '@/constants/types/type.dashboard';
import axios from 'axios';

export default function Page({ params }: { params: { slug: TitleKeys } }) {
  const db = params.slug;
  const websocketRef = useRef<WebSocket | null>(null);
  const [status, setStatus] = useState<Status>({
    message: '',
    status: false,
  });
  const { settingsBar, toggleSettingsBar, key } = useSettingsToggle(false);
  const dispatch = useDispatch();
  const [tableData, setTableData] = useState([]);
  const [resultType, setResultType] = useState<string>('');
  const [rawQueryResponse, setRawQueryResponse] = useState<any>();
  const [trainValue, setTrainValue] = useState({
    user_query: '',
    sql_query: '',
    source: 'source1',
  });

  useEffect(() => {
    const backendUrl = process.env.NEXT_PUBLIC_BACKEND_SOCKET || '';
    const accessToken = localStorage.getItem('accessToken');
    const websocket = new WebSocket(
      `${backendUrl}/query/${params.slug}-query/${accessToken}`
    );
    websocketRef.current = websocket;
    websocket.onopen = () => {
      console.log('Connected to websocket');
    };

    websocket.onmessage = (event) => {
      const parsedData = JSON.parse(event.data);
      console.log('The parsed data is :', parsedData);
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
      dispatch(
        setHistory({
          message: parsedData.message,
          sql_query: parsedData.sql_query,
          messageFrom: 'chatbot',
          answer_type: parsedData.answer_type,
        })
      );
      if (parsedData.sql_query !== null && parsedData.sql_query !== undefined) {
        setTrainValue((prev) => ({
          ...prev,
          sql_query: parsedData.sql_query,
        }));
      }
    };

    websocket.onclose = () => {
      console.log('Disconnected from websocket');
    };

    return () => {
      websocket.close();
    };
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, []);

  async function handleRawQuerySubmit() {
    try {
      const accessToken = localStorage.getItem('accessToken') || '';
      const response = await raw_query_interface.rawQuery(
        trainValue.sql_query,
        accessToken,
        db
      );
      if (response?.code === 200) {
        console.log('The response is as follows', response);
        if (response.data.response_type === 'table') {
          setTableData(response.data.response);
          setResultType('table');
        } else if (response.data.response_type === 'json') {
          setRawQueryResponse(response.data);
          setResultType('json');
        }
      }
    } catch (e) {
      throw new Error("Couldn't get raw query");
    }
  }

  function handleChange(e: any) {
    console.log('The value is :', e.target.value);
    setTrainValue({
      ...trainValue,
      [e.target.name]: e.target.value,
    });
  }

  async function SubmitForTrain() {
    try {
      const response = await axios.post(
        `${process.env.NEXT_PUBLIC_BACKEND_URL}/query/data`,
        trainValue
      );
      if (response.status === 200) {
        console.log('The response is :', response.data);
      }
    } catch (err) {
      console.log('The error is :', err);
    }
  }

  return (
    <React.Fragment>
      {settingsBar && <ConnectionSettings dbType={db} key={key} />}
      <div className="w-full h-full flex py-4 flex-col">
        <div className="flex w-full justify-between items-center font-medium  px-4">
          <div className=" font-semibold text-4xl text-Pri-Dark">
            {TITLE[db]}
          </div>
          <div>
            <button
              className=" bg-white p-2 rounded-md px-4 font-medium text-Pri-Dark"
              onClick={toggleSettingsBar}
            >
              Settings
            </button>
          </div>
        </div>
        <div className="w-full flex flex-row h-full p-4 gap-4">
          <RenderConversation
            websocketRef={websocketRef}
            texts={conversationStaticTexts}
            status={status}
            db={db}
          />
          <div className="flex flex-col w-1/2  p-6  bg-white rounded-2xl">
            <div className=" flex flex-col gap-2">
              <div className="text-lg font-semibold text-Pri-Dark">
                Train the system
              </div>
              <div className="text-sm font-medium">
                Enter user query and the corresponding correct SQL query and hit
                enter. This will improve the accuracy of the model by very good
                margin.
              </div>
              <div className="flex  w-full justify-between">
                <div className="text-lg font-semibold text-Pri-Dark">
                  User Query
                </div>
              </div>
              <textarea
                id="comment"
                name="user_query"
                rows={4}
                className="block w-full rounded-md border-s py-1.5 text-gray-900  p-2  border-2  border-Gray-Background outline-none no-scrollbar placeholder:text-gray-400 sm:text-base sm:leading-6"
                defaultValue={''}
                value={trainValue.user_query}
                onChange={(e) => handleChange(e)}
              />
            </div>

            <div className="flex flex-col gap-2">
              <div className="flex  w-full justify-between">
                <div className="text-lg font-semibold text-Pri-Dark">
                  SQL Query
                </div>
              </div>
              <textarea
                id="comment"
                name="sql_query"
                rows={4}
                className="block w-full rounded-md border-s py-1.5 text-gray-900  p-2  border-2  border-Gray-Background outline-none no-scrollbar placeholder:text-gray-400 sm:text-base sm:leading-6"
                defaultValue={''}
                value={trainValue.sql_query}
                onChange={(e) => handleChange(e)}
              />
              <div className="flex justify-end gap-4">
                <button
                  className="rounded-md  text-black px-3.5 py-2.5 text-sm font-semibold  shadow-sm hover:bg-gray-100 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600"
                  onClick={handleRawQuerySubmit}
                >
                  Query
                </button>
                <button
                  className="rounded-md  text-black px-3.5 py-2.5 text-sm font-semibold  shadow-sm hover:bg-gray-100 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600"
                  onClick={SubmitForTrain}
                >
                  Train
                </button>
              </div>
            </div>

            {resultType === 'table' && <TableView tableData={tableData} />}
            {resultType === 'json' && <JSONRenderer data={rawQueryResponse} />}
          </div>
        </div>
      </div>
    </React.Fragment>
  );
}
