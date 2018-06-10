import { take, call, put, select, fork } from 'redux-saga/effects';
import * as actions from './actions'
import { REQUEST_PRODUCT_LIST, SEND_REQUEST_POST } from './constants'
import request from 'utils/request'

const url = 'http://13.209.25.111:8000/products/'
const postURL = 'http://13.209.25.111:8000/posts/'

export const getUserInfo = (state) => state.get('global').toJS().loginResult;

export function* requestProductList(searchText) {
  if(searchText === '') {
    yield put(actions.receivedProductList())
    return
  }
  try {
    const data = yield call(request, url + '?search=' + searchText)
    yield put(actions.receivedProductList(data))
  }
  catch (error) {
    yield put(actions.receivedProductList())
  }
}

export function* sendRequestPost (posts) {
  for(let i=0; i<posts.length; i++) {
    const form = new FormData()
    form.set('review_id', 1)
    form.set('content', posts[i].content)
    form.set('image', posts[i].image)
    console.log(posts[i].image)
    const userInfo = yield select(getUserInfo)
    try {
      const data = yield call(request, postURL, {
        method: 'POST',
        headers: {
          'Authorization': 'Token ' + userInfo.token
        },
        body: form
      })
      console.log(data)
    } catch (e) {
      console.log(e)
    }
  }
}

export function* watchRequestProductList() {
  while (true) {
    const { searchText } = yield take(REQUEST_PRODUCT_LIST)
    yield call(requestProductList, searchText)
  }
}

export function* watchSendRequestPost() {
  while (true) {
    const { posts } = yield take(SEND_REQUEST_POST)
    yield call(sendRequestPost, posts)
  }
}

// All sagas to be loaded
export default [
  watchRequestProductList,
  watchSendRequestPost
];
