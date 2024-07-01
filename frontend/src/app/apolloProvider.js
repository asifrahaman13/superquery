'use client';
import React, { useEffect, useState } from 'react';
import { ApolloProvider } from '@apollo/client';
import createAppoloClient from './appolo-client';

const ApolloClientProvider = ({ children }) => {
  const [client, setClient] = useState(null);

  useEffect(() => {
    const clientInstance = createAppoloClient();
    setClient(clientInstance);
  }, []);

  if (!client) {
    return null;
  }

  return <ApolloProvider client={client}>{children}</ApolloProvider>;
};

export default ApolloClientProvider;
