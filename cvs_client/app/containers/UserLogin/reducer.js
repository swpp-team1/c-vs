/*
 *
 * UserLogin reducer
 *
 */

import { fromJS } from 'immutable';
import {
  DEFAULT_ACTION,
  SIGNUP_RESULT
} from './constants';

const initialState = fromJS({});

function userLoginReducer(state = initialState, action) {
  switch (action.type) {
    case DEFAULT_ACTION:
      return state;
    case SIGNUP_RESULT:
      console.log(action.message)
      return fromJS({...state.toJS(), signupSucceeded: action.succeeded, errorMessage: action.message})
    default:
      return state;
  }
}

export default userLoginReducer;
