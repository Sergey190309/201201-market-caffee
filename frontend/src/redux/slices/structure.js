import { createSlice } from '@reduxjs/toolkit';

export const initialState = {
  loading: false,
  loaded: false,
};

const structureSlice = createSlice({
  name: 'structure',
  initialState,
  reducers: {
    setState: (state, { payload }) => {
      // tested
      /**
       * for testing
       */
      Object.assign(state, payload);
    },
    structureStart: state => {
      state.loading = true;
      state.loaded = false;
    },
    structureSuccess: (state, { payload }) => {
      let structures = {};
      // console.log('structureSlice, structureSuccess, payload ->', payload)
      payload.forEach(structure => {
        structures = { ...structures, ...structure };
      });
      Object.assign(state, structures, { loaded: true, loading: false });
    },
    structureFail: state => {
      Object.keys(state).forEach(key => {
        if (!['loading', 'loaded'].includes(key)) {
          delete state[key];
        }
      });
      Object.assign(state, initialState);
    },
  },
});

export const { setState, structureStart, structureSuccess, structureFail } =
  structureSlice.actions;
export const structureSelector = state => state.structure;
export default structureSlice.reducer;
