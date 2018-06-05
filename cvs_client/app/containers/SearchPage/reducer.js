/*
 *
 * SearchPage reducer
 *
 */

import { fromJS } from 'immutable';
import {
  DEFAULT_ACTION,
  SEARCH_PRODUCT,
  RECEIVED_SEARCH_RESULT
} from './constants';

const initialState = fromJS({});

function searchPageReducer(state = initialState, action) {
  switch (action.type) {
    case DEFAULT_ACTION:
      return state;
    case RECEIVED_SEARCH_RESULT:
      return fromJS({...state.toJS(), searchResult: action.searchResult});
    default:
      return state;
  }
}

export default searchPageReducer;
