/*
 *
 * NewRecipe reducer
 *
 */

import { fromJS } from 'immutable';
import {
  DEFAULT_ACTION,
  RECEIVED_PRODUCT_LIST,
  IS_SUCCESSFUL_POST
} from './constants';

const initialState = fromJS({});

function newRecipeReducer(state = initialState, action) {
  switch (action.type) {
    case DEFAULT_ACTION:
      return state;
    case RECEIVED_PRODUCT_LIST:
      return fromJS({...state.toJS(), productList: action.productList});
    case IS_SUCCESSFUL_POST:
      return fromJS({...state.toJS(), isSuccessful: action.isSuccessful});
    default:
      return state;
  }
}

export default newRecipeReducer;
