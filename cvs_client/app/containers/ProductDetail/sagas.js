import { take, call, put, select } from 'redux-saga/effects';
import * as actions from './actions'
import { REQUEST_PRODUCT_DETAIL } from './constants'
import request from 'utils/request'

const url = 'http://13.209.25.111:8000/products/'

export function* requestProductDetail(id) {
  try {
    const data = yield call(request, url + id + '/')
    yield put(actions.receivedProductDetail(data))
  }
  catch (error) {
    yield put(actions.receivedProductDetail())
  }
}
export function* defaultSaga() {
  while (true) {
    const { id } = yield take(REQUEST_PRODUCT_DETAIL)
    yield call(requestProductDetail, id)
  }
}

// All sagas to be loaded
export default [
  defaultSaga,
];
