import { v4 } from 'uuid';
import mockAxios from '../../api/apiClient';
import {
  START_LNGS,
  START_TECH_IN,
  TECH_IN_FAIL,
  TECH_IN_SUCCESS,
} from '../actions/types';
import { recordSaga } from '../../testUtils';
import { startInitWorker, techInFetch } from './tech';
// import { axiosCommonToken } from '../../api/apiClient';

// jest.mock('../../api/apiClient', () => ({ axiosCommonToken: jest.fn() }));

describe('Tech saga testing', () => {
  const mockTechInData = v4();
  const mockResolveData = {
    message: 'ТехРег докладывает! Тех жетон в сообщении.',
    payload:
      'mock_token',
  };
  const mockRejectData = {
    response: {
      data: {
        message: 'Error message',
      },
      status: 400,
      headers: { header: 'Some header' },
    },
    config: { config: 'Some config' },
  };

  beforeAll(() => {
    jest.resetAllMocks();
  });

  // test.skip('start init saga', async () => {
  //   const dispatched = await recordSaga(startInitWorker);
  //   expect(dispatched.length).toBe(1);
  //   const { type, payload } = dispatched[0];
  //   expect(type).toBe(START_TECH_IN);
  //   expect(payload).toBeString();
  //   console.log('start init saga, dispatched ->', dispatched)
  // });


  test('tech in success', async () => {
    mockAxios.post.mockImplementation(() => Promise.resolve({ data: mockResolveData }));
    const setToken = jest.fn()
    const initialAction = {
      // type: LOG_IN_START,
      payload: mockTechInData,

    };
    const expDispatch00 = {
      type: TECH_IN_SUCCESS,
      payload: mockResolveData.payload,
    };
    const expDispatch01 = {
      type: START_LNGS,
    };
    const dispatched = await recordSaga(techInFetch, initialAction, setToken);
    expect(mockAxios.post).toHaveBeenCalledTimes(1);
    expect(mockAxios.post.mock.calls[0][0]).toBe('/home/tech/auth');
    expect(mockAxios.post.mock.calls[0][1]).toEqual({ tech_id: mockTechInData });
    // expect(setToken).toHaveBeenCalledTimes(1);

    // expect(axiosCommonToken).toHaveBeenCalledTimes(1);
    expect(dispatched.length).toBe(2);
    expect(dispatched[0]).toEqual(expDispatch00);
    expect(dispatched[1]).toEqual(expDispatch01);

    // console.log('tech in success tesing, daispatched ->', dispatched)
  });

  test('tech in fail', async () => {
    mockAxios.post.mockImplementation(() => Promise.reject({ data: mockRejectData }));
    const initialAction = {
      // type: LOG_IN_START,
      payload: mockTechInData,
    };
    // const expDispatch = {
    //   type: TECH_IN_SUCCESS,
    //   payload: mockResolveData.payload
    // }
    const dispatched = await recordSaga(techInFetch, initialAction);
    expect(mockAxios.post).toHaveBeenCalledTimes(1);
    expect(mockAxios.post.mock.calls[0][0]).toBe('/home/tech/auth');
    expect(mockAxios.post.mock.calls[0][1]).toEqual({ tech_id: mockTechInData });
    expect(dispatched.length).toBe(1);
    const { type, payload } = dispatched[0];
    expect(type).toBe(TECH_IN_FAIL);
    expect(payload).toBeObject();
    expect(payload).toContainKeys(['data']);

    // expect(dispatched[0]).toEqual(expDispatch);

    // console.log('tech in success tesing, dispatched ->', dispatched[0].payload)
  });
});
