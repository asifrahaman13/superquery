import { combineReducers, configureStore } from '@reduxjs/toolkit';
import conversationSlice from './conversation/conversationSlice';

const store = configureStore({
  reducer: {
    // add reducers here
    conversation: conversationSlice,
  },
});

const rootReducer = combineReducers({
  // add reducers here
  conversation: conversationSlice,
});

export default store;

export type RootState = ReturnType<typeof rootReducer>;
