import { delayAlertHiding } from './alert';


describe('Normal func testing', () => {
  test('delayAlertHiding func testing', async () => {
    await expect(delayAlertHiding(5)).toResolve();
    await expect(delayAlertHiding(5)).not.toReject();
  });
})

// jest.mock('./alert', () => ({ delayAlertHiding: jest.fn() }));

// describe('Whole Saga testing', () => {

//   beforeAll(() => {
//     jest.resetAllMocks();
//   });

//   test('it should wait every start alert', () => {
//     delayAlertHiding.mockImplementation(() => Promise.resolve());
//     const dispatched = recordSaga()
//     // console.log(genObject.next().value)
//     // expect(genObject.next().value).toEqual(takeEvery(START_ALERT, ));
//   });
// });
