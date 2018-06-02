/*
 *
 * ProductDetail actions
 *
 */

import {
  DEFAULT_ACTION,
  REQUEST_PRODUCT_DETAIL,
  RECEIVED_PRODUCT_DETAIL,
} from './constants';

export function defaultAction() {
  return {
    type: DEFAULT_ACTION,
  };
}

export function requestProductDetail (id) {
  return {
    type: REQUEST_PRODUCT_DETAIL,
    id
  }
}

export function receivedProductDetail (productDetail) {
  return {
    type: RECEIVED_PRODUCT_DETAIL,
    productDetail: productDetail
  }
}
