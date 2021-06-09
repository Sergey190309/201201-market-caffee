import { idsByIdNum, recordIdList } from './utils';

describe('Utils testing', () => {
  describe('idsByIdNum testing', () => {

    test('idsByIdNum testing', () => {
      const id = 'testingId';
      const qnt = 3
      const expResult = [
        id+'_00',
        id+'_01',
        id+'_02',
      ]
      expect(idsByIdNum(id, qnt)).toEqual(expResult);
    });

    test('negative qnt should retun empty array', () => {
      const id = 'testingId';
      const qnt = -3
      const expResult = []
      expect(idsByIdNum(id, qnt)).toEqual(expResult);
    });

    test('qnt above 100 shoult retun array length 100', () => {
      const id = 'testingId';
      const qnt = 150
      expect(idsByIdNum(id, qnt).length).toEqual(100);
    });
  });

  describe('recordIdList testing', () => {
    test('normal, small qnt', () => {
      const arg = '01_vblock_txt_3'
      const expResult = [
        '01_vblock_txt_000',
        '01_vblock_txt_001',
        '01_vblock_txt_002',
      ]
      expect(recordIdList(arg)).toEqual(expResult);
      expect(recordIdList(arg).length).toBe(3);
    });

    test('number can not be converted to int', () => {
      const arg = '01_vblock_txt_z'
      // const expResult = [
      //   '01_vblock_txt_000',
      //   '01_vblock_txt_001',
      //   '01_vblock_txt_002',
      // ]
      expect(recordIdList(arg)).toBe(0);
      console.log('recordIdList testing, recordIdList(arg) ->', recordIdList(arg))
    });

    test('number has been above 1000', () => {
      const arg = '01_vblock_txt_1300'
      // const expResult = [
      //   '01_vblock_txt_000',
      //   '01_vblock_txt_001',
      //   '01_vblock_txt_002',
      // ]
      expect(recordIdList(arg).length).toBe(1000);
      // console.log('recordIdList testing, recordIdList(arg) ->', recordIdList(arg))
    });
  });
});
