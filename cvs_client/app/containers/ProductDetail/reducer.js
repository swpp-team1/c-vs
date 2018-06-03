/*
 *
 * ProductDetail reducer
 *
 */

import { fromJS } from 'immutable';
import {
  DEFAULT_ACTION,
  RECEIVED_PRODUCT_DETAIL,
  RECEIVED_RELATED_PRODUCTS,
} from './constants';

const initialState = fromJS({});

function productDetailReducer(state = initialState, action) {
  switch (action.type) {
    case DEFAULT_ACTION:
      return state;
    case RECEIVED_PRODUCT_DETAIL:
      return fromJS({...state.toJS(), productDetail: action.productDetail});
    case RECEIVED_RELATED_PRODUCTS:
      return fromJS({...state.toJS(), relatedProducts: action.relatedProducts});
    default:
      return state;
  }
}

export default productDetailReducer;
