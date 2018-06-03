import { take, call, put, select, fork } from 'redux-saga/effects';
import * as actions from './actions'
import { REQUEST_PRODUCT_DETAIL, REQUEST_RELATED_PRODUCTS } from './constants'
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

export function* requestRelatedProducts(smallCategory, largeCategory) {
  try {
    const data = yield call(request, url + '?' + (smallCategory ? 'small_category=' + smallCategory :'') + (largeCategory ? '&large_category=' + largeCategory :''))
    yield put(actions.receivedRelatedProducts(data))
  }
  catch (error) {
    yield put(actions.receivedRelatedProducts())
  }
}

export function* watchRequestProductDetail() {
  while (true) {
    const { id } = yield take(REQUEST_PRODUCT_DETAIL)
    yield call(requestProductDetail, id)
  }
}

export function* watchRequestRelatedProducts() {
  while (true) {
    const { smallCategory, largeCategory } = yield take(REQUEST_RELATED_PRODUCTS)
    yield call(requestRelatedProducts, smallCategory, largeCategory)
  }
}

export function* defaultSaga() {
  yield fork(watchRequestProductDetail)
  yield fork(watchRequestRelatedProducts)
}

// All sagas to be loaded
export default [
  defaultSaga,
];
