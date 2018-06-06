/*
 *
 * UserLogin reducer
 *
 */

import { fromJS } from 'immutable';
import {
  DEFAULT_ACTION,
  SIGNUP_RESULT,
  LOGIN_SUCCEEDED
} from './constants';

const initialState = fromJS({});

function userLoginReducer(state = initialState, action) {
  switch (action.type) {
    case DEFAULT_ACTION:
      return state;
    case SIGNUP_RESULT:
      return fromJS({...state.toJS(), signupSucceeded: action.succeeded, errorMessage: action.message})
    default:
      return state;
  }
}

export default userLoginReducer;
