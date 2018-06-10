/*
 *
 * NewReview reducer
 *
 */

import { fromJS } from 'immutable';
import {
  DEFAULT_ACTION, IS_SUCCESSFUL_POST,
} from './constants';

const initialState = fromJS({});

function newReviewReducer(state = initialState, action) {
  switch (action.type) {
    case DEFAULT_ACTION:
      return state;
    case IS_SUCCESSFUL_POST:
      return fromJS({...state.toJS(), isSuccessful: action.isSuccessful});
    default:
      return state;
  }
}

export default newReviewReducer;
