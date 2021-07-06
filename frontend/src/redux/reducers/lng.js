import { LNG_SWITCH } from '../constants/types';

const initialStore = 'en';
// const initialStore = 'ru';

const lngSwitch = (store = initialStore, action) => {
  const { type, payload } = action;

  switch (type) {
    case LNG_SWITCH:
      return payload;
    default:
      // console.log('lngSwithc reducer, store ->', store)
      return store;
  }
};

export default lngSwitch;
