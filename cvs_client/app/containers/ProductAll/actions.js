/*
 *
 * ProductAll actions
 *
 */

import {
  DEFAULT_ACTION,
  GET_ALL_PRODUCTS,
  PRODUCTS_LIST_RECEIVED,
} from './constants';

export function defaultAction() {
  return {
    type: DEFAULT_ACTION,
  };
}

export function getAllProducts(id) {
  return {
    type: GET_ALL_PRODUCTS,
    id
  }
}

export function productsListReceived(productsList) {
  return {
    type: PRODUCTS_LIST_RECEIVED,
    productsList: productsList
  }
}
