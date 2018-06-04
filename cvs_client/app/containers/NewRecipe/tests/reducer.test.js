
import { fromJS } from 'immutable';
import newRecipeReducer from '../reducer';

describe('newRecipeReducer', () => {
  it('returns the initial state', () => {
    expect(newRecipeReducer(undefined, {})).toEqual(fromJS({}));
  });
});
