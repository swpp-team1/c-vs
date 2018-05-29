
import { fromJS } from 'immutable';
import productAllReducer from '../reducer';

describe('productAllReducer', () => {
  it('returns the initial state', () => {
    expect(productAllReducer(undefined, {})).toEqual(fromJS({}));
  });
});
