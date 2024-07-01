'use client';
import React from 'react';
import { gql, useQuery } from '@apollo/client';

interface Record {
  id: string;
  name: string;
  age: number;
}

const GET_RECORD = gql`
  query {
    allRecords(id: "123") {
      id
      name
      age
    }
  }
`;

const Page = () => {
  const { loading, error, data } = useQuery(GET_RECORD);

  if (loading) return <p>Loading...</p>;
  if (error) return <p>Error :(</p>;

  return (
    <div>
      {data.allRecords.map((record: Record, index: number) => (
        <div key={record.id}>
          <div>{index}</div>
          <div>{record.id}</div>
          <div>{record.name}</div>
          <div>{record.age}</div>
          <p>
            {record.name}: {record.age}
          </p>
        </div>
      ))}
    </div>
  );
};

export default Page;
