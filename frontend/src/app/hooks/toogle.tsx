'use client';
import { useState } from 'react';

const useSettingsToggle = (initialState = false) => {
  const [settingsBar, setSettingsBar] = useState(initialState);
  const [key, setKey] = useState(0);

  const toggleSettingsBar = () => {
    setSettingsBar(true);
    setKey(key + 1);
  };

  return {
    settingsBar,
    toggleSettingsBar,
    key,
  };
};

export default useSettingsToggle;
