/*
 *
 * ProductDetail actions
 *
 */

import {
  DEFAULT_ACTION,
  REQUEST_PRODUCT_DETAIL,
  RECEIVED_PRODUCT_DETAIL,
  REQUEST_RELATED_PRODUCTS,
  RECEIVED_RELATED_PRODUCTS,
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

export function requestRelatedProducts (smallCategory, largeCategory) {
  return {
    type: REQUEST_RELATED_PRODUCTS,
    smallCategory,
    largeCategory
  }
}

export function receivedRelatedProducts (relatedProducts) {
  return {
    type: RECEIVED_RELATED_PRODUCTS,
    relatedProducts: relatedProducts
  }
}
