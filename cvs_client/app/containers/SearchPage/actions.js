/*
 *
 * SearchPage actions
 *
 */

import {DEFAULT_ACTION, SEARCH_PRODUCT, RECEIVED_SEARCH_RESULT} from './constants'

export function defaultAction() {
  return {
    type: DEFAULT_ACTION,
  };
}

export function searchProduct(searchKey){

  return{
    type: SEARCH_PRODUCT,
    searchKey
  };

}

export function receivedSearchResult (searchResult) {
  return {
    type: RECEIVED_SEARCH_RESULT,
    searchResult: searchResult
  }
}