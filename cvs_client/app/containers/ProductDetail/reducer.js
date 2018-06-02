/*
 *
 * ProductDetail reducer
 *
 */

import { fromJS } from 'immutable';
import {
  DEFAULT_ACTION,
  RECEIVED_PRODUCT_DETAIL,
} from './constants';

const initialState = fromJS({});

function productDetailReducer(state = initialState, action) {
  switch (action.type) {
    case DEFAULT_ACTION:
      return state;
    case RECEIVED_PRODUCT_DETAIL:
      return fromJS({...state, productDetail: action.productDetail});
    default:
      return state;
  }
}

export default productDetailReducer;
