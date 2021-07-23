// import i18next from 'i18next';

import { axiosCommonToken } from '../../api/apiClient';
import {
  initialState,
  lngsFail,
  lngsSuccess,
  setTestState,
  startI18n,
  startInitLoading,
  startLngs,
  startTechIn,
  techInFail,
  techInSuccess,
} from './tech';
import store from '../store';
import { TECH_TOKEN } from '../constants/localStorageVariables';

jest.mock('../../api/apiClient');
jest.mock('../../l10n/i18n');

describe('Tech slice testing', () => {
  let state;
  beforeEach(() => {
    jest.resetAllMocks();
    store.dispatch(setTestState(initialState));
    state = store.getState().tech;
    expect(state).toEqual(initialState);
  });
  test('startInitLoading reducer', () => {
    const expState = { ...initialState, loading: true, loaded: false };
    store.dispatch(startInitLoading());
    state = store.getState().tech;
    expect(state).toEqual(expState);
  });

  test('startTechIn reducer', () => {
    const expState = { ...initialState };

    store.dispatch(setTestState({ techLoaded: true }));
    store.dispatch(startTechIn('mockV4'));
    state = store.getState().tech;
    expect(state).toEqual(expState);
  });

  test('techInSuccess reducer', () => {
    const mockPayload = 'mockPayload';
    const expState = { ...initialState, techLoaded: true, techToken: mockPayload };
    store.dispatch(setTestState({ techLoaded: false }));
    store.dispatch(techInSuccess(mockPayload));
    expect(axiosCommonToken).toHaveBeenCalledTimes(1);
    expect(axiosCommonToken).toHaveBeenCalledWith(mockPayload);
    expect(localStorage.setItem).toHaveBeenCalledTimes(1);
    expect(localStorage.setItem).toHaveBeenCalledWith(TECH_TOKEN, mockPayload);
    state = store.getState().tech;
    expect(state).toEqual(expState);
    // console.log('tech slice testing, state ->', state);
    // console.log('tech slice testing, expState ->', expState);
  });

  test('techInFail reducer', () => {
    const mockPayload = 'mockPayload';
    const expState = { ...initialState };
    store.dispatch(
      setTestState({
        techLoaded: true,
        techToken: mockPayload,
        loading: true,
      })
    );
    store.dispatch(techInFail());
    expect(localStorage.removeItem).toHaveBeenCalledTimes(1);
    expect(localStorage.removeItem).toHaveBeenCalledWith(TECH_TOKEN);
    state = store.getState().tech;
    expect(state).toEqual(expState);
    // console.log('tech slice testing, state ->', state);
    // console.log('tech slice testing, expState ->', expState);
  });

  test('startLngs reducer', () => {
    const expState = { ...initialState };
    store.dispatch(
      setTestState({
        lngsLoaded: true,
      })
    );
    store.dispatch(startLngs());
    state = store.getState().tech;
    expect(state).toEqual(expState);
    // console.log('tech slice testing, state ->', state);
    // console.log('tech slice testing, expState ->', expState);
  });

  test('lngsSuccess reducer', () => {
    const expState = { ...initialState,lngsLoaded: true };
    // store.dispatch(
    //   setTestState({
    //     lngsLoaded: true,
    //   })
    // );
    store.dispatch(lngsSuccess());
    state = store.getState().tech;
    expect(state).toEqual(expState);
  });

  test('lngsFail reducer', () => {
    const expState = { ...initialState};
    store.dispatch(
      setTestState({
        lngsLoaded: true,
        loading: true,
      })
    );
    store.dispatch(lngsFail());
    state = store.getState().tech;
    expect(state).toEqual(expState);
  });

  test('startI18n reducer', () => {
    const expState = { ...initialState, loading: true};
    store.dispatch(
      setTestState({
        i18nLoaded: true,
      })
    );
    state = store.getState().tech;
    console.log('tech slice testing, state before ->', state);
    store.dispatch(startI18n());
    state = store.getState().tech;
    // expect(state).toEqual(expState);
    console.log('tech slice testing, state ->', state);
    console.log('tech slice testing, expState ->', expState);
  });
});
