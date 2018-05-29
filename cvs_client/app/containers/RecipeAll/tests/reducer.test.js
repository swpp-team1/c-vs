
import { fromJS } from 'immutable';
import recipeAllReducer from '../reducer';

describe('recipeAllReducer', () => {
  it('returns the initial state', () => {
    expect(recipeAllReducer(undefined, {})).toEqual(fromJS({}));
  });
});
