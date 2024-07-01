import { ApolloClient, InMemoryCache, createHttpLink } from '@apollo/client';
import { setContext } from '@apollo/client/link/context';
import config from '../../config/config';

const createAppoloClient = () => {
  const { backendUrl } = config;
  const httpLink = createHttpLink({
    uri: `${backendUrl}/graphql`,
  });

  const authLink = setContext((_, { headers }) => {
    const token = localStorage.getItem('accessToken');

    return {
      headers: {
        ...headers,
        authorization: token ? `Bearer ${token}` : '',
      },
    };
  });

  return new ApolloClient({
    link: authLink.concat(httpLink),
    cache: new InMemoryCache(),
  });
};

export default createAppoloClient;
