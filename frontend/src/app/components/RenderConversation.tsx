import React from 'react';
import ButtonStatus from './ui/ButtonStatus';
import BarChart from './Charts/BarChart';
import LineChart from './Charts/LineChart';
import PieChart from './Charts/pieChart';
import ReactMarkdown from 'react-markdown';
import Skeleton from './ui/Skeleton';
import { useDispatch, useSelector } from 'react-redux';
import { setQuery, setHistory } from '@/lib/conversation/conversationSlice';
import { RootState } from '@/lib/store';
import {
  HistoryItem,
  IconComponentsProps,
  ICONS,
  RenderConversationProps,
} from '@/constants/types/type.dashboard';
import TableView from './TableView';
import SqlRender from './ui/sqlRender';

const IconComponents: React.FC<IconComponentsProps> = ({ props }) => {
  const IconComponent = ICONS[props.slug];

  if (!IconComponent) {
    console.error(`Icon component not found for slug: ${props.slug}`);
    return null;
  }

  return (
    <div className="flex items-center">
      <IconComponent className="mr-2" size={200} />
    </div>
  );
};

const RenderConversation = ({
  websocketRef,
  texts,
  status,
  db,
}: RenderConversationProps) => {
  const dispatch = useDispatch();
  const conversationSlice = useSelector(
    (state: RootState) => state.conversation
  );

  const handleSubmit = (e: { preventDefault: () => void }) => {
    e.preventDefault();

    if (websocketRef.current) {
      const queryJson = JSON.stringify({ query: conversationSlice.query });

      websocketRef.current.send(queryJson);
      dispatch(setQuery({ query: '' }));
      dispatch(
        setHistory({
          message: conversationSlice.query,
          messageFrom: 'user',
          sql_query: '',
          answer_type: null,
        })
      );

      console.log(history);
    }
  };
  return (
    <React.Fragment>
      <div className="w-1/2 flex flex-col gap-4  justify-between mb-12  p-6 bg-white rounded-2xl">
        <div className="overflow-y-scroll no-scrollbar h-full flex flex-col gap-2 text-justify bg-white">
          {conversationSlice.history.length > 0 && (
            <>
              {conversationSlice.history.map((item: HistoryItem, index) => (
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
                        <PieChart data={{ message: item.message }} />
                      )}
                      {item.answer_type === 'table_response' && (
                        <TableView tableData={JSON.parse(item?.message)} />
                      )}

                      {item.answer_type === 'sql_query' && (
                        <SqlRender sqlQuery={item?.sql_query} />
                      )}
                    </div>
                  )}

                  {item?.messageFrom === 'user' && (
                    <div className=" w-3/4 max-w-3/4  ml-auto flex justify-end ">
                      <p className="bg-gray-200  rounded-md p-2">
                        {item.message}
                      </p>
                    </div>
                  )}
                </div>
              ))}
            </>
          )}

          {status.status && <Skeleton />}
          <div className=" w-full flex justify-center flex-col gap-2 h-full items-center">
            {conversationSlice.history.length === 0 && (
              <>
                <IconComponents props={{ slug: db }} />
                <div className="flex gap-4  ">
                  {texts.map((text, index) => (
                    <div
                      className="bg-gray-100 w-1/4 p-4 rounded-lg"
                      key={index}
                    >
                      {text}
                    </div>
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
            className="block w-full rounded-md py-1.5 border-gray-200 outline-none focus:border-gray-200 text-gray-900 placeholder:text-gray-400  px-2"
            placeholder="Enter your query"
            value={conversationSlice.query}
            onChange={(e) => dispatch(setQuery({ query: e.target.value }))}
          />

          {!status.status ? (
            <button
              onClick={handleSubmit}
              className="bg-gray-100 rounded-lg  p-3 px-5 font-semibold text-Pri-Dark"
            >
              Submit
            </button>
          ) : (
            <ButtonStatus message={status.message} />
          )}
        </div>
      </div>
    </React.Fragment>
  );
};

export default RenderConversation;
