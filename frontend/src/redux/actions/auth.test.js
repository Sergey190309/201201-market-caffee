import mockAxios from '../../api/apiClient';
// import mockAxios from 'axios';

import configureMockStore from 'redux-mock-store';
import thunk from 'redux-thunk';
// import MockAdapter from 'axios-mock-adapter'

import {
  LOG_IN_MODAL_CLOSED,
  LOG_IN_SUCCESS,
  LOG_OUT,
  SIGN_UP_MODAL_CLOSED,
  SET_ALERT,
  LOG_IN_FAIL,
} from './types';

import { logInAction, logOutAction, setLoggedInFalse, setSignedUpFalse } from './auth';

// const mock = new MockAdapter(mockAxios)

jest.mock('../reducers');

describe('Auth action testing', () => {
  describe('normal action creators', () => {
    test('logOutAction', () => {
      const expAction = {
        type: LOG_OUT,
      };
      expect(logOutAction()).toEqual(expAction);
    });

    test('setSignedUpFalse', () => {
      const expAction = {
        type: SIGN_UP_MODAL_CLOSED,
      };
      expect(setSignedUpFalse()).toEqual(expAction);
    });

    test('setLoggedInFalse', () => {
      const expAction = {
        type: LOG_IN_MODAL_CLOSED,
      };
      expect(setLoggedInFalse()).toEqual(expAction);
    });
  });

  describe('async action creators', () => {
    describe('logInAction', () => {
      const middleWares = [thunk];
      const mockStore = configureMockStore(middleWares);
      const mockEmail = 'test@email.com';
      const mockPassword = 'password';

      afterEach(() => {});

      test('success', async () => {
        const mockState = {};
        const store = mockStore(mockState);
        const mockData = {
          message: 'message',
          payload: {
            user_name: 'user_name',
            email: mockEmail,
            isAdmin: true,
            access_token: 'access_token',
            refresh_token: 'refresh_token',
          },
        };
        const expActions = [
          {
            type: SET_ALERT,
            payload: {
              message: 'message',
              alertType: 'info',
            },
          },
          {
            type: LOG_IN_SUCCESS,
            payload: {
              userName: 'user_name',
              email: mockEmail,
              isAdmin: true,
              access_token: 'access_token',
              refresh_token: 'refresh_token',
            },
          },
        ];

        // mockAxios.post.mockImplementationOnce(() => Promise.resolve({ data: mockData }));
        mockAxios.post.mockResolvedValueOnce({ data: mockData });
        await store.dispatch(logInAction(mockEmail, mockPassword));
        expect(mockAxios.post).toHaveBeenCalledTimes(1);
        expect(store.getActions()[0].type).toEqual(expActions[0].type);
        expect(store.getActions()[0].payload.message).toBe(expActions[0].payload.message);
        expect(store.getActions()[0].payload.alertType).toBe(
          expActions[0].payload.alertType
        );
        expect(store.getActions()[1]).toEqual(expActions[1]);
      });

      test('fail, wrong password', async () => {
        const mockState = {};
        const store = mockStore(mockState);
        const mockData = {
          data: {
            message: 'wrong password',
          },
        };
        const expActions = [
          {
            type: SET_ALERT,
            payload: {
              message: 'wrong password',
              alertType: 'error',
            },
          },
          {
            type: LOG_IN_FAIL,
          },
        ];
        // console.log('test:', mockData.response.data.message)
        mockAxios.post.mockRejectedValueOnce({ response: mockData });

        await store.dispatch(logInAction(mockEmail, mockPassword));
        expect(store.getActions()[0].type).toEqual(expActions[0].type);
        expect(store.getActions()[0].payload.message).toBe(expActions[0].payload.message);
        expect(store.getActions()[0].payload.alertType).toBe(
          expActions[0].payload.alertType
        );
        expect(store.getActions()[1]).toEqual(expActions[1]);
      });

      test('fail, network error', async () => {
        const mockState = {};
        const store = mockStore(mockState);
        const mockData = {
          request: { readyState: 4 },
          message: 'network error',
        };
        const expActions = [
          {
            type: SET_ALERT,
            payload: {
              message: 'network error',
              alertType: 'error',
            },
          },
          {
            type: LOG_IN_FAIL,
          },
        ];
        // console.log('test:', mockData.response.data.message)
        mockAxios.post.mockRejectedValueOnce({ ...mockData });

        await store.dispatch(logInAction(mockEmail, mockPassword));
        // console.log(store.getActions()[0]);
        expect(store.getActions()[0].type).toEqual(expActions[0].type);
        expect(store.getActions()[0].payload.message).toBe(expActions[0].payload.message)
        expect(store.getActions()[0].payload.alertType).toBe(expActions[0].payload.alertType)
        expect(store.getActions()[1]).toEqual(expActions[1]);
      });
    });
  });
});
