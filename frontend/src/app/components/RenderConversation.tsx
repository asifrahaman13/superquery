import React, { useState } from 'react';
import ButtonStatus from './ui/ButtonStatus';
import Skeleton from './ui/Skeleton';
import { useDispatch, useSelector } from 'react-redux';
import { setQuery, setHistory } from '@/lib/conversation/conversationSlice';
import { RootState } from '@/lib/store';
import {
  Label,
  Listbox,
  ListboxButton,
  ListboxOption,
  ListboxOptions,
} from '@headlessui/react';
import { CheckIcon, ChevronUpDownIcon } from '@heroicons/react/20/solid';

import {
  HistoryItem,
  IconComponentsProps,
  ICONS,
  RenderConversationProps,
} from '@/constants/types/type.dashboard';
import TableView from './TableView';
import SqlRender from './ui/sqlRender';
import DynamicChart from './Charts/DynamicChart';

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
    }
  };

  const plotMapping = [
    { id: 1, name: 'Line plot', type: 'line' },
    { id: 2, name: 'Bar plot', type: 'bar' },
    { id: 3, name: 'Pie plot', type: 'pie' },
  ];

  const [selectedPlots, setSelectedPlots] = useState<{ [key: number]: any }>({});

  const handlePlotChange = (index: number, plot: any) => {
    setSelectedPlots((prev) => ({
      ...prev,
      [index]: plot,
    }));
  };

  return (
    <React.Fragment>
      <div className="w-1/2 flex flex-col gap-4 py-20 justify-between p-8 bg-white rounded-2xl">
        <div className="overflow-y-scroll items-center flex flex-col flex-grow gap-4 text-justify bg-white">
          {conversationSlice.history.length > 0 && (
            <div className="w-full">
              {conversationSlice.history.map((item: HistoryItem, index) => (
                <div key={index} className="flex flex-col gap-6">
                  {item?.messageFrom === 'chatbot' && (
                    <div className="flex flex-col gap-8">
                      <div className="mt-6">
                        {item?.answer_type === 'sql_query' && (
                          <SqlRender sqlQuery={item?.sql_query} />
                        )}
                      </div>

                      {item.answer_type === 'table_response' && (
                        <TableView tableData={JSON.parse(item?.message)} />
                      )}

                      {item?.message !== null &&
                        item?.message !== undefined && (
                          <div>
                            <Listbox
                              value={selectedPlots[index] || plotMapping[0]}
                              onChange={(plot) => handlePlotChange(index, plot)}
                            >
                              <Label className="block text-lg font-semibold leading-6 text-gray-900">
                                Graph (Choose your graph)
                              </Label>
                              <div className="relative mt-2">
                                <ListboxButton className="relative w-full cursor-default rounded-md bg-white py-1.5 pl-3 pr-10 text-left text-gray-900 shadow-sm focus:outline-none sm:text-sm sm:leading-6">
                                  <span className="block truncate">
                                    {selectedPlots[index]?.name || plotMapping[0].name}
                                  </span>
                                  <span className="pointer-events-none absolute inset-y-0 right-0 flex items-center pr-2">
                                    <ChevronUpDownIcon
                                      aria-hidden="true"
                                      className="h-5 w-5 text-gray-400"
                                    />
                                  </span>
                                </ListboxButton>

                                <ListboxOptions
                                  transition
                                  className="absolute z-10 mt-1 max-h-60 w-full overflow-auto rounded-md bg-white py-1 text-base shadow-lg ring-1 ring-black ring-opacity-5 focus:outline-none data-[closed]:data-[leave]:opacity-0 data-[leave]:transition data-[leave]:duration-100 data-[leave]:ease-in sm:text-sm"
                                >
                                  {plotMapping.map((plot) => (
                                    <ListboxOption
                                      key={plot.id}
                                      value={plot}
                                      className="group relative cursor-default select-none py-2 pl-8 pr-4 text-gray-900 data-[focus]:bg-indigo-600 data-[focus]:text-white"
                                    >
                                      <span className="block truncate font-normal group-data-[selected]:font-semibold">
                                        {plot.name}
                                      </span>

                                      <span className="absolute inset-y-0 left-0 flex items-center pl-1.5 text-indigo-600 group-data-[focus]:text-white [.group:not([data-selected])_&]:hidden">
                                        <CheckIcon
                                          aria-hidden="true"
                                          className="h-5 w-5"
                                        />
                                      </span>
                                    </ListboxOption>
                                  ))}
                                </ListboxOptions>
                              </div>
                            </Listbox>

                            <DynamicChart
                              data={item?.message}
                              type={selectedPlots[index]?.type || plotMapping[0].type}
                            />
                          </div>
                        )}
                    </div>
                  )}

                  {item?.messageFrom === 'user' && (
                    <div className="w-3/4 max-w-3/4 ml-auto flex justify-end">
                      <p className="bg-[#f2f2f2] rounded-md p-2">
                        {item.message}
                      </p>
                    </div>
                  )}
                </div>
              ))}
            </div>
          )}

          {status.status && <Skeleton />}
          <div className="w-full flex justify-center flex-col gap-2 h-full items-center">
            {conversationSlice.history.length === 0 && (
              <>
                <IconComponents props={{ slug: db }} />
              </>
            )}
          </div>
        </div>
        <div className="flex gap-2">
          <input
            type="text"
            name="query"
            id="query"
            className="block w-full rounded-md py-1.5 border-gray-200 outline-none focus:border-gray-200 text-gray-900 placeholder:text-gray-400 px-2"
            placeholder="Enter your query"
            value={conversationSlice.query}
            onChange={(e) => dispatch(setQuery({ query: e.target.value }))}
          />

          {!status.status ? (
            <button
              onClick={handleSubmit}
              className="rounded-md text-black px-3.5 py-2.5 text-sm font-semibold shadow-sm hover:bg-gray-100 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600"
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
