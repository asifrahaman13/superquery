import { createSlice, PayloadAction } from '@reduxjs/toolkit';

// Define the state and action types
interface ConversationState {
  query: string;
  history: Array<{ message: string; messageFrom: string }>;
}

interface SetQueryActionPayload {
  query: string;
}

interface SetHistoryActionPayload {
  message: string;
  sql_query: string | '';
  messageFrom: string;
  answer_type: string | null;
}

// Create the conversation slice with typed state and actions
export const conversationSlice = createSlice({
  name: 'conversation',
  initialState: {
    query: '',
    history: [],
  } as ConversationState,
  reducers: {
    setQuery: (state, action: PayloadAction<SetQueryActionPayload>) => {
      const { query } = action.payload;
      state.query = query;
    },
    setHistory: (state, action: PayloadAction<SetHistoryActionPayload>) => {
      const { message, messageFrom, answer_type, sql_query } = action.payload;
      const chatResponse = { message, messageFrom, answer_type, sql_query };
      state.history = [...state.history, chatResponse];
      console.log(
        'The entire history',
        JSON.parse(JSON.stringify(state.history))
      );
    },
    clearHistory: (state) => {
      state.history = [];
    },
  },
});

// Export the actions and reducer
export const { setQuery, setHistory, clearHistory } = conversationSlice.actions;
export default conversationSlice.reducer;
