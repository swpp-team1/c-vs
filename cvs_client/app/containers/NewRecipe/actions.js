/*
 *
 * NewRecipe actions
 *
 */

import {
  DEFAULT_ACTION,
  REQUEST_PRODUCT_LIST,
  RECEIVED_PRODUCT_LIST,
  SEND_REQUEST_POST
} from './constants';

export function requestProductList (searchText) {
  return {
    type: REQUEST_PRODUCT_LIST,
    searchText
  }
}

export function receivedProductList (productList) {
  return {
    type: RECEIVED_PRODUCT_LIST,
    productList: productList
  }
}

export function sendRequestPost (post) {
  return {
    type: SEND_REQUEST_POST,
    post
  }
}

export function defaultAction() {
  return {
    type: DEFAULT_ACTION,
  };
}
