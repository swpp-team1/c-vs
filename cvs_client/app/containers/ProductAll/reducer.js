/*
 *
 * ProductAll reducer
 *
 */

import { fromJS } from 'immutable';
import {
  DEFAULT_ACTION,
  PRODUCTS_LIST_RECEIVED
} from './constants';

const initialState = fromJS({});

function productAllReducer(state = initialState, action) {
  switch (action.type) {
    case DEFAULT_ACTION:
      return state;
    case PRODUCTS_LIST_RECEIVED:
      return fromJS({...state, productsList: action.productsList});
    default:
      return state;
  }
}

export default productAllReducer;
