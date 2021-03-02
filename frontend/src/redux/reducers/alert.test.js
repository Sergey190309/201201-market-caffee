import {
  SET_ALERT,
  REMOVE_ALERT,
} from '../actions/types';
import alertReducer from './alert';

describe('alertReducer', () => {
  it('should return initial state haveing invalid action', () => {
    expect(alertReducer(undefined, {})).toEqual([]);
  });

  it('should set alert', () => {
    const action = {
      type: SET_ALERT,
      payload: {
        message: 'Test message',
        alertType: 'Alert type',
        id: 'test id',
      },
    };
    expect(alertReducer(undefined, action)[0]).toEqual(
      action.payload
    );
  });

  it('should it should remove alert', () => {
    const state = [
      {
        message: 'Test message',
        alertType: 'Alert type',
        id: 'test id',
      },
    ];
    const action = {
      type: REMOVE_ALERT,
      payload: {
        message: 'Test message',
        alertType: 'Alert type',
        id: 'test id',
      },
    };
    expect(alertReducer(state, action)).toEqual([]);
  });
});