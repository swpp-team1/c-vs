import { take, call, put, select } from 'redux-saga/effects'
import request from 'utils/request'
import { SIGNUP_REQUEST } from './constants'

const signupURL = 'http://13.209.25.111:8000/signup/'


export function* signupRequest(username, password, email) {
  try {
    const data = yield call(request, signupURL, {
      method: 'POST',
      headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        username: username,
        password: password,
        email: email
      })
    })
    console.log(data)
  }
  catch(error) {
    (Promise.resolve(error.response)).then((value) => value.json()).then((body) => console.log(body))
  }
}

export function* watchSignupRequest() {
  while (true) {
    const {username, password, email} = yield take(SIGNUP_REQUEST)
    yield call(signupRequest, username, password, email)
  }
}

// All sagas to be loaded
export default [
  watchSignupRequest,
];
