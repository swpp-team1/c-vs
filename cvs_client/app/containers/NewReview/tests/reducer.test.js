
import { fromJS } from 'immutable';
import newReviewReducer from '../reducer';

describe('newReviewReducer', () => {
  it('returns the initial state', () => {
    expect(newReviewReducer(undefined, {})).toEqual(fromJS({}));
  });
});
