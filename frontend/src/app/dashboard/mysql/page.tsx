'use client';
import React, { useState } from 'react';
import { gql, useLazyQuery } from '@apollo/client';
import ConnectionSettings from '@/app/components/ConnectionSettings';
import useSettingsToggle from '@/app/hooks/toogle';
import {
  SiMysql,
} from 'react-icons/si';

const GET_RESULT = gql`
  query SqlLLMQuery($query: String!) {
    sqlLLMQuery(query: $query) {
      query
    }
  }
`;

const Page = () => {
  const [query, setQuery] = useState<string>('');

  const [executeQuery, { loading, error, data }] = useLazyQuery(GET_RESULT);

  const handleChange = (e: {
    target: { value: React.SetStateAction<string> };
  }) => {
    setQuery(e.target.value);
  };

  const handleSubmit = (e: { preventDefault: () => void }) => {
    e.preventDefault();
    executeQuery({ variables: { query } });
  };

  const { settingsBar, toggleSettingsBar, key } = useSettingsToggle(false);
  return (
    <>
      {settingsBar && <ConnectionSettings dbType="mysql" key={key} />}
      <div className="w-full flex flex-col gap-12">
        <div className="w-full flex flex-row h-full">
          <div className="w-1/2 flex flex-col gap-4 h-full overflow-y-scroll no-scrollbar">
            <label
              htmlFor="email"
              className="block font-semibold leading-6 text-3xl text-orange-400"
            >
              MySQL Query
            </label>
            <div className="flex flex-grow">
              {loading && <p>Loading...</p>}
              {error && <p>Error: {error.message}</p>}
              {data && (
                <div>
                  <p>Result:</p>
                  <p>{data.sqlLLMQuery.query}</p>
                </div>
              )}
            </div>
            <div className='flex justify-center flex-grow'>
              <SiMysql size={300}/>
            </div>
            <div className="mt-2 ">
              <input
                type="text"
                name="query"
                id="query"
                className="block w-full rounded-md py-1.5 border-2 border-gray-200 outline-none focus:border-gray-200 text-gray-900 placeholder:text-gray-400 sm:text-sm sm:leading-6 placeholder:px-2 p-2"
                placeholder="Enter your query"
                value={query}
                onChange={handleChange}
              />
            </div>
            <div className="w-full">
              {' '}
              <button
                onClick={handleSubmit}
                className="bg-orange-400 rounded-lg p-3 w-full text-white"
              >
                Submit
              </button>
            </div>
          </div>
          <div className="flex flex-col w-1/2 gap-8">
            <div className="flex  w-full justify-between">
              <div className="text-3xl font-semibold text-orange-400">
                MySQL
              </div>{' '}
              <div>
                <button
                  className=" bg-orange-400 p-2 rounded-md px-4 text-white"
                  onClick={toggleSettingsBar}
                >
                  Settings
                </button>
              </div>
            </div>
            <p>
              MySQL is a widely-used open-source relational database management
              system known for its scalability, performance, and robust feature
              set. It organizes data into tables linked by relationships,
              supporting multi-platform deployment and offering high
              availability through features like replication and clustering.
              MySQL excels in handling both small-scale applications and
              large-scale systems with efficient data management and query
              execution. Security features include access control and
              encryption, while its active community ensures continuous
              development and support. Commonly used in web applications, data
              warehousing, and online transaction processing (OLTP), MySQL
              remains a cornerstone for developers and businesses seeking a
              reliable, flexible database solution.{' '}
            </p>
          </div>
        </div>
      </div>
    </>
  );
};

export default Page;
