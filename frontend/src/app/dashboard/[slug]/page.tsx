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

export default function Page({ params }: { params: { slug: TitleKeys } }) {
  const db = params.slug;
  const websocketRef = useRef<WebSocket | null>(null);
  const [status, setStatus] = useState<Status>({
    message: '',
    status: false,
  });
  const { settingsBar, toggleSettingsBar, key } = useSettingsToggle(false);
  const [rawQuery, setRawQuery] = useState<string>('');
  const dispatch = useDispatch();
  const [tableData, setTableData] = useState([]);
  const [resultType, setResultType] = useState<string>('');
  const [rawQueryResponse, setRawQueryResponse] = useState<any>();

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
      console.log('##########################', status);
      dispatch(
        setHistory({
          message: parsedData.message,
          sql_query: parsedData.sql_query,
          messageFrom: 'chatbot',
          answer_type: parsedData.answer_type,
        })
      );
      if (parsedData.sql_query !== null && parsedData.sql_query !== undefined) {
        console.log('ljasdffffffffffffffff :', parsedData.sql_query);
        setRawQuery(parsedData.sql_query);
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
        db
      );
      if (response?.code === 200) {
        console.log('The response', response);
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

  return (
    <React.Fragment>
      {settingsBar && <ConnectionSettings dbType={db} key={key} />}
      <div className="w-full my-16 flex flex-col">
        <div className="flex w-full justify-between items-center py-2 px-4">
          <div className=" font-semibold text-4xl text-Pri-Dark">
            {TITLE[db]}
          </div>
          <div>
            <button
              className=" bg-white p-2 rounded-md px-4 text-Pri-Dark"
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
          <div className="flex flex-col w-1/2  border-2 p-6 mb-12 bg-white rounded-2xl">
            <div className="h-1/2 flex flex-col gap-2">
              <div className="flex  w-full justify-between">
                <div className="text-3xl font-semibold text-Pri-Dark">
                  🎉 Manual Query
                </div>
              </div>
              <textarea
                id="comment"
                name="comment"
                rows={4}
                className="block w-full rounded-md border-s py-1.5 text-gray-900  p-2  border-2  border-Gray-Background outline-none placeholder:text-gray-400 sm:text-base sm:leading-6"
                defaultValue={''}
                value={rawQuery}
                onChange={handleRawQuery}
              />
              <div className="flex justify-end">
                <button
                  className="bg-gray-100 rounded-lg  p-3  px-5 font-semibold text-Pri-Dark"
                  onClick={handleRawQuerySubmit}
                >
                  Submit
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
