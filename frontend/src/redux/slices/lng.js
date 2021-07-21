import { createSlice } from '@reduxjs/toolkit';

import { LNG_INFO } from '../constants/localStorageVariables';

export const lngInfo = () => {
  /**
   * { lng: 'en' }
   */
  const _LngInfo = localStorage.getItem(LNG_INFO)
    ? { ...JSON.parse(localStorage.getItem(LNG_INFO)) }
    : { lng: 'en' };
  return _LngInfo;
};

export const initialState = {
  ...lngInfo(),
};

const lngSlice = createSlice({
  name: 'lng',
  initialState,
  reducers: {
    lngSwitch: (state, { payload }) => {
      state.lng = payload;
    },
  },
});

export const { lngSwitch } = lngSlice.actions;
export const lngSelector = state => state.lng;
export default lngSlice.reducer;