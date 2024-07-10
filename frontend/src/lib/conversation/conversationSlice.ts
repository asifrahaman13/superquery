import { createSlice, PayloadAction } from '@reduxjs/toolkit';
import { Dispatch, AnyAction } from 'redux';

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
      const { message, messageFrom, answer_type } = action.payload;
      const chatResponse = { message, messageFrom, answer_type };
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
