import { take, call, put, select, fork } from 'redux-saga/effects';
import * as actions from './actions'
import { REQUEST_PRODUCT_LIST } from './constants'
import request from 'utils/request'

const url = 'http://13.209.25.111:8000/products/'

export function* requestProductList(searchText) {
  if(searchText === '')
    yield put(actions.receivedProductList())
  try {
    const data = yield call(request, url + '?search=' + searchText)
    yield put(actions.receivedProductList(data))
  }
  catch (error) {
    yield put(actions.receivedProductList())
  }
}

export function* watchRequestProductList() {
  while (true) {
    const { searchText } = yield take(REQUEST_PRODUCT_LIST)
    yield call(requestProductList, searchText)
  }
}

// All sagas to be loaded
export default [
  watchRequestProductList,
];
