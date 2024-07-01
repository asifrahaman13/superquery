'use client';
import React, { useState } from 'react';
import { gql, useLazyQuery } from '@apollo/client';
import ConnectionSettings from '@/app/components/ConnectionSettings';
import useSettingsToggle from '@/app/hooks/toogle';

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
      {settingsBar && <ConnectionSettings dbType="postgres" key={key} />}
      <div className="w-full ">
           <div>
          <div className='text-3xl font-semibold text-orange-400'>Postgres</div>
        </div>
        <div className="w-full text-right">
          <button
            className=" bg-orange-400 p-2 rounded-md px-4 text-white"
            onClick={toggleSettingsBar}
          >
            Settings
          </button>
        </div>
        <div>
          <label
            htmlFor="email"
            className="block text-sm font-medium leading-6 text-gray-900"
          >
            Query
          </label>
          <div className="mt-2">
            <input
              type="text"
              name="query"
              id="query"
              className="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6"
              placeholder="Enter your query"
              value={query}
              onChange={handleChange}
            />
          </div>
          <button onClick={handleSubmit}>Submit</button>
        </div>
        <div>
          {loading && <p>Loading...</p>}
          {error && <p>Error: {error.message}</p>}
          {data && (
            <div>
              <p>Result:</p>
              <p>{data.sqlLLMQuery.query}</p>
            </div>
          )}
        </div>
      </div>
    </>
  );
};

export default Page;
