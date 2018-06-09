import { take, call, put, select } from 'redux-saga/effects'
import * as actions from './actions'
import request from 'utils/request'
import { LOGIN_REQUEST } from './constants'

const loginURL = 'http://13.209.25.111:8000/login/'

export function* login(username, password) {
  console.log('!!')
  try {
    const data = yield call(request, loginURL, {
      method: 'POST',
      headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        username: username,
        password: password,
      })
    })
    yield put(actions.loginSucceeded(data))
  }
  catch(error) {
    yield put(actions.loginSucceeded())
  }
}

export function* watchLogin() {
  while (true) {
    const {username, password} = yield take(LOGIN_REQUEST)
    yield call(login, username, password)
  }
}

// All sagas to be loaded
export default [
  watchLogin
];
