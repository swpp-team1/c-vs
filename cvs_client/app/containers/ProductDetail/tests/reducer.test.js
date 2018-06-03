
import { fromJS } from 'immutable';
import productDetailReducer from '../reducer';

describe('productDetailReducer', () => {
  it('returns the initial state', () => {
    expect(productDetailReducer(undefined, {})).toEqual(fromJS({}));
  });
});
