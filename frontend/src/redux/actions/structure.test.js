import { structureFail, structureStart, structureSuccess } from './structure';
import { STRUCTURE_FAIL, STRUCTURE_START, STRUCTURE_SUCCESS } from '../constants/types';
import { mockResolveData } from '../../api/calls/getViewsStructure.test';

describe('View structure action testing', () => {
  test('structureStart', () => {
    const expAction = {
      type: STRUCTURE_START,
    };
    expect(structureStart()).toEqual(expAction);
  });

  test('stractureSuccess', () => {
    const viewStructures = mockResolveData.payload.map(structure => ({
      [structure['view_id']]: structure['attributes'],
    }));
    const expAction = {
      type: STRUCTURE_SUCCESS,
      payload: viewStructures,
    };
    expect(structureSuccess(viewStructures)).toEqual(expAction);
    // console.log('structureSuccess ->', structureSuccess(mockResolveData.payload));
  });

  test('structureFail', () => {
    const expAction = {
      type: STRUCTURE_FAIL,
    };
    expect(structureFail()).toEqual(expAction);
  });
});
